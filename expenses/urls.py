from django.urls import path 
 
from .views import CustomLoginView, about_view, delete_expense_view, download_csv_view, edit_expense_view, home_view, logout_view, register_view 
 
urlpatterns = [ 
    path('', home_view, name='home'), 
    path('about/', about_view, name='about'), 
    path('register/', register_view, name='register'), 
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', logout_view, name='logout'), 
    path('edit/<int:expense_id>/', edit_expense_view, name='edit_expense'), 
    path('delete/<int:expense_id>/', delete_expense_view, name='delete_expense'), 
    path('download-csv/', download_csv_view, name='download_csv'), 
]
