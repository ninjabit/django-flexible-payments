from django_filters import CharFilter, BooleanFilter, FilterSet, NumberFilter

from flexible_payments.models import PaymentMethod, Transaction


class PaymentMethodFilter(FilterSet):
    processor = CharFilter(name='payment_processor', lookup_expr='iexact')
    canceled = BooleanFilter(name='canceled')
    verified = BooleanFilter(name='verified')

    class Meta:
        model = PaymentMethod
        fields = ['processor', 'canceled', 'verified']


class TransactionFilter(FilterSet):
    payment_processor = CharFilter(
        name='payment_method__payment_processor',
        lookup_expr='iexact'
    )
    state = CharFilter(name='state')
    min_amount = NumberFilter(name='amount', lookup_expr='gte')
    max_amount = NumberFilter(name='amount', lookup_expr='lte')
    currency = CharFilter(name='currency', lookup_expr='iexact')
    disabled = BooleanFilter(name='disabled')

    class Meta:
        model = Transaction
        fields = ['payment_method', 'state', 'min_amount', 'max_amount',
                  'currency', 'disabled']
