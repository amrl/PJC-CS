class TreeNode:

    def __init__(self, pid):
        self.Lptr = None
        self.productid = pid
        self.Rptr = None
        self.orders = LinkedList()


class ListNode:

    def __init__(self, oid):
        self.next = None  # pointer
        self.orderid = oid


class LinkedList:

    def __init__(self):
        self.Head = None

    def add(self, oid):
        """Add a new orderid to the front."""
        new_node = ListNode(oid)
        temp = self.Head
        self.Head = new_node
        new_node.next = temp

    def size(self):
        """Return number of orderid."""
        count = 0
        current = self.Head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        """Display all orderid found."""
        output = list()
        current = self.Head
        while current is not None:
            output.append(current.orderid)
            current = current.next
        return ', '.join(output)


class BSTree:

    def __init__(self):
        self.Root = None

    def insert(self, pid, oid):
        """Add a productid to tree. If it already exists, just add the orderid
        to the LinkedList linked to that productid.
        """
        new_node = TreeNode(pid)
        new_node.orders.add(oid)  # orders is a LinkedList

        if self.Root is None:
            self.Root = new_node
        else:
            current = self.Root
            while current is not None:
                prev = current
                if pid == current.productid:  # product already exists in tree
                    current.orders.add(oid)
                    return
                elif pid < current.productid:
                    current = current.Lptr
                    LastMove = 'L'
                else:
                    current = current.Rptr
                    LastMove = 'R'

            if LastMove == 'L':
                prev.Lptr = new_node
            else:
                prev.Rptr = new_node

    def search(self, pid):
        current = self.Root
        while current is not None:
            if pid == current.productid:
                return True
            elif pid < current.productid:
                current = current.Lptr
            else:
                current = current.Rptr
        return False

    def inorder_func(self, root):
        if root is not None:
            self.inorder_func(root.Lptr)
            print("{0}:".format(root.productid), end=" ")
            print(root.orders)
            self.inorder_func(root.Rptr)

    def inorder(self):
        self.inorder_func(self.Root)

    def most_popular(self):
        pass

    def delete(self):
        pass


# tree = BSTree()
# tree.insert("B", "9")
# tree.insert("A", "9")
# tree.insert("F", "9")
# tree.insert("G", "1")
# tree.insert("C", "8")
# tree.insert("B", "2")
# tree.insert("A", "1")
# tree.insert("F", "2")
# tree.insert("E", "1")
# tree.insert("A", "7")
# tree.insert("G", "3")
# tree.insert("B", "7")
# tree.insert("E", "9")
# tree.insert("C", "4")
# tree.insert("H", "5")
# tree.insert("C", "3")
# tree.insert("D", "3")
# tree.inorder()
