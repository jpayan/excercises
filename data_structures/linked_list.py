class LinkedList:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self):
        return f"{self.value} -> {self.next}"

    def __eq__(self, other):
        temp = self
        while temp is not None:
            if other is None or temp.value != other.value:
                return False
            temp = temp.next
            other = other.next
        return True
