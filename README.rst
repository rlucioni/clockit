clockit |PyPI|_ |Travis|_
=========================
.. |PyPI| image:: https://img.shields.io/pypi/v/clockit.svg?style=flat-square&maxAge=3600
.. _PyPI: https://pypi.python.org/pypi/clockit

.. |Travis| image:: https://img.shields.io/travis/rlucioni/clockit.svg?style=flat-square&maxAge=3600
.. _Travis: https://travis-ci.org/rlucioni/clockit

Tool for timing the execution of Python functions.

Installation
------------

Install with ``pip``::

    pip install clockit

Usage
-----

Run as follows::

    $ python
    >>> from clockit import clockit
    >>> def f(x, y=1):
    ...     return x, y
    ...
    >>> clocked = clockit(f, 1, y=2)
    >>> clocked.result
    (1, 2)
    >>> clocked.time
    0.0005593200330622494

``clockit`` uses the ``timeit`` module which accepts objects that are callable without arguments.
