# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.

# Do both operations in O(1) time


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.store = dict()
        self.priority_head = Node(None)
        self.priority_tail = Node(None)
        self.priority_head.next = self.priority_tail
        self.priority_tail.previous = self.priority_head

    def get(self, key):
        if key in self.store:
            item = self.store[key]
            self._pull_out_item(item)
            self._prioritize_item(item)
            return item.value
        else:
            return -1

    def put(self, key, value):
        item = None
        if key in self.store:
            item = self.store[key]
            item.value = value
            self._pull_out_item(item)
        else:
            if self.size + 1 >  self.capacity:
                self._evict_item()  
            item = Node(key, value)
            self.store[key] = item
            self.size += 1
        self._prioritize_item(item)
    
    def _evict_item(self):
        del self.store[self.priority_tail.previous.key]
        self._pull_out_item(self.priority_tail.previous)
        self.size -= 1

    def _pull_out_item(self, item):
        item.previous.next = item.next
        item.next.previous = item.previous
    
    def _prioritize_item(self, item):
        item.next = self.priority_head.next
        item.previous = self.priority_head
        self.priority_head.next.previous = item
        self.priority_head.next = item


class Node(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

# cache = LRUCache(1)
# cache.put(2, 1)
# print(cache.get(2))

# cache = LRUCache(2)
# cache.put(2, 1)
# cache.put(2, 2)
# print(cache.get(2))
# cache.put(1, 1)
# cache.put(4, 1)
# print(cache.get(2))

# cache = LRUCache(10)
# cache.put(10, 13)
# cache.put(3, 17)
# cache.put(6, 11)
# cache.put(10, 5)
# cache.put(9, 10)
# print(cache.get(13))
# cache.put(2, 19)
# print(cache.get(2))
# print(cache.get(3))
# cache.put(5, 25)
# print(cache.get(8))
# cache.put(9, 22)
# cache.put(5, 5)
# cache.put(1, 30)
# print(cache.get(11))
# cache.put(9, 12)
# print(cache.get(7))
# print(cache.get(5))
# print(cache.get(8))
# print(cache.get(9))
# cache.put(4, 30)
# cache.put(9, 3)
# print(cache.get(9))
# print(cache.get(10))
# print(cache.get(10))
# cache.put(6, 14)
# cache.put(3, 1)
# print(cache.get(3))
# cache.put(10, 11)
# print(cache.get(8))
# cache.put(2, 14)
# print(cache.get(1))
# print(cache.get(5))
# print(cache.get(4))
# cache.put(11, 4)
# cache.put(12, 24)
# cache.put(5, 18)
# print(cache.get(13))
# cache.put(7, 23)
# print(cache.get(8))
# print(cache.get(12))
# cache.put(3, 27)
# cache.put(2, 12)
# print(cache.get(5))
# cache.put(2, 9)
# cache.put(13, 4)
# cache.put(8, 18)
# cache.put(1, 7)
# print(cache.get(6))
# cache.put(9, 29)
# cache.put(8, 21)
# print(cache.get(5))
# cache.put(6, 30)
# cache.put(1, 12)
# print(cache.get(10))
# cache.put(4, 15)
# cache.put(7, 22)
# cache.put(11, 26)
# cache.put(8, 17)
# cache.put(9, 29)
# print(cache.get(5))
# cache.put(3, 4)
# cache.put(11, 30)
# print(cache.get(12))
# cache.put(4, 29)
# print(cache.get(3))
# print(cache.get(9))
# print(cache.get(6))
# cache.put(4, 4)
# print(cache.get(1))
# print(cache.get(10))
# cache.put(3, 29)
# cache.put(10, 28)
# cache.put(1, 20)
# cache.put(11, 13)
# print(cache.get(3))
# cache.put(3, 12)
# cache.put(3, 8)
# cache.put(10, 9)
# cache.put(3, 26)
# print(cache.get(8))
# print(cache.get(7))
# print(cache.get(5))
# cache.put(13, 17)
# cache.put(2, 27)
# cache.put(11, 15)
# print(cache.get(12))
# cache.put(9, 19)
# cache.put(2, 15)
# cache.put(3, 16)
# print(cache.get(1))
# cache.put(12, 17)
# cache.put(9, 1)
# cache.put(6, 19)
# print(cache.get(4))
# print(cache.get(5))
# print(cache.get(5))
# cache.put(8, 1)
# cache.put(11, 7)
# cache.put(5, 2)
# cache.put(9, 28)
# print(cache.get(1))
# cache.put(2, 2)
# cache.put(7, 4)
# cache.put(4, 22)
# cache.put(7, 24)
# cache.put(9, 26)
# cache.put(13, 28)
# cache.put(11, 26)
