# Grid n * m
# [0][0] = Robot
# Robot can only move to the right or down
# [n-1][m-1] = Goal
# No obstacles
#
# Sample Input m=2 n=2 output = 2
# [S][]
# [][F]
#
# Sample Input m=3 n=3 output = 6
# [S][][]
# [][][]
# [][][F]
#
# Input m=1 n=1 output = 0
# [SF]
#
# m >= 1 <=50
# n >= 1 <=50
#
# Base case
# Reached [n-1][m-1]
# Moving Right and reached [*][m-1]
# Moving Down and reached [n-1][*]

w = 0
z = 0


def number_of_unique_paths_logic(height: int, width: int) -> int:
    return _number_of_unique_paths(height, width)


# O(((m - 1) + (n - 1) C (m - 1)) * 2 - 1)
def _number_of_unique_paths(height: int, width: int, x: int=0, y: int=0) -> int:
    global w
    w += 1
    if x == height - 1 or y == width - 1:
        return 1
    return _number_of_unique_paths(height, width, x + 1, y) + _number_of_unique_paths(height, width, x, y + 1)


# O((2(m - 1) + 2(n - 1)) * O() of multiplication))
def number_of_unique_paths_math(height: int, width: int) -> int:
    return factorial(height - 1 + width - 1) // (factorial(height - 1) * factorial(width - 1))


def factorial(n: int) -> int:
    res = 1
    for i in range(1, n):
        res += product(res, i)
    return res


def product(a, b):
    global z
    res = 0
    for _ in range(0, b):
        z += 1
        res = addition(res, a)
    return res


def addition(a, b):
    global z
    while b:
        z += 1
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


if __name__ == '__main__':
    height = 5
    width = 5

    print(number_of_unique_paths_logic(height, width))
    print(w)
    # print(number_of_unique_paths_math(height, width))
    # print(z)
