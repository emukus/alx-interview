#!/usr/bin/python3
"""A method to determine the winner of Prime Game as outlined in
the README"""


def prime_btwn(n):
    """
    calculate prime numbers btwn 1 and n
    Args:
        n (int): the number to calculate prime numbers up to
    Returns:
        int: the number of prime numbers btwn 1 and n
    """
    prime_numbers = 0

    for k in range(2, n + 1):
        is_prime = True
        for l in range(2, k // 2 + 1):
            if k % l == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers += 1
    return prime_numbers


def isWinner(x, nums):
    """
    Determines the winner of a game of prime numbers.
    Args:
        x (int): the number of rounds to play
        nums (list): the list of numbers n to play
    Returns:
       string: the winner of the game (Ben or Maria),
       or None if there is a tie
    """
    if not x or not nums:
        return None
    ben = 0
    maria = 0
    for k in range(x):
        prime_nums = prime_btwn(nums[k])
        if prime_nums % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben == maria:
        return None
    winner = "Ben" if ben > maria else "Maria"
    return winner
