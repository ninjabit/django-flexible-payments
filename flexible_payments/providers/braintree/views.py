import braintree as sdk
from flexible_payments.providers.base import BaseProvider


class BraintreeProvider(BaseProvider):
    def __init__(self, merchant_id, public_key, private_key, sandbox=True, **kwargs):
        self.merchant_id = merchant_id
        self.public_key = public_key
        self.private_key = private_key

        super(BraintreeProvider, self).__init__(**kwargs)

    def get_client_token(self, request, transaction_uuid=None):
        pass

    def get_payment_token_from_request(self, payment, request):
        pass

    def capture(self, payment):
        pass

    def release(self, payment):
        pass

    def refund(self, payment):
        pass


