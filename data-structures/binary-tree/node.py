class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.leftPtr = None
        self.rightPtr = None

    def setData(self, new_data):
        self.data = new_data

    def getData(self):
        return self.data

    def setLeftPtr(self, new_ptr):
        self.leftPtr = new_ptr

    def getLeftPtr(self):
        return self.leftPtr

    def setRightPtr(self, new_ptr):
        self.rightPtr = new_ptr

    def getRightPtr(self):
        return self.rightPtr
