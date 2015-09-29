from everything import BTree


def RankList(tree, root, stack):
    if root != 0:
        RankList(tree, tree[root].getRightP(), stack)
        stack.append((tree[root].getName(), tree[root].getScore()))
        RankList(tree, tree[root].getLeftP(), stack)

    while len(stack) > 0:
        name, score = stack.pop()
        print("{0}: {1}".format(name, score))


def main():
    tree = BTree()

    infile = open("SCORES.txt", "r")
    for line in infile:
        name, score = line[:-1].split('|')
        tree.AddNodeToBinaryTree(name, score)
    infile.close()

    RankList(tree.ThisTree, tree.Root, list())

# main()
