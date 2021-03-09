"""
Asked by Uber

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6]

Follow-up: what if you can't use division?
"""


def product_of_array(l):
    product = 1
    for i in l:
        product *= i
    products = []
    for i in l:
        products.append(product / i)
    return products


def product_of_array_v2(l):
    n = len(l)
    products = []
    left = 1
    for i in range(n):
        if i > 0:
            left *= l[i - 1]
        products.append(left)
    right = 1
    for i in range(n - 1, -1, -1):
        if i < n -1:
            right *= l[i + 1]
        products[i] *= right
    return products


if __name__ == "__main__":
    print(product_of_array([1, 2, 3, 4, 5]))
    print(product_of_array([3, 2, 1]))
    print(product_of_array_v2([1, 2, 3, 4, 5]))
    print(product_of_array_v2([3, 2, 1]))
