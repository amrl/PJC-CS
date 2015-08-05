def TraversalInReverseOrder(self, Index, stack=[]):
    if Index != 0:
        stack.append(self.Node[Index].get_data())
        self.TraversalInReverseOrder(self.Node[Index].get_ptr(), stack)
    else:
        while len(stack) != 0:
            print(stack.pop())


def ReverseTraversal(self):
    self.TraversalInReverseOrder(self.Start)
