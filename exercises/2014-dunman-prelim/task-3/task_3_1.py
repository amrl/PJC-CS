class Node:

    def __init__(self, Item_ID, Type, Title, Status):
        self.LeftP = None
        self.Data = [int(Item_ID), Type, Title, Status]
        self.RightP = None

    def getLeftP(self):
        return self.LeftP

    def setLeftP(self, new_ptr):
        self.LeftP = new_ptr

    def getRightP(self):
        return self.RightP

    def setRightP(self, new_ptr):
        self.RightP = new_ptr


class BSTree:

    def __init__(self):
        self.Root = None

    def insert(self, Item_ID, Type, Title, Status):
        new_node = Node(Item_ID, Type, Title, Status)

        if self.Root is None:
            self.Root = new_node
        else:
            current = self.Root
            while current is not None:
                prev = current
                if int(Item_ID) < current.Data[0]:
                    current = current.getLeftP()
                    LastMove = 'L'
                else:
                    current = current.getRightP()
                    LastMove = 'R'

            if LastMove == 'L':
                prev.setLeftP(new_node)
            else:
                prev.setRightP(new_node)


# tree = BSTree()
# infile = open("ITEMS.dat", "r")
# for line in infile:
#     Item_ID, Type, Title, Status = line[:-1].split(',')
#     tree.insert(Item_ID, Type, Title, Status)
# infile.close()
