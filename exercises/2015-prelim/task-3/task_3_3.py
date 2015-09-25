# NOTE: this is a method in the LinkedList class


def Update(self, new_value):
    if self.NextFree == -1:  # check if free node exists
        print("No space to insert")
        return

    # set empty node at NextFree to be the new node
    self.Node[self.NextFree].setWord(new_value)  # insert word into node
    self.Node[self.NextFree].setCount(1)  # initialise count to 1

    if self.Start == -1:  # insert into empty list
        holdfree = self.Node[self.NextFree].getPointer()
        self.Node[self.NextFree].setPointer(-1)
        self.Start = self.NextFree
        self.NextFree = holdfree
    else:
        # insert as first node of list
        if new_value < self.Node[self.Start].getWord():
            holdfree = self.Node[self.NextFree].getPointer()
            self.Node[self.NextFree].setPointer(self.Start)
            self.Start = self.NextFree
            self.NextFree = holdfree
        else:
            previous = self.Start
            current = self.Start
            # search position to insert node
            while (new_value > self.Node[current].getWord()
                   and self.Node[current].getPointer() != -1):
                previous = current
                current = self.Node[current].getPointer()

            # word exists, just increment count
            if new_value == self.Node[current].getWord():
                self.Node[current].setCount(self.Node[current].getCount() + 1)
                # revert changes made to node at NextFree
                self.Node[self.NextFree].setWord("")
                self.Node[self.NextFree].setCount(0)

            # insert as last node of list
            elif (new_value > self.Node[current].getWord()
                  and self.Node[current].getPointer() == -1):
                holdfree = self.Node[self.NextFree].getPointer()
                self.Node[current].setPointer(self.NextFree)
                self.Node[self.NextFree].setPointer(-1)
                self.NextFree = holdfree

            # insert in-between nodes
            else:
                holdfree = self.Node[self.NextFree].getPointer()
                self.Node[previous].setPointer(self.NextFree)
                self.Node[self.NextFree].setPointer(current)
                self.NextFree = holdfree
