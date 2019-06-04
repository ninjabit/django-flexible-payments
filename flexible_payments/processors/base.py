from django.conf import settings
from django.template.loader import select_template
from django.utils.deconstruct import deconstructible


@deconstructible
class PaymentProcessorBase(object):
    """

    """
    form_class = None
    template_slug = None
    payment_method_class = None
    transaction_view_class = None
    allowed_currencies = ()

    def __init__(self, name):
        self.name = name

    def get_form(self, transaction, request):
        form = None
        if self.form_class:
            form = self.form_class(
                payment_method=transaction.payment_method,
                transaction=transaction,
                request=request
            )
        return form

    def get_template(self, transaction):
        template = select_template([
            'forms/{}/transaction_form.html'.format(
                self.template_slug
            ),
            'forms/transaction_form.html'
        ])

        return template

    def get_view(self, transaction, request, **kwargs):
        assert self.transaction_view_class, 'You must specify a `transaction_view_class` ' \
                                            'attribute for the {} class.'.format(
                                                self.__class__.__name__
                                            )

        kwargs.update({
            'form': self.get_form(transaction, request),
            'template': self.get_template(transaction),
            'transaction': transaction,
            'request': request
        })
        return self.transaction_view_class.as_view(**kwargs)

    def handle_transaction_response(self, transaction, request):
        raise NotImplementedError

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.__class__ is other.__class__

    def __ne__(self, other):
        return not self.__eq__(other)


