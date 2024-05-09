from dictionary import hashf, create


def createGraph(V, E):
    """O(V + E)"""
    G = create(len(V))
    for v in V:
        index = hashf(v, len(V))
        G[index] = [v]

    for a, b in E:
        index = hashf(a, len(V))
        G[index].append(b)
    return G


def printGraph(G):
    for v in G:
        print(v)
    print()


if __name__ == "__main__":
    V = ['u', 'a', 'w']
    E = [('u', 'a'), ('w', 'a')]
    G = createGraph(V, E)
    printGraph(G)
    pass
