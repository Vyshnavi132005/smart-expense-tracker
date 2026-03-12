from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.models import User 
 
from .models import Expense 
 
class StyledDateInput(forms.DateInput): 
    input_type = 'date' 
 
class ExpenseForm(forms.ModelForm): 
    class Meta: 
        model = Expense 
        fields = ['amount', 'category', 'description', 'date'] 
        widgets = { 
            'amount': forms.NumberInput(attrs={'step': '0.01'}), 
            'date': StyledDateInput(), 
        } 
 
class RegisterForm(UserCreationForm): 
    email = forms.EmailField(required=True) 
 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 
 
class LoginForm(AuthenticationForm): 
    username = forms.CharField(max_length=150)
