=====
Usage
=====

To use django-flexible-payments in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'flexible_payments.apps.FlexiblePaymentsConfig',
        ...
    )

Add django-flexible-payments's URL patterns:

.. code-block:: python

    from flexible_payments import urls as flexible_payments_urls


    urlpatterns = [
        ...
        url(r'^', include(flexible_payments_urls)),
        ...
    ]
