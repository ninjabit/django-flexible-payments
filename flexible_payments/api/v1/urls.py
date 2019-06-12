from django.urls import path, include
from rest_framework.routers import SimpleRouter

from flexible_payments.api.v1.views import BraintreeTokenView, BraintreeTransactionView, PaymentMethodViewSet, \
    TransactionViewSet

router = SimpleRouter()
router.register('payment-methods', PaymentMethodViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('braintree/token/', BraintreeTokenView.as_view(), name='client_token'),
    path('braintree/pay/', BraintreeTransactionView.as_view(), name='pay'),
    path('', include(router.urls)),
]
