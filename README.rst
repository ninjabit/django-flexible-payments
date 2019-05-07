=============================
django-flexible-payments
=============================

.. image:: https://badge.fury.io/py/django-flexible-payments.svg
    :target: https://badge.fury.io/py/django-flexible-payments

.. image:: https://travis-ci.org/ninjabit/django-flexible-payments.svg?branch=master
    :target: https://travis-ci.org/ninjabit/django-flexible-payments

.. image:: https://codecov.io/gh/ninjabit/django-flexible-payments/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ninjabit/django-flexible-payments

Reusable, extensible, integrated and independent Plans, Quotas, Payments, Invoices for Django.

Why
---

Taking inspiration from
silver,
django-payments,
django-getpaid,
django-plans,
django-invoices,
not having found the needed flexibility around the payment providers configuration and the users' subscription flow,
the flexible <plan,payment,billing,invoice> apps ecosystem
try to fill the gap leveraging a complete independent communication system among apps based on signals and hooks.
Any app in the ecosystem support the swappable models approach to let the developers use this library swapping the
default implementations with their own.
Any app of the ecosystem can be swapped out entirely and replaced with compatible ones, listening and emitting the same
signals, with the same high level api implementation.

For example, the signup flow, leveraging
django-registration
and the compatible app
django-allauth
can be integrated with django-flexible-plans to allow the user signup with the desired plan, have in the signup process the payment phase,
and eventually having the account with the subscription activated once the payment has been approved and received.

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

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
