"""
[EASY]
This problem was asked by Square.

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all prime numbers less than 100, we would first mark [4, 6, 8, ...] (multiples of two),
then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N,
the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, withou taking N as an input)
"""
import itertools


def sieve_of_eratosthenes(n: int) -> list:
    nums = [i for i in range(2, n)]
    for i in range(2, n):
        for num in nums:
            if num != i and num % i == 0:
                nums.remove(num)
    return nums


assert sieve_of_eratosthenes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def prime_generator():
    yield 2
    yield 3
    nums = [2, 3]
    i = 4
    while True:
        prime = True
        for num in nums:
            if i % num == 0:
                prime = False
                break
        if prime:
            yield i
        nums.append(i)
        i += 1

assert list(itertools.takewhile(lambda x: x < 100, prime_generator())) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]