#!/usr/bin/python3
"""MinOperations."""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve exactly
    n H characters in the file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations needed to achieve n H characters.
             If n is impossible to achieve, returns 0.
    """
    if n == 1:
        return 0 

    a = [float('inf')] * (n + 1)
    a[1] = 0
 
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                a[i] = min(a[i], a[j] + (i // j))

    return a[n] if a[n] != float('inf') else 0
