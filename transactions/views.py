from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import IncomeExpense
from rest_framework.permissions import IsAuthenticated


# Create your views here.



class TransactionCreateListView(generics.GenericAPIView):

    serializer_class = serializers.IncomeExpenseCreateSerializer
    queryset = IncomeExpense.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = IncomeExpense.objects.all()
        serializers = self.serializer_class(instance = transactions, many=True)
        return Response(data = serializers.data, status = status.HTTP_200_OK)
        #return Response(data ={"mess":'hello'})


    def post(self, request):
        data = request.data

        user = request.user
        serializers = self.serializer_class(data = data)
        if serializers.is_valid():
            serializers.save(user = user)
            return Response(data = serializers.data, status= status.HTTP_201_CREATED)
        
        return Response(data= serializers.errors, status = status.HTTP_400_BAD_REQUEST)



class TransactionDetailView(generics.GenericAPIView):

    serializer_class = serializers.IncomeExpenseDetailSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request, transaction_id):
        
        transaction = get_object_or_404(IncomeExpense, pk = transaction_id)
        serializer = self.serializer_class(instance = transaction)
        return Response(data = serializer.data, status = status.HTTP_200_OK)
    

    def put(self, request, transaction_id):
        data  = request.data

        transaction = get_object_or_404(IncomeExpense, pk= transaction_id)
        serializer = self.serializer_class(data = data, instance =transaction)

        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data, status= status.HTTP_200_OK)

        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, transaction_id):
        

        transaction.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
    

class UserTransactionsView(generics.GenericAPIView):

    serializer_class = serializers.IncomeExpenseDetailSerializer
    queryset = IncomeExpense.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        transaction = IncomeExpense.objects.all().filter(user = user)
        serializer = self.serializer_class(instance = transaction, many= True)
        return Response (data = serializer.data, status = status.HTTP_200_OK)
