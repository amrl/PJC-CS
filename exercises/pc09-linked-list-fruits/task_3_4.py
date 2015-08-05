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


def IsFull(self):
    return self.NextFree == 0
