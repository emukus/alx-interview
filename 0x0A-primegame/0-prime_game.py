#!/usr/bin/python3
"""A method to determine the winner of Prime Game as outlined in
the README"""


def isWinner(x, nums):
    """
    Determines the winner of a game of prime numbers.
    
    Args:
        x (int): the number of rounds to play
        nums (list): the list of numbers n to play
    
    Returns:
        string: the winner of the game (Ben or Maria), or None if there is a tie
    """
    if not x or not nums:
        return None
    
    def is_prime(num):
        """
        Determines whether a number is prime.
        
        Args:
            num (int): the number to check
            
        Returns:
            bool: True if the number is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    ben = 0
    maria = 0
    for num in nums:
        prime_nums = sum([1 for i in range(2, num+1) if is_prime(i)])
        if prime_nums % 2 == 0:
            ben += 1
        else:
            maria += 1
    
    if ben == maria:
        return None
    
    return "Ben" if ben > maria else "Maria"
