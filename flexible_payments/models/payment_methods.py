import swapper
from cryptography.fernet import Fernet, InvalidToken
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.conf import settings
from model_utils.managers import InheritanceManager
from model_utils.models import TimeStampedModel


class PaymentMethod(TimeStampedModel):
    class PaymentProcessors:
        @classmethod
        def as_choices(cls):
            for name in settings.PAYMENT_PROCESSORS.keys():
                yield (name, name)

        @classmethod
        def as_list(cls):
            return [name for name in settings.PAYMENT_PROCESSORS.keys()]

    payment_processor = models.CharField(choices=PaymentProcessors.as_choices(),
                                         blank=False, null=False, max_length=256)
    customer = models.ForeignKey(
        swapper.get_model_name('flexible_plans', 'Customer'),
        on_delete=models.CASCADE
    )
    data = JSONField(default=dict, blank=True, null=True)

    verified = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)

    objects = InheritanceManager()

    def encrypt_data(self, data):
        key = settings.PAYMENT_METHOD_SECRET
        return Fernet(key).encrypt(bytes(data))

    def decrypt_data(self, crypted_data):
        key = settings.PAYMENT_METHOD_SECRET

        try:
            return str(Fernet(key).decrypt(bytes(crypted_data)))
        except InvalidToken:
            return None


