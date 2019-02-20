class Node:
    def __init__(self, key, distance):
        self.key = key
        self.distance = distance
        self.previous = None


class MinHeap:
    def __init__(self):
        self._size = 0
        self._heap = []
        self._positions = {}

    def add(self, item):
        self._heap.append(item)
        self._size += 1
        self._positions[item.key] = self._size - 1
        self._heapify_up()
    
    def poll(self):
        if self._size == 0:
            raise Exception("Heap is empty.")
        item = self._heap[0]
        self._heap[0] = self._heap[-1]
        del self._heap[-1]
        self._size -= 1
        if self._size:
            self._positions[self._heap[0].key] = 0
        del self._positions[item.key]
        self._heapify_down()
        return item

    def peek(self):
        if self._size == 0:
            raise Exception("Heap is empty.")
        return self._heap[0]

    def get(self, key):
        return self._heap[self._positions[key]]

    def update(self, key, distance, previous):
        index = self._positions[key]
        item = self._heap[index]
        item.distance = distance
        item.previous = previous
        self._swap(index, self._size - 1)
        self._heapify_up()

    def is_empty(self):
        return self._size == 0

    def _swap(self, index_a, index_b):
        self._positions[self._heap[index_a].key] = index_b
        self._positions[self._heap[index_b].key] = index_a
        self._heap[index_a], self._heap[index_b] = self._heap[index_b], self._heap[index_a]

    def _heapify_up(self):
        index = self._size - 1
        while self._has_parent(index) and self._get_parent(index).distance > self._heap[index].distance:
            parent_index = self.__get_parent_index(index)
            self._swap(parent_index, index)
            index = parent_index

    def _heapify_down(self):
        index = 0
        while self._has_left_child(index):
            smaller_child_index = self._get_smaller_child_index(index)
            if self._heap[index].distance < self._heap[smaller_child_index].distance:
                break
            else:
                self._swap(index, smaller_child_index)
            index = smaller_child_index

    @classmethod
    def __get_left_child_index(cls, parent_index):
        return 2 * parent_index + 1
    
    @classmethod
    def __get_right_child_index(cls, parent_index):
        return 2 * parent_index + 2
    
    @classmethod
    def __get_parent_index(cls, child_index):
        return (child_index - 1) // 2

    def _has_left_child(self, parent_index):
        return self.__get_left_child_index(parent_index) < self._size
    
    def _has_right_child(self, parent_index):
        return self.__get_right_child_index(parent_index) < self._size

    def _has_parent(self, child_index):
        return self.__get_parent_index(child_index) >= 0

    def _get_left_child(self, parent_index):
        return self._heap[self.__get_left_child_index(parent_index)]

    def _get_right_child(self, parent_index):
        return self._heap[self.__get_right_child_index(parent_index)]

    def _get_parent(self, child_index):
        return self._heap[self.__get_parent_index(child_index)]
    
    def _get_smaller_child_index(self, parent_index):
        smaller_child_index = self.__get_left_child_index(parent_index)
        if self._has_right_child(parent_index) and self._get_right_child(parent_index).distance < self._get_left_child(parent_index).distance:
            smaller_child_index = self.__get_right_child_index(parent_index)
        return smaller_child_index

    def __repr__(self):
        return str([node.distance for node in self._heap])
