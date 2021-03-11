"""
[MEDIUM]
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random
from math import sqrt


def estimate_pi() -> float:
    iterations = 1000000
    x = 0
    for i in range(iterations):
        x += sqrt(1 - random.random() ** 2)
    return 4 * x / iterations


if __name__ == '__main__':
    pi = estimate_pi()
    print(pi)
    assert 3.140 <= pi <= 3.149
