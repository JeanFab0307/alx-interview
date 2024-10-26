#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """
    Return:
        The name of the player tat won the most rounds
    """
    ben = 0
    maria = 0
    for i in range(x):
        prime = sievePrime(nums[i])

        if len(prime) % 2 != 0:
            maria += 1
        else:
            ben += 1

        if ben > x / 2:
            return "Ben"
        if maria > x / 2:
            return "Maria"
    return None


def sievePrime(n):
    """
        Return list of prime numbers between 1 and n inclusive
    """
    prime = []
    filtered = [True] * (n + 1)
    for p in range(2, n + 1):
        if (filtered[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                filtered[i] = False
    return prime
