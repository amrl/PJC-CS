# Binary Tree: 2013 H2 Computing P1 Q3


from node import Node


# dummy node in 1st node
ThisTree = [None] + [Node() for i in range(20)]
# link LeftP of nodes to next node's index
for index in range(1, 20):
    (ThisTree[index]).setLeftP(index+1)

# index of the root node
Root = 0

# index of a free node
NextFreePosition = 1


# Task 3.2
def AddItemToBinaryTree(NewTreeItem):
    global ThisTree, Root, NextFreePosition

    # check
    if NextFreePosition > 20:
        print("Error: No space available to add item.\n")
        return

    # set data to new node in the next free space (leaf)
    ThisTree[NextFreePosition].setData(NewTreeItem)
    ThisTree[NextFreePosition].setLeftP(0)
    ThisTree[NextFreePosition].setRightP(0)

    PreviousPosition = 2
    LastMove = 'X'

    if Root == 0:
        Root = NextFreePosition
    else:
        # traverse the tree to find the position for the new value
        CurrentPosition = Root

        while CurrentPosition != 0:
            PreviousPosition = CurrentPosition
            if NewTreeItem < ThisTree[CurrentPosition].getData():
                # move left
                LastMove = 'L'
                CurrentPosition = ThisTree[CurrentPosition].getLeftP()
            else:
                # move right
                LastMove = 'R'
                CurrentPosition = ThisTree[CurrentPosition].getRightP()

    # set the left/right pointer of a current leaf node to the new node
    if LastMove == 'R':
        ThisTree[PreviousPosition].setRightP(NextFreePosition)
    else:
        ThisTree[PreviousPosition].setLeftP(NextFreePosition)

    # move on to the next free node index in the list
    NextFreePosition += 1


# Task 3.3
def OutputData():
    global ThisTree, Root, NextFreePosition

    print("Root:", Root)
    print("NextFreePosition:", NextFreePosition)
    print()

    # Header
    print("{0:^10}{1:^10}{2:^10}{3:^10}"
          .format("Index", "LeftP", "Data", "RightP"))
    print('-'*40)

    for count, node in enumerate(ThisTree):
        if node is not None:
            print("{0:^10}{1:^10}{2:^10}{3:^10}"
                  .format(count, node.getLeftP(), node.getData(),
                          node.getRightP()))
    print()


# Task 3.4
def main():
    global ThisTree, Root, NextFreePosition

    while True:
        newData = input("Enter data to enter tree: ")
        if newData == "XXX":
            break
        else:
            AddItemToBinaryTree(newData)

    OutputData()


# Task 3.6
def inOrderTraversal(ThisTree, index=1):
    if index != 0:
        # Traverse the left subtree by recursively calling the in-order
        # function
        inOrderTraversal(ThisTree, ThisTree[index].getLeftP())

        # Display the data part of root element (or current element)
        print(ThisTree[index].getData())

        # Traverse the right subtree by recursively calling the in-order
        # function
        inOrderTraversal(ThisTree, ThisTree[index].getRightP())

main()
inOrderTraversal(ThisTree)
