from node import Node


class Queue:

    def __init__(self):
        self.front = None

    def enqueue(self, new_data):
        """Add a new node to the rear of the queue."""
        new_node = Node(new_data)
        current = self.front

        if current is None:
            self.front = new_node
        else:
            while current.getPtr() is not None:
                current = current.getPtr()

            current.setPtr(new_node)

    def dequeue(self):
        """Remove the node at the front of the queue and return its data."""
        temp = self.front
        self.front = self.front.getPtr()
        return temp.getData()

    def isEmpty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.front is None

    def size(self):
        """Return the number of nodes in the queue."""
        count = 0
        current = self.front

        while current is not None:
            current = current.getPtr()
            count += 1

        return count
