from setuptools import setup

setup(
    name='qcqp',
    version='0.8.1',
    author='Jaehyun Park, Stephen Boyd',
    author_email='jpark@cs.stanford.edu, boyd@stanford.edu',
    packages=['qcqp'],
    license='MIT',
    zip_safe=False,
    install_requires=["cvxpy >= 0.4.8",
                      "CVXcanon >= 0.1.1"],
    use_2to3=True,
    url='http://github.com/cvxgrp/qcqp/',
    description='CVXPY extension for nonconvex QCQPs.',
    long_description='A CVXPY extension for nonconvex quadratically constrained quadratic programs.',
)
