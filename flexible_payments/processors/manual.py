from flexible_payments.processors.base import PaymentProcessorBase
from flexible_payments.processors.forms import GenericTransactionForm
from flexible_payments.processors.mixins import ManualProcessorMixin
from flexible_payments.processors.views import GenericTransactionView


class ManualProcessor(PaymentProcessorBase, ManualProcessorMixin):
    form_class = GenericTransactionForm
    transaction_view_class = GenericTransactionView

    def handle_transaction_response(self, transaction, request):
        pass

