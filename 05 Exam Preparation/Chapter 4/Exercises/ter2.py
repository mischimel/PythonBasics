"""
ter2. Prime number (using a Python package)
Write a program that uses a Python package for checking if an integer is a prime number or not.
The Python Package Index (PyPI, https://pypi.org/) is a repository of software for the Python programming language.
"""
import sympy

number = int(input("Please enter an integer: "))

if sympy.isprime(number):
    print(number, "is a prime number.")
else:
    print(number, "is NOT a prime number.")