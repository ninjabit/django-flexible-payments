from django.conf import settings

# Default dummy provider
PAYMENT_PROVIDERS = {
    'default': ('payments.dummy.DummyProvider', {})}

# Cache used to store providers
PROVIDER_CACHE = {}


class BaseProvider(object):
    """
    This class defines the provider API.
    Providers need to subclass this and implement their custom logic in the provided methods.
    It should not be instantiated directly. Use factory instead.
    """
    def __init__(self, capture=True):
        self._capture = capture

    def get_payment_token_from_request(self, payment, request):
        """
        Returns the payment token from payment provider request
        :param payment: the payment object
        :param request: the httprequest object
        :return: payment token
        """
        raise NotImplementedError()

    def capture(self, payment):
        """

        :param payment:
        :return:
        """
        raise NotImplementedError()

    def release(self, payment):
        """

        :param payment:
        :return:
        """
        raise NotImplementedError()

    def refund(self, payment):
        """

        :param payment:
        :return:
        """
        raise NotImplementedError()


def provider_factory(variant):
    """
    Provider factory
    Use this function to instantiate providers with proper variant
    :param variant: name of the provider
    :return: Provider instance
    """
    # Loads payments providers configured in settings or the default dummy provider otherwise
    variants = getattr(settings, 'PAYMENT_PROVIDERS', PAYMENT_PROVIDERS)

    # Extracts handler and config from the payment providers requested by variant
    handler, config = variants.get(variant, (None, None))
    if not handler:
        # If the requested provider is not installed raise an error
        raise ValueError("The provider is not installed: %s" % variant)
    if variant not in PROVIDER_CACHE:
        module_path, class_name = handler.rsplit('.', 1)
        # Dynamic import of the module class, by path and class name
        module = __import__(
            str(module_path), globals(), locals(), [str(class_name)]
        )
        class_ = getattr(module, class_name)
        # Add the provider instance to the provider cache
        PROVIDER_CACHE[variant] = class_(**config)
    return PROVIDER_CACHE[variant]

