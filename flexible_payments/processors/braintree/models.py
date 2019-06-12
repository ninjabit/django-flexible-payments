import braintree
import swapper
from braintree.exceptions import NotFoundError
from django.contrib.postgres.fields import JSONField
from django.db import models
from flexible_payments.models import Transaction
from flexible_payments.models.payment_methods import PaymentMethod


class BraintreeCustomer(models.Model):
    data = JSONField(default=dict, null=True, blank=True)
    customer = models.ForeignKey(swapper.get_model_name('flexible_plans', 'Customer'), on_delete=models.CASCADE)


class BraintreePlan(models.Model):
    data = JSONField(default=dict, null=True, blank=True)
    plan = models.ForeignKey(swapper.get_model_name('flexible_plans', 'Plan'), on_delete=models.CASCADE)


class BraintreeSubscription(models.Model):
    data = JSONField(default=dict, null=True, blank=True)
    subscription = models.ForeignKey(swapper.get_model_name('flexible_plans', 'Subscription'), models.CASCADE)


class BraintreePaymentMethod(PaymentMethod):

    @property
    def token(self):
        return self.decrypt_data

    @property
    def braintree_id(self):
        return self.data.get('braintree_id')

    @property
    def braintree_transaction(self):
        try:
            return braintree.Transaction.find(self.braintree_id)
        except NotFoundError:
            return None

    class Meta:
        proxy = True


class BraintreeTransaction(models.Model):
    braintree_id = models.CharField(max_length=150, blank=True)
    transaction = models.ForeignKey('flexible_payments.Transaction', on_delete=models.CASCADE)
