import logging
from django_fsm import TransitionNotAllowed

logger = logging.getLogger(__name__)


class PaymentProcessorType(object):
    Manual = "manual"
    Automatic = "automatic"
    Triggered = "triggered"


class BaseProcessorMixin(object):
    """
    Interface for a payment processor
    """

    def refund_transaction(self, transaction):
        raise NotImplementedError

    def refund_partial_transaction(self, transaction, amount):
        raise NotImplementedError

    def void_transaction(self, transaction):
        raise NotImplementedError

    def process_transaction(self, transaction):
        try:
            transaction.process()
            transaction.save()
        except TransitionNotAllowed:
            logger.exception(
                "Error processing transaction %d" % transaction.pk
            )
            return False
        self.execute_transaction(transaction)

    def execute_transaction(self, transaction):
        raise NotImplementedError

    def fetch_transaction_status(self, transaction):
        """
            Implementation is optional.

            Used for payment processors that do not provide webhooks and require
            interrogations initiated by us, to obtain the status of the
            transaction.

            Should only be called for pending transactions that belong to the
            payment processor where this is implemented.

            Can be called for all pending transactions by using the management
            command with the same name.

            :return: True on success, False on failure.
        """

        return True


class ManualProcessorMixin(object):
    type = PaymentProcessorType.Manual


class AutomaticProcessorMixin(BaseProcessorMixin):
    type = PaymentProcessorType.Automatic

    def setup_automated_payments(self, customer):
        raise NotImplementedError


class TriggeredProcessorMixin(BaseProcessorMixin):
    type = PaymentProcessorType.Triggered
