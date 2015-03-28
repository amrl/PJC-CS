from node import Node


class OrderedList:

    """A linked list with nodes ordered in non-decreasing order."""

    def __init__(self):
        self.head = None

    def add(self, new_data):
        """Add a new node to the list according to non-decreasing order."""
        new_node = Node(new_data)
        current = self.head

        if current is None or current.getData() > new_data:
            temp = self.head
            self.head = new_node
            new_node.setPtr(temp)
        else:
            while (current.getPtr() is not None
                   and current.getPtr().getData() < new_data):
                current = current.getPtr()

            temp = current.getPtr()
            current.setPtr(new_node)
            new_node.setPtr(temp)

    def pop(self):
        """Remove the node at the end of the list and return its data."""
        current = self.head
        prev = None

        while current.getPtr() is not None:
            prev = current
            current = current.getPtr()

        if prev is None:
            self.head = None
        else:
            prev.setPtr(None)

        return current.getData()

    def isEmpty(self):
        """Return True if the list is empty, False otherwise."""
        return self.head is None

    def size(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head

        while current is not None:
            current = current.getPtr()
            count += 1

        return count
