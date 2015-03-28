class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.ptr = None

    def setData(self, new_data):
        self.data = new_data

    def getData(self):
        return self.data

    def setPtr(self, new_ptr):
        self.ptr = new_ptr

    def getPtr(self):
        return self.ptr
