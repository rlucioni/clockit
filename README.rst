clockit
=======

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
