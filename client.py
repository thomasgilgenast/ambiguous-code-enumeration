import sys


from tree import Tree


if __name__ == '__main__':
    try:
        int(sys.argv[1])
        t = Tree(sys.argv[1])
    except ValueError:
        t = Tree.from_letters(sys.argv[1])
    t.explore()
    print t
