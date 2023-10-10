#!/usr/bin/python3
"""
Calculates the minimum number of operations to achieve 'n' 'H' characters
"""


def minOperations(n):
    """
    The minimum number of operations needed to achieve 'n' 'H' characters

    Args:
        n (int): The target number of 'H' characters

    Returns:
        int: The minimum number of operations needed
    """
    if n <= 1:
        return 0
    for op in range(2, n + 1):
        if n % op == 0:
            return minOperations(int(n / op)) + op
