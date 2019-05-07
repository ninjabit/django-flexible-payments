from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    item_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name='object',
        on_delete=models.CASCADE
    )
    item_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        db_index=True
    )
    item = GenericForeignKey('item_type', 'item_id')
