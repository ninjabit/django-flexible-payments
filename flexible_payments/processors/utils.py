from django.conf import settings
from django.utils.module_loading import import_string


def get_instance(name):
    data = settings.PAYMENT_PROCESSORS[name]
    klass = import_string(data['class'])
    kwargs = data.get('setup_data', {})
    return klass(name, **kwargs)


def get_all_instances():
    choices = []
    for processor_import_path in settings.PAYMENT_PROCESSORS.keys():
        choices.append(get_instance(processor_import_path))
    return choices


def get_providers_choices():
    choices = []
    for processor in settings.PAYMENT_PROCESSORS.keys():
        choices.append((processor, str(processor).capitalize()))
    return choices
