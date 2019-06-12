from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from flexible_payments.api.v1.serializers import PaymentMethodSerializer, TransactionSerializer
from flexible_payments.models import PaymentMethod, Transaction
from flexible_payments.processors.braintree.payment_processor import BraintreePaymentProcessor
from flexible_payments.processors.utils import get_instance


class BraintreeTokenView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        payment_processor = get_instance('Braintree')
        if not isinstance(payment_processor, BraintreePaymentProcessor):
            return Response(
                {'detail': 'Braintree processor error'}
            )
        client_token = payment_processor.client_token()
        return Response(client_token)


class BraintreeTransactionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        nonce = kwargs.get('nonce')
        if not nonce:
            return Response(
                {'detail': 'Braintree nonce not present'}
            )
        return Response()


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PaymentMethodSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer
