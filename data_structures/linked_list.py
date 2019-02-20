class LinkedList:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self):
        return f"{self.value} -> {self.next}"
