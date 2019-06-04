# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from flexible_payments.views import TransactionListView, TransactionDetailView, PaymentMethodListView
from . import views

app_name = 'flexible_payments'
urlpatterns = [
    path('payment_methods/', PaymentMethodListView.as_view(), name='payment_method_list'),
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/<int:id>/', TransactionDetailView.as_view(), name='transaction_detail'),
]
