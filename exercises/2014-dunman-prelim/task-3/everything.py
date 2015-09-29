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

    def search(self):
        item_id = input("Enter item id: ")

        current = self.Root
        while current is not None:
            if current.Data[0] == item_id:
                book_type, title = current.Data[1], current.Data[2]
                if book_type == 'B':
                    book_type = "Book"
                else:
                    book_type = "Electronic"
                if current.Data[3] == 'A':
                    print("Available: {0} [{1}]".format(title, book_type))
                else:
                    print("Unvailable: {0} [{1}]".format(title, book_type))
                return
            else:
                if item_id < current.Data[0]:
                    current = current.getLeftP()
                else:
                    current = current.getRightP()

        print("ID not found.")

    def display_loan_electronic_func(self, root):
        if root is not None:
            self.display_loan_electronic_func(root.getLeftP())
            if root.Data[1] == 'E' and root.Data[3] == 'U':
                print("{0}. {1}".format(root.Data[0], root.Data[2]))
            self.display_loan_electronic_func(root.getRightP())

    def display_loan_electronic(self):
        self.display_loan_electronic_func(self.Root)
