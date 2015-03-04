from setuptools import setup


tests_require = ['nose']


setup(
    name='recontool',
    description='command line accounting tool',
    version='0.0.1',
    url='http://github.com/cieplak/recontool',
    author='patrick cieplak',
    author_email='patrick.cieplak@gmail.com',
    test_suite='nose.collector',
    scripts=[
        'bin/recontool'
    ],
    packages=['recontool'],
    install_requires=[
        'ipython',
        'click',
    ],
    tests_require=tests_require,
)
