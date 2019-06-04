from django.urls import path, include

from flexible_payments.api.v1.views import BraintreeTokenView, BraintreeTransactionView

urlpatterns = [
    path('braintree/token/', BraintreeTokenView.as_view(), name='client_token'),
    path('braintree/pay/', BraintreeTransactionView.as_view(), name='pay'),
]
