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


def search(T, element):
    def searchR(node, word, wordSize, index):
        if index == wordSize:
            return True

        letter = word[index]
        letterFound, new = isLetterOnChildren(node, letter)
        return False if not letterFound else searchR(new, word, wordSize, index + 1)

    if T is None or T.root is None:
        raise Warning("Empty Trie or root")
    return searchR(T.root, element, len(element), 0)
