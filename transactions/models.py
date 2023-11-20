from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()



class IncomeExpense(models.Model):
    
    TRANSACTION_TYPES = (
        ('INCOME','income'),
        ('EXPENSE', 'expense')
    )

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    transaction_type = models.CharField(max_length= 20, choices= TRANSACTION_TYPES, default= TRANSACTION_TYPES[0][0])
    category = models.CharField(max_length=50)
    amount = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    def __str__(self):
        return f"<Transcation {self.amount} in {self.transaction_type} by {self.user.email}>"



