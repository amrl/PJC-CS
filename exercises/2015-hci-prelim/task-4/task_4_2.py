# NOTE: This is a method for the BTree class


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
                CurrentPosition = self.ThisTree[CurrentPosition].getRightP()

    if LastMove == 'R':
        self.ThisTree[PreviousPosition].setRightP(self.NextFreePosition)
    elif LastMove == 'L':
        self.ThisTree[PreviousPosition].setLeftP(self.NextFreePosition)

    self.NextFreePosition = temp
