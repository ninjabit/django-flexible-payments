from django.contrib import admin

from flexible_payments.models.products import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('item', 'created')
    list_filter = ('created',)
