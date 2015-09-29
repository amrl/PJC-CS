# NOTE: This is a method for the BSTree class


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
