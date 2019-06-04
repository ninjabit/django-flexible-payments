import uuid
import logging
import swapper
from django.contrib.postgres.fields import JSONField
from django.db import models, transaction
from django_fsm import FSMField, transition
from model_utils.models import TimeStampedModel
from djmoney.models.fields import MoneyField

from flexible_payments.signals import transaction_process, transaction_settled

logger = logging.getLogger(__name__)


class Transaction(TimeStampedModel):
    class STATE:
        INITIAL = 'initial'
        PENDING = 'pending'
        SETTLING = 'settling'
        SETTLED = 'settled'
        FAILED = 'failed'
        CANCELED = 'canceled'
        REFUNDED = 'refunded'

        @classmethod
        def as_list(cls):
            return [getattr(cls, state) for state in vars(cls).keys() if state[0].isupper()]

        @classmethod
        def as_choices(cls):
            return (
                (state, state.capitalize()) for state in cls.as_list()
            )

    uuid = models.UUIDField(default=uuid.uuid4)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    state = FSMField(choices=STATE.as_choices(), default=STATE.INITIAL)
    payment_method = models.ForeignKey(
        'flexible_payments.PaymentMethod',
        on_delete=models.DO_NOTHING
    )
    data = JSONField(default=dict, null=True, blank=True)

    @property
    def payment_processor(self):
        return self.payment_method.payment_processor

    @property
    def customer(self):
        return self.payment_method.customer

    ####################################
    # Finite State Machine Transitions #
    ####################################

    @transition(field=state, source=STATE.INITIAL, target=STATE.PENDING)
    def process(self):
        transaction_process.send(sender=self.__class__, transaction=self)
        pass

    @transition(field=state, source=[STATE.INITIAL, STATE.PENDING],
                target=STATE.SETTLED)
    def settle(self):
        transaction_settled.send(sender=self.__class__, transaction=self)
        pass

    @transition(field=state, source=[STATE.INITIAL, STATE.PENDING],
                target=STATE.CANCELED)
    def cancel(self, cancel_code='default', cancel_reason='Unknown cancel reason'):
        self.cancel_code = cancel_code
        logger.error(str(cancel_reason))

    @transition(field=state, source=[STATE.INITIAL, STATE.PENDING],
                target=STATE.FAILED)
    def fail(self, fail_code='default', fail_reason='Unknown fail reason'):
        self.fail_code = fail_code
        logger.error(str(fail_reason))

    @transition(field=state, source=STATE.SETTLED, target=STATE.REFUNDED)
    def refund(self, refund_code='default', refund_reason='Unknown refund reason'):
        self.refund_code = refund_code
        logger.error(str(refund_reason))

    @transaction.atomic()
    def save(self, *args, **kwargs):
        # TODO: emit signal? builtin signals should trigger automatically
        super(Transaction, self).save(*args, **kwargs)
