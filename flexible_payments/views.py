# -*- coding: utf-8 -*-
from braces.views import StaffuserRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from flexible_payments.models.payment_methods import PaymentMethod
from flexible_payments.models.transactions import Transaction


class PaymentMethodListView(StaffuserRequiredMixin, ListView):
    model = PaymentMethod


class PaymentMethodDetailView(StaffuserRequiredMixin, DetailView):
    model = PaymentMethod


class TransactionListView(StaffuserRequiredMixin, ListView):
    model = Transaction


class TransactionDetailView(StaffuserRequiredMixin, DetailView):
    model = Transaction
