class Stack:

    def __init__(self, lim):
        self.Limit = lim
        self.Data = []  # max size => self.Limit

    def IsEmpty(self):
        return len(self.Data) == 0

    def IsFull(self):
        return len(self.Data) == self.Limit

    def Push(self, new_data):
        self.Data.append(new_data)

    def Pop(self):
        return self.Data.pop()

    def Peek(self):
        return self.Data[-1]

    def Size(self):
        return len(self.Data)

    def Display(self):
        for data in self.Data:
            print(data)
        print("TOP OF STACK")
