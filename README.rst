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

``clockit`` uses the ``timeit`` module which accepts objects that are callable without arguments.

Distribution
------------

Install requirements::

    $ pip install -r requirements.txt

Bump the package version, then build a source distribution and a wheel::

    $ python setup.py sdist bdist_wheel 

Register the project with the PyPI test server::

    $ python setup.py register -r test

Use ``twine`` to safely upload previously built distributions to the PyPI test server::

    $ twine upload -r test dist/clockit-<version>*

If all is well, register the project with PyPI::

    $ python setup.py register

Finally, use ``twine`` to safely upload distributions to PyPI::

    $ twine upload dist/clockit-<version>*
