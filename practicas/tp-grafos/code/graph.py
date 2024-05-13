from dictionary import hashf, create


class Node:
    key, next, color = None, None, "WHITE"

    def __repr__(self):
        return self.key


def createNode(key):
    new = Node()
    new.key = key
    return new


def appNode(root, key):
    if not root:
        return createNode(key)
    node = root
    while node.next:
        node = node.next
    node.next = createNode(key)
    return root


def createGraph(V, E):
    """O(V + E)"""
    G = create(len(V))
    for v in V:
        index = hashf(v, len(V))
        G[index] = createNode(v)

    for a, b in E:
        index = hashf(a, len(V))
        appNode(G[index], b)
        index = hashf(b, len(V))
        appNode(G[index], a)
    return G


def printGraph(G):
    for v in G:
        printList(v)
    print()


def printList(root):
    node = root
    while node:
        print(node.key, end=' ')
        node = node.next
    print()


def startNode(G, letter):
    index = hashf(letter, len(G))
    return G[index]


if __name__ == "__main__":
    V = ['u', 'a', 'w']
    E = [('u', 'a'), ('w', 'a')]
    G = createGraph(V, E)
    printGraph(G)
