from django.contrib import admin

from flexible_payments.models.transactions import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = ('created',)
