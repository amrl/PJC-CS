class Node:

    def __init__(self, data=None):
        self.pointer = None
        self.data = data

    def getPointer(self):
        return self.pointer

    def setPointer(self, ptr):
        self.pointer = ptr

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata


class Stack:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.getPointer() is not None:
                current = current.getPointer()
            current.setPointer(Node(data))

    def peek(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current.getPointer() is not None:
                current = current.getPointer()
            return current.getData()

    def pop(self):
        if self.head is None:
            return
        else:
            current = self.head
            prev = None
            while current.getPointer() is not None:
                prev = current
                current = current.getPointer()

            if prev is None:
                data = current.getData()
                self.head = None
                return data
            else:
                prev.setPointer(None)
                return current.getData()
