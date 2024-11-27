#!/usr/bin/python3
"""
Method to calculate the minimum operations to achieve exactly n H characters.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in n H characters.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
