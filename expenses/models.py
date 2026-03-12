from django.conf import settings 
from django.db import models 
 
class Expense(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses') 
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    category = models.CharField(max_length=100) 
    description = models.CharField(max_length=255) 
    date = models.DateField() 
 
    class Meta: 
        ordering = ['-date', '-id'] 
 
    def __str__(self): 
        return f'{self.user.username} - {self.category} - {self.amount}'
