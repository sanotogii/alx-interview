#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game for multiple rounds.

    :param x: Number of rounds
    :param nums: An array of n for each round
    :return: Name of the player that won the most rounds,
    or None if it's a tie
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    primes_up_to = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        primes_up_to[i] = primes_up_to[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    for n in nums:
        if primes_up_to[n] % 2 == 1:
            maria_wins += 1

    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None
