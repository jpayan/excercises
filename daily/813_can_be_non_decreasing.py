"""
[MEDIUM]
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can
modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any
one element to get a non-decreasing array.
"""
from typing import List


def can_be_non_decreasing(nums: List[int]) -> bool:
    previous_lowest = 0
    decrease_count = 0
    for num in nums:
        if num < previous_lowest:
            previous_lowest = num
            decrease_count += 1
            if decrease_count > 1:
                return False
    return True


if __name__ == '__main__':
    assert can_be_non_decreasing([10, 5, 7])
    assert can_be_non_decreasing([1, 5, 3, 4, 5, 6, 8])
    assert can_be_non_decreasing([])
    assert can_be_non_decreasing([0, 0, 0, 0, 0])
    assert not can_be_non_decreasing([10, 5, 1])
    assert not can_be_non_decreasing([5, 1, 3, 4, 2])
