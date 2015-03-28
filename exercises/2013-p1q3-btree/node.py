class Node:

    def __init__(self):
        self.LeftP = 0
        self.Data = ""
        self.RightP = 0

    def getLeftP(self):
        return self.LeftP

    def setLeftP(self, ptr):
        self.LeftP = int(ptr)

    def getData(self):
        return self.Data

    def setData(self, data):
        self.Data = str(data)

    def getRightP(self):
        return self.RightP

    def setRightP(self, ptr):
        self.RightP = int(ptr)
