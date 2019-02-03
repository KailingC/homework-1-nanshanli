"""Spring 2019 COMSW 4995: Applied Machine Learning.

UNI: nl2643
Homework 1 Task 1.2

Tests for fib function within fib.py

"""

from task1.task12 import fib


def test_two():
    """Check that fib(2) == 1."""
    assert fib(2) == 1


def test_five():
    """Check that fib(5) == 5."""
    assert fib(5) == 5


def test_twelve():
    """Check that fib(12) == 144."""
    assert fib(12) == 144
