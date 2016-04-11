from setuptools import setup


with open('README.rst') as readme:
    long_description = readme.read()


setup(
    name='clockit',
    version='0.1.0',
    description='Tool for timing the execution of Python functions',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 3 - Alpha',
    ],
    keywords='clockit',
    url='https://github.com/rlucioni/clockit',
    author='Renzo Lucioni',
    author_email='renzo@lucioni.email',
    license='MIT',
    py_modules=['clockit'],
)
