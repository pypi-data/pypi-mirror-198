from setuptools import setup

setup(
    name='fibonacci2283371488',
    version='0.1',
    description='A package for calculating Fibonacci numbers and visualizing ASTs',
    py_modules=['fib'],
    install_requires=[
        'networkx',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'fibonacci=fib:main',
        ],
    },
)
