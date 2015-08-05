def TraversalInOrder(self, Index):
    if Index != 0:
        print(self.Node[Index].get_data())
        # follow the pointer to the next data item in the linked list
        self.TraversalInOrder(self.Node[Index].get_ptr())


def Traversal(self):
    self.TraversalInOrder(self.Start)
