"""
Asked by Stripe

Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates
and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.

You can modify the input array in-place.
"""
from typing import List


def find_smallest_missing_positive_int(l: List[int]) -> int:
    size = len(l)
    for i in range(size):
        while 0 < l[i] < size and l[i] != l[l[i]]:
            l[l[i]], l[i] = l[i], l[l[i]]
    for i in range(1, size):
        if l[i] != i:
            return i
    return size


if __name__ == "__main__":
    l = [0, 1, 2, 3]
    print(find_smallest_missing_positive_int(l))
    l = [3, 4, -1, 1]
    print(find_smallest_missing_positive_int(l))
    l = [1, 2, 0]
    print(find_smallest_missing_positive_int(l))
