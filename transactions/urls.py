from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TransactionCreateListView.as_view(), name='transactions'),
    path('<int:transaction_id>/', views.TransactionDetailView.as_view(), name = "transaction_detail"),
    path('user/',views.UserTransactionsView.as_view(), name ='transaction_detail_by_user'),
]
