"""
[HARD]
This problem was asked by Stripe

Given an array of intetgers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def get_first_missing_positive(nums: list) -> int:
    nums.append(0)
    n = len(nums)
    for i in range(n):
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    nums_set = {i for i in nums}
    for i in range(n + 1):
        if i > 0 and i not in nums_set:
            return i


assert get_first_missing_positive([3, 4, -1, 1]) == 2
assert get_first_missing_positive([1, 2, 0]) == 3
assert get_first_missing_positive([1, 2, 3]) == 4
assert get_first_missing_positive([0, -1, -35, 198]) == 1
assert get_first_missing_positive([]) == 1