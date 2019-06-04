from django.http import HttpResponse
from django.views.generic import View
from rest_framework.exceptions import MethodNotAllowed


class GenericTransactionView(View):
    form = None
    template = None
    transaction = None
    request = None

    def get_context_data(self):
        return {
            'payment_method': self.transaction.payment_method,
            'transaction': self.transaction,
            'customer': self.transaction.customer,
            'form': self.form,
            # 'document': self.transaction.document,
            # 'provider': self.transaction.provider,
            # 'entries': list(self.transaction.document._entries),
            # 'payment_complete_url': get_payment_complete_url(self.transaction,
            #                                                 self.request)
        }

    def render_template(self):
        return self.template.render(context=self.get_context_data())

    def get(self, request):
        return HttpResponse(self.render_template())

    def post(self, request):
        return MethodNotAllowed
