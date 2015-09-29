# NOTE: This is a method for the BSTree class


def display_loan_electronic(self, root):
    if root is not None:
        self.display_loan_electronic(root.getLeftP())
        if root.Data[1] == 'E' and root.Data[3] == 'U':
            print("{0}. {1}".format(root.Data[0], root.Data[2]))
        self.display_loan_electronic(root.getRightP())
