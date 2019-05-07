import swapper as swapper
from django.db import models

from model_utils.models import TimeStampedModel


class Order(TimeStampedModel):
    products = models.ManyToManyField('Product', related_name='+')
    customer = models.ForeignKey(swapper.get_model_name('flexible_plans', 'Customer'), on_delete=models.DO_NOTHING)
