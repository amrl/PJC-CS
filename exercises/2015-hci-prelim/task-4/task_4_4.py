from everything import BTree


def main():
    tree = BTree()

    infile = open("SCORES.txt", "r")
    for line in infile:
        name, score = line[:-1].split('|')
        tree.AddNodeToBinaryTree(name, score)
    infile.close()

    tree.OutputData()


# main()
