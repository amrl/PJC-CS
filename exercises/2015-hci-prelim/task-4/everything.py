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

    def AddNodeToBinaryTree(self, NewName, NewScore):
        if self.NextFreePosition == 0:
            print("No more free nodes available!")
            return

        temp = self.ThisTree[self.NextFreePosition].getLeftP()
        self.ThisTree[self.NextFreePosition].setLeftP(0)
        self.ThisTree[self.NextFreePosition].setName(NewName)
        self.ThisTree[self.NextFreePosition].setScore(NewScore)
        self.ThisTree[self.NextFreePosition].setRightP(0)
        LastMove = 'X'

        if self.Root == 0:
            self.Root = self.NextFreePosition
        else:
            # traverse the tree to find the position for the new value
            CurrentPosition = self.Root
            while CurrentPosition != 0:
                PreviousPosition = CurrentPosition
                if NewScore < self.ThisTree[CurrentPosition].getScore():
                    # move left
                    LastMove = 'L'
                    CurrentPosition = self.ThisTree[CurrentPosition].getLeftP()
                else:
                    # move right
                    LastMove = 'R'
                    CurrentPosition = self.ThisTree[
                        CurrentPosition].getRightP()

        if LastMove == 'R':
            self.ThisTree[PreviousPosition].setRightP(self.NextFreePosition)
        elif LastMove == 'L':
            self.ThisTree[PreviousPosition].setLeftP(self.NextFreePosition)

        self.NextFreePosition = temp

    def OutputData(self):
        print("Root: {0}".format(self.Root))
        print("NextFreePosition: {0}".format(self.NextFreePosition))
        print("-" * 65)
        print("{0:^10}|{1:^10}|{2:^20}|{3:^10}|{4:^10}".format(
            "Index", "LeftP", "Name", "Score", "RightP"))
        print("-" * 65)
        for index, node in enumerate(self.ThisTree[1:]):
            print("{0:^10}|{1:^10}|{2:^20}|{3:^10}|{4:^10}".format(
                index + 1, node.getLeftP(), node.getName(), node.getScore(),
                node.getRightP()))
