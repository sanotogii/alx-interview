#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    def is_prime(n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """Get all prime numbers up to n"""
        return [i for i in range(2, n + 1) if is_prime(i)]

    def play_game(n):
        """Simulate a single game"""
        primes = get_primes(n)
        return len(primes) % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
