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
