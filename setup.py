from setuptools import setup


with open('README.rst') as readme:
    long_description = readme.read()


setup(
    name='clockit',
    version='0.2.4',
    description='Tool for timing the execution of Python functions',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='clockit',
    url='https://github.com/rlucioni/clockit',
    author='Renzo Lucioni',
    author_email='renzo@lucioni.email',
    license='MIT',
    py_modules=['clockit'],
)
