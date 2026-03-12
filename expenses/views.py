import calendar 
import csv 
from datetime import date 
 
from django.contrib import messages 
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LoginView 
from django.db.models import Count, Sum 
from django.db.models.functions import ExtractMonth 
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404, redirect, render 
 
from .forms import ExpenseForm, LoginForm, RegisterForm 
from .models import Expense 
 
class CustomLoginView(LoginView): 
    template_name = 'login.html' 
    authentication_form = LoginForm 
    redirect_authenticated_user = True 
 
def register_view(request): 
    if request.user.is_authenticated: 
        return redirect('home') 
    if request.method == 'POST': 
        form = RegisterForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            messages.success(request, 'Account created successfully.') 
            return redirect('home') 
    else: 
        form = RegisterForm() 
    return render(request, 'register.html', {'form': form}) 
 
def about_view(request): 
    return render(request, 'about.html') 
 
@login_required 
def logout_view(request): 
    logout(request) 
    messages.info(request, 'You have been logged out.') 
    return redirect('login')
 
@login_required 
def home_view(request): 
    selected_month = request.GET.get('month', '') 
    if request.method == 'POST': 
        form = ExpenseForm(request.POST) 
        if form.is_valid(): 
            expense = form.save(commit=False) 
            expense.user = request.user 
            expense.save() 
            messages.success(request, 'Expense added successfully.') 
            return redirect('home') 
    else: 
        form = ExpenseForm(initial={'date': date.today()}) 
    user_expenses = Expense.objects.filter(user=request.user) 
    filtered_expenses = user_expenses 
    if selected_month and selected_month.isdigit(): 
        filtered_expenses = filtered_expenses.filter(date__month=int(selected_month)) 
    summary = filtered_expenses.aggregate(total_spending=Sum('amount'), total_transactions=Count('id')) 
    category_data = filtered_expenses.values('category').annotate(total=Sum('amount')).order_by('category') 
    monthly_data = user_expenses.annotate(month=ExtractMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month') 
    categories = [item['category'] for item in category_data] 
    totals = [float(item['total']) for item in category_data] 
    months = [calendar.month_name[item['month']] for item in monthly_data if item['month']] 
    month_totals = [float(item['total']) for item in monthly_data] 
    context = {'form': form, 'expenses': filtered_expenses, 'selected_month': selected_month, 'month_choices': list(enumerate(calendar.month_name))[1:], 'total_spending': summary['total_spending'] or 0, 'total_transactions': summary['total_transactions'] or 0, 'categories': categories, 'totals': totals, 'months': months, 'month_totals': month_totals} 
    return render(request, 'home.html', context) 
 
@login_required 
def edit_expense_view(request, expense_id): 
    expense = get_object_or_404(Expense, id=expense_id, user=request.user) 
    if request.method == 'POST': 
        form = ExpenseForm(request.POST, instance=expense) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, 'Expense updated successfully.') 
            return redirect('home') 
    else: 
        form = ExpenseForm(instance=expense) 
    return render(request, 'edit.html', {'form': form, 'expense': expense}) 
 
@login_required 
def delete_expense_view(request, expense_id): 
    expense = get_object_or_404(Expense, id=expense_id, user=request.user) 
    expense.delete() 
    messages.success(request, 'Expense deleted successfully.') 
    return redirect('home') 
 
@login_required 
def download_csv_view(request): 
    expenses = Expense.objects.filter(user=request.user).order_by('-date', '-id') 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment; filename=expenses.csv' 
    writer = csv.writer(response) 
    writer.writerow(['Amount', 'Category', 'Description', 'Date']) 
    for expense in expenses: 
        writer.writerow([expense.amount, expense.category, expense.description, expense.date]) 
    return response
