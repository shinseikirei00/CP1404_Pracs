"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(4))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n <= 0:
        print(0)
    else:
        print(n ** 2)
        do_something(n - 1)


do_something(4)
