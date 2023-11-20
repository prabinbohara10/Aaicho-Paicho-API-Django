from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import IncomeExpense


# Create your views here.
class TransactionCreateListView(generics.GenericAPIView):

    serializer_class = serializers.IncomeExpenseCreateSerializer
    queryset = IncomeExpense.objects.all()

    def get(self, request):
        transactions = IncomeExpense.objects.all()
        serializers = self.serializer_class(instance = transactions, many=True)
        return Response(data = serializers.data, status = status.HTTP_200_OK)
        #return Response(data ={"mess":'hello'})

    def post(self, request):
        pass


class TransactionDetailView(generics.GenericAPIView):

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
