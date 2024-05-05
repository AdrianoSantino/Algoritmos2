import pickle

from avltree import *


class LinkedList:
    root = None


class Node:
    key = None
    value = None
    next = None


def newNode(key, value):
    new = Node()
    new.key, new.value = key, value
    return new


if __name__ == "__main__":

    # L = LinkedList()
    # L.root = newNode(10, 20)
    # L.root.next = newNode(15, 50)

    A = AVLTree()
    for key in range(4):
        A.root = insert(A, random.randint(0, 50))
    A.root.display()

    with open('pickletesting.txt', 'bw') as f:
        pickle.dump(A, f)

    B = input('press sth:')

    with open('pickletesting.txt', 'br') as f:
        B = pickle.load(f)

    B.root.display()
