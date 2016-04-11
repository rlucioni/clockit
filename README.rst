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
    >>> clockit(f, 1, y=2)
    0.00045296200551092625
