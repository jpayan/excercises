from typing import List


def zero_array(arr: List[int]) -> int:
    if sum(arr) != 0:
        return -1
    j = len(arr) - 1
    left = 0
    right = 0
    for i in range(len(arr)):
        left += arr[i]
        right += arr[j]
        if left + right == 0 and i == j - 1:
            return j
        if left == 0 and i == len(arr) - 1:
            return 0
        j -= 1


if __name__ == '__main__':
    print(zero_array([1, 2, 3, 4, 5]))
    # Expected: -1

    print(zero_array([2, -3, -4, 2, 2, 1]))
    # Expected: 3

    print(zero_array([-1, 1]))
    # Expected: 1

    print(zero_array([-2, 4, -3, -3, 6, -4, 2]))
    # Expected: 0
