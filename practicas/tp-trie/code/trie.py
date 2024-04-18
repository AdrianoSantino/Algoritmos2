class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


def newNode(key):
    new = TrieNode()
    new.children = []
    new.key = key
    return new


def isLetterOnChildren(node, letter):
    for n in node.children:
        if n.key == letter:
            return True, n
    return False, None


def insert(T, element):
    def insertR(node, word, wordSize, index):

        if index == wordSize:
            node.isEndOfWord = True
            return

        letter = word[index]
        letterFound, new = isLetterOnChildren(node, letter)
        if not letterFound:
            new = newNode(letter)
            node.children.append(new)
        new.parent = node
        insertR(new, word, wordSize, index + 1)

    if T is None:
        T = Trie()
    if T.root is None:
        T.root = newNode(None)
    insertR(T.root, element, len(element), 0)
    return


def searchNode(T, element):
    def searchNodeR(node, word, wordSize, index):

        if index == wordSize:
            return True, node

        letter = word[index]
        letterFound, new = isLetterOnChildren(node, letter)
        if not letterFound:
            return False, node
        else:
            return searchNodeR(new, word, wordSize, index + 1)

    if T is None or T.root is None:
        raise Warning("Empty Trie or root")
    return searchNodeR(T.root, element, len(element), 0)


def search(T, element):
    return searchNode(T, element)[0]


def delete(T, element):
    wordFound, lastLetterNode = searchNode(T, element)
    if not wordFound:
        return False

    lastLetterNode.isEndOfWord = False

    # A word can be a leaf nor an inner node
    if lastLetterNode.children is []:  # is inner, job done
        return False

    node = lastLetterNode  # is leaf
    while True:
        if node is None or node.isEndOfWord:  # reached the root or a new word ending
            return True
        nodeParent = node.parent
        nodeParent.children.remove(node)
        node = nodeParent
