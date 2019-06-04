from django.dispatch import Signal

transaction_refund = Signal(providing_args=['transaction'])
transaction_cancel = Signal(providing_args=['transaction'])
transaction_process = Signal(providing_args=['transaction'])
transaction_settled = Signal(providing_args=['transaction'])
