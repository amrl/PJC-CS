from node import Node


class Stack:

    def __init__(self):
        self.top = None

    def push(self, new_data):
        """Add a new node to the top of the stack."""
        temp = self.top
        self.top = Node(new_data)
        self.top.setPtr(temp)

    def pop(self):
        """Remove the node at the top of the stack and return its data."""
        temp = self.top
        self.top = self.top.getPtr()
        return temp.getData()

    def peek(self):
        """Return the data of the node at the top of the stack."""
        return self.top.getData()

    def isEmpty(self):
        """Return True if the stack is empty, False otherwise."""
        return self.top is None

    def size(self):
        """Return the number of nodes in the stack."""
        count = 0
        current = self.top

        while current is not None:
            current = current.getPtr()
            count += 1

        return count
