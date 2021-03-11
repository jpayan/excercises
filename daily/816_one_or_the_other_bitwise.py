"""
[MEDIUM]
This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0
using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""
# a = 5  = 0000 0101
# b = 15 = 0000 1111
# --------------
# a & b  = 0000 0101 = (5) (1s in both bits)
# --------------
# a | b  = 0000 1111 (15) (1s in any bit)
# --------------
# a ^ b  = 0000 1010 (10) (1s only in one bit)
# --------------
# a << 1 = 0000 1010 (10) (shift a left by 1 bit)
# --------------
# b << 1 = 0001 1110 (30) (shift b left by 1 bit)
# --------------
# a << b = 0010 1000 0000 0000 0000 (163840) (shift a left by b bits)
# --------------
# b << a = 0001 1110 0000 (480) (shift b left by a bits)
# --------------
# a >> 2 = 0000 0010 (2) (shift a right by 1 bit)
# --------------
# b >> 1 = 0000 0111 (7) (shift b right by 1 bit)
# --------------
# a >> b = 0000 0000 (0) (shift a right by b bits)
# --------------
# b >> a = 0000 0000 (5) (shift b right by a bits)
# --------------
# ~a     =-0000 0110 (-6) (-(a + 1))
# --------------
# ~b     =-0001 0000 (30) (-(b + 1))


def one_or_the_other_bitwise(x: int, y: int, b: int) -> int:
    return (x & -b) | (y & ~-b)


def one_or_the_other_math(x: int, y: int, b: int) -> int:
    return y + (x - y) * b


if __name__ == '__main__':
    assert one_or_the_other_bitwise(15, 37, 0) == 37
    assert one_or_the_other_bitwise(15, 37, 1) == 15

    assert one_or_the_other_math(15, 37, 0) == 37
    assert one_or_the_other_math(15, 37, 1) == 15
