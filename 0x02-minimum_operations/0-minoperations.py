#!/usr/bin/python3
"""Calculates the fewest no of operations needed to result in exactly n
no of characters in a file"""


def minOperations(n):
    """Returns the fewest no. of operations needed"""
    operations = 0
    iterator = 2
    
    while n > 1:
        while n % iterator == 0:
            operations += iterator
            n /= iterator
        iterator +=1
    return operations
