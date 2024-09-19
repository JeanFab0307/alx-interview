#!/usr/bin/python3
"""make change."""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.
    Return:
    fewer number of coins needed to meet total
    Or 0 is total <= 0
    Or -1 if not possible
    """
    i = 0
    memo = total
    while total > 0:
        i += 1
        for coin in coins:
            memo1 = total - coin
            if memo1 < memo and memo1 >= 0:
                memo = memo1
        if total == memo:
            return -1
        total = memo
    if total <= 0:
        return i
