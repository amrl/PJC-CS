class ListNode:

    def __init__(self, data="empty string", ptr=0):
        self.DataValue = data  # string
        self.PointerValue = ptr  # integer

    def get_data(self):
        return self.DataValue

    def set_data(self, new_data):
        self.DataValue = new_data

    def get_ptr(self):
        return self.PointerValue

    def set_ptr(self, new_ptr):
        self.PointerValue = new_ptr


class LinkedList:

    def Initialise(self):
        # dummy node at index 0
        self.Node = [None] + [ListNode() for _ in range(30)]
        # set pointer of each ListNode to next index
        for index in range(1, 30):
            self.Node[index].set_ptr(index+1)

        self.Start = 0
        self.NextFree = 1

    # this method is from task 3.4
    def AddNode(self, NewItem):
        self.Node[self.NextFree].DataValue = NewItem

        if self.Start == 0:
            self.Start = self.NextFree
            Temp = self.Node[self.NextFree].get_ptr()
            self.Node[self.NextFree].set_ptr(0)
            self.NextFree = Temp
        else:
            # traverse the list – starting at Start to find
            # the position at which to insert the new item
            Temp = self.Node[self.NextFree].get_ptr()

            if NewItem < self.Node[self.Start].get_data():
                # new item will become the start of the list
                self.Node[self.NextFree].set_ptr(self.Start)
                self.Start = self.NextFree
                self.NextFree = Temp
            else:
                # the new item is not at the start of the list . . .
                Previous = 0
                Current = self.Start
                Found = False

                while not Found and Current != 0:
                    if NewItem <= self.Node[Current].get_data():
                        self.Node[Previous].set_ptr(self.NextFree)
                        self.Node[self.NextFree].set_ptr(Current)
                        self.NextFree = Temp
                        Found = True
                    else:
                        # move on to the next node
                        Previous = Current
                        Current = self.Node[Current].get_ptr()

                if Current == 0:
                    self.Node[Previous].PointerValue = self.NextFree
                    self.Node[self.NextFree].PointerValue = 0
                    self.NextFree = Temp

    # this procedure is from task 3.5
    def TraversalInOrder(self, Index):
        if Index != 0:
            print(self.Node[Index].get_data())
            # follow the pointer to the next data item in the linked list
            self.TraversalInOrder(self.Node[Index].get_ptr())

    # this method is from task 3.5
    def Traversal(self):
        self.TraversalInOrder(self.Start)

    # this procedure is from task 3.7
    def TraversalInReverseOrder(self, Index, stack=[]):
        if Index != 0:
            stack.append(self.Node[Index].get_data())
            self.TraversalInReverseOrder(self.Node[Index].get_ptr(), stack)
        else:
            while len(stack) != 0:
                print(stack.pop())

    # this method is from task 3.7
    def ReverseTraversal(self):
        self.TraversalInReverseOrder(self.Start)

    def DisplayLinkedList(self):
        # header
        print("{0:^10}|{1:^20}|{2:^10}".format("Index", "Data", "Pointer"))
        print("-"*42)
        # display each ListNode data
        for index, listnode in enumerate(self.Node[1:]):
            print("{0:^10}|{1:^20}|{2:^10}"
                  .format(index+1, listnode.get_data(), listnode.get_ptr()))

    def IsEmpty(self):
        return self.Start == 0

    # this method is from task 3.4
    def IsFull(self):
        return self.NextFree == 0
