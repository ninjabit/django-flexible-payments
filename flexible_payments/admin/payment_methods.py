from django.contrib import admin

from flexible_payments.models import PaymentMethod


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_filter = ('payment_processor',)
