"""
Asked by Google
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def sum_in_list(l, k):
    component = set()
    for number in l:
        if k - number in component:
            return True
        else:
            component.add(number)
    return False


if __name__ == "__main__":
    l = [10, 15, 3, 7]
    k = 17
    print(sum_in_list(l, 17))
