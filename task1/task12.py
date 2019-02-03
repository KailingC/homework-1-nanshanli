"""Spring 2019 COMSW 4995: Applied Machine Learning.

UNI: nl2643
Homework 1 Task 1.2

Contains function that computes fibonacci sequence

"""


def fib(n):
    """Find fibonacci sequence for a given value n."""
    prev = 1
    curr = 1

    if n == 1:
        return 1
    elif n == 2:
        return 1

    for i in range(3, n + 1):
        temp = prev + curr
        prev = curr
        curr = temp

    return curr
