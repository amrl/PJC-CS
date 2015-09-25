# Merged all the Tasks together


class ListNode:

    def __init__(self):
        self.Word = ""
        self.Count = 0
        self.Pointer = -1

    def getWord(self):
        return self.Word

    def setWord(self, new_word):
        self.Word = new_word

    def getCount(self):
        return self.Count

    def setCount(self, new_count):
        self.Count = new_count

    def getPointer(self):
        return self.Pointer

    def setPointer(self, new_ptr):
        self.Pointer = new_ptr


class LinkedList:

    def Initialise(self):
        self.Node = [ListNode() for _ in range(30)]
        # link nodes to next index
        for index, listnode in enumerate(self.Node[:-1]):
            listnode.setPointer(index+1)
        self.Start = -1  # NULL is -1
        self.NextFree = 0

    def Display(self):
        # headers
        print('-'*40)
        print("{0:^5}|{1:^15}|{2:^5}|{3:^10}"
              .format("Index", "Word", "Count", "Pointer"))
        print('-'*40)

        for index, listnode in enumerate(self.Node):
            print("{0:^5}|{1:^15}|{2:^5}|{3:^10}"
                  .format(index,
                          listnode.getWord(),
                          listnode.getCount(),
                          listnode.getPointer()))

    def IsEmpty(self):
        return self.Start == -1

    def IsFull(self):
        return self.Next == -1

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
                    self.Node[current].setCount(
                                       self.Node[current].getCount() + 1)
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

    def Query(self):
        user_word = input("Enter a word: ")

        found = False
        for listnode in self.Node:
            if user_word == listnode.getWord():
                found = True
                occurrences = listnode.getCount()
                print("Number of occurences:", occurrences)

        if not found:
            print("Word not found.")


# Task 3.2
test = LinkedList()
test.Initialise()
test.Display()


# Task 3.4
infile = open("Story.txt", "r")
words = infile.read().split()
for word in words:
    test.Update(word)
infile.close()
test.Display()
