class Node:

    def __init__(self):
        self.LeftP = 0
        self.Name = ""
        self.Score = 0
        self.RightP = 0

    def getLeftP(self):
        return self.LeftP

    def setLeftP(self, new_ptr):
        self.LeftP = new_ptr

    def getName(self):
        return self.Name

    def setName(self, new_name):
        self.Name = new_name

    def getScore(self):
        return self.Score

    def setScore(self, new_score):
        self.Score = new_score

    def getRightP(self):
        return self.RightP

    def setRightP(self, new_ptr):
        self.RightP = new_ptr


class BTree:

    def __init__(self):
        self.ThisTree = [None] + [Node() for _ in range(20)]
        for index, node in enumerate(self.ThisTree[1:-1]):
            self.ThisTree[index + 1].setLeftP(index + 2)
        self.Root = 0
        self.NextFreePosition = 1


# tree = BTree()
