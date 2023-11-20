from django.contrib import admin
from .models import IncomeExpense

# Register your models here.

@admin.register(IncomeExpense)
class IncomeExpenseAdmin(admin.ModelAdmin):
    list_display = ['user','transaction_type','amount','updated_at']
    list_filter = ['created_at','transaction_type', 'user']