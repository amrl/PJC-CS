# NOTE: This is a method for the BTree class


def OutputData(self):
    print("Root: {0}".format(self.Root))
    print("NextFreePosition: {0}".format(self.NextFreePosition))
    print("-" * 65)
    print("{0:^10}|{1:^10}|{2:^20}|{3:^10}|{4:^10}".format(
        "Index", "LeftP", "Name", "Score", "RightP"))
    print("-" * 65)
    for index, node in enumerate(self.ThisTree[1:]):
        print("{0:^10}|{1:^10}|{2:^20}|{3:^10}|{4:^10}".format(
            index + 1, node.getLeftP(), node.getName(), node.getScore(),
            node.getRightP()))
