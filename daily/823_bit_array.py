"""
[MEDIUM]
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i
"""
class BitArray:
    def __init__(self, size: int) -> None:
        self.size = size
        self.array = [0] * size

    def set(self, i: int, val: int) -> None:
        if not 0 <= val <= 1:
            raise ValueError("val must be either 0 or 1.")
        self.array[i] = val

    def get(self, i: int) -> int:
        return self.array[i]


size = 5
ba = BitArray(size)
for i in range(size):
    print(ba.get(i))

ba.set(0, 1)
ba.set(1, 1)
ba.set(4, 1)
for i in range(size):
    print(ba.get(i))

try:
    ba.set(5, 1)
    assert False
except IndexError as e:
    assert True

try:
    ba.get(5)
    assert False
except IndexError as e:
    assert True

try:
    ba.set(-6, 1)
    assert False
except IndexError as e:
    assert True

try:
    ba.get(-6)
    assert False
except IndexError as e:
    assert True