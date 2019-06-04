=============================
django-flexible-payments
=============================

.. image:: https://badge.fury.io/py/django-flexible-payments.svg
    :target: https://badge.fury.io/py/django-flexible-payments

.. image:: https://travis-ci.org/ninjabit/django-flexible-payments.svg?branch=master
    :target: https://travis-ci.org/ninjabit/django-flexible-payments

.. image:: https://codecov.io/gh/ninjabit/django-flexible-payments/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ninjabit/django-flexible-payments

Independent and reusable Payment app for Django, used to build the Django Subscription Plan System.

Why
---

Taking inspiration from
silver
django-payments
django-getpaid
django-plans
django-invoices
django-flexible-payments offers a customizable approach to support payments;
PaymentMethod and Transaction are connected with their PaymentProcessor

How
---



Documentation
-------------

The full documentation is at https://django-flexible-payments.readthedocs.io.

Quickstart
----------

Install django-flexible-payments::

    pip install django-flexible-payments

Add it to your `INSTALLED_APPS`:

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
        url(r'^payments/', include(flexible_payments_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_
*  `django-fsm`_
*  `django-money`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _django-fsm: https://github.com/viewflow/django-fsm
.. _django-money: https://github.com/django-money/django-money
