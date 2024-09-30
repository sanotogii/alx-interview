# Prime Game

## Description

This project revolves around a competitive game between two players, Maria and Ben. The game involves selecting prime numbers from a set of consecutive integers, removing them and their multiples from the set. The player unable to make a move loses the game. 

You are tasked with implementing the function `isWinner(x, nums)`, which determines who wins the most rounds of the game, given that both players play optimally. Maria always goes first.

## Concepts Needed

### Prime Numbers
- **Understanding Prime Numbers**: A prime number is a number greater than 1 that has no divisors other than 1 and itself.
- **Efficient Prime Detection**: Since the game involves removing prime numbers and their multiples, understanding efficient ways to detect primes is crucial.

### Sieve of Eratosthenes
- **Prime Number Calculation**: The Sieve of Eratosthenes is a highly efficient algorithm for finding all prime numbers up to a given limit, which is useful for optimizing the solution to this game.
  
### Game Theory
- **Turn-based Competitive Games**: Understanding the mechanics of two-player games where each player makes moves in turn, and each player aims to win by making optimal decisions.
- **Optimal Play**: Both players are assumed to play optimally, meaning they will make the best possible move at every step.

### Dynamic Programming/Memoization
- **Optimization**: To improve the performance of the game simulation, dynamic programming or memoization techniques can be used to avoid recalculating results.

## Requirements
- Python 3 (version 3.4.3) on Ubuntu 20.04 LTS.
- Files must be PEP 8 compliant.
- Implement a `README.md` at the root of the project.
- Your code should be executable and not import external libraries.

## Tasks

### 0. Prime Game

Implement the function `isWinner(x, nums)`:
- `x`: the number of rounds.
- `nums`: an array of `n`, where each `n` represents the maximum number in the set for that round.
- The function should return the name of the player who won the most rounds ("Maria" or "Ben").
- If the winner cannot be determined (i.e., if both players win the same number of rounds), return `None`.

### Example

Consider `x = 3` and `nums = [4, 5, 1]`:
1. **Round 1** (`n = 4`): Maria picks 2, removes multiples of 2. Ben picks 3 and wins.
2. **Round 2** (`n = 5`): Maria picks 2, Ben picks 3, Maria picks 5 and wins.
3. **Round 3** (`n = 1`): Ben wins automatically as there are no prime numbers to choose.

Result: Ben wins 2 rounds, and Maria wins 1 round, so the function should return `"Ben"`.

## Resources

- **Prime Numbers**:
  - [Khan Academy: Introduction to Prime Numbers](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:foundation/x2f8bb11595b61c86:prime-composite-numbers/v/prime-numbers-introduction)
  - [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
  
- **Game Theory**:
  - [Game Theory Basics](https://www.khanacademy.org/economics-finance-domain/microeconomics/nash-equilibrium-tutorial/game-theory/v/game-theory-nash-equilibrium)

- **Dynamic Programming**:
  - [Dynamic Programming With Python Examples](https://realpython.com/python-dynamic-programming/)

## Mock Technical Interview

You can practice the concepts for this project in mock technical interviews for preparation.

---

## Repository

- **GitHub repository**: `alx-interview`
- **Directory**: `0x0A-primegame`
- **File**: `0-prime_game.py`
