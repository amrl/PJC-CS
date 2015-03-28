from node import Node


class BinaryTree:

    """
    An ordered binary tree (BST) with smaller items on the left of the root
    and larger items on the right.
    """

    def __init__(self):
        self.root = None

    def add(self, new_data):
        """Add a new node to the tree (according to BST)."""
        new_node = Node(new_data)
        current = self.root

        if current is None:
            self.root = new_node
        else:
            while current is not None:
                prev = current
                if new_data < current.getData():
                    current = current.getLeftPtr()
                    LastMove = 'L'
                else:
                    current = current.getRightPtr()
                    LastMove = 'R'

            if LastMove == 'L':
                prev.setLeftPtr(new_node)
            else:
                prev.setRightPtr(new_node)

    def lookup(self, target):
        """Return True if target exists in the tree, False otherwise."""
        current = self.root

        while current is not None:
            if current.getData() == target:
                return True
            elif current.getData() > target:
                current = current.getLeftPtr()
            else:
                current = current.getRightPtr()

        return False

    def isEmpty(self):
        """Return True if the tree is empty, False otherwise."""
        return self.root is None

    def inOrder(self, pointer, outlist):
        """Traverse the tree in inorder. Used for the print method."""
        if pointer is not None:
            self.inOrder(pointer.getLeftPtr(), outlist)
            outlist.append(pointer.getData())
            self.inOrder(pointer.getRightPtr(), outlist)

            return outlist

    def __str__(self):
        """Display the tree contents according to inorder traversal."""
        return ', '.join(str(data) for data in self.inOrder(self.root, []))
