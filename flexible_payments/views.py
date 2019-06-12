# -*- coding: utf-8 -*-
from braces.views import StaffuserRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)
from django.views.generic.base import View

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


class PaymentView(View):
    pass


# Temporary payment function view taken from django 2 by example

def payment_process(request):
    from flexible_products.models import Order
    import braintree

    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # retrieve payment nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        transaction_options = {

        }
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.total),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
