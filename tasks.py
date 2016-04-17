"""Task functions for use with Invoke."""
from invoke import ctask as task


@task
def pep8(context):
    """Run pep8 quality checks."""
    pep8 = 'pep8 clockit.py'
    context.run(pep8)


@task
def pylint(context):
    """Run pylint quality checks."""
    pylint = 'pylint --reports=no clockit.py'
    context.run(pylint)


@task(pep8, pylint)
def quality(context):
    """Check code quality."""
    pass
