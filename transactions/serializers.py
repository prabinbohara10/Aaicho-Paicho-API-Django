from .models import IncomeExpense
from rest_framework import serializers


class IncomeExpenseCreateSerializer(serializers.ModelSerializer):

    transaction_type = serializers.CharField(max_length= 20)
    category = serializers.CharField(max_length=50)
    amount = serializers.IntegerField() 

    class Meta:
        model = IncomeExpense
        fields = ['id','transaction_type','category','amount']


class IncomeExpenseDetailSerializer(serializers.ModelSerializer):

    transaction_type = serializers.CharField(max_length= 20)
    category = serializers.CharField(max_length=50)
    amount = serializers.IntegerField() 
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateField()

    class Meta:
        model = IncomeExpense
        fields = ['transaction_type','category','amount','created_at','updated_at']