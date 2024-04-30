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


def isLetterOnChildren(node: TrieNode, letter: str) -> [bool, TrieNode | None]:
    """Returns a tuple: bool is found and the node itself (None if not found)."""
    for n in node.children:
        if n.key == letter:
            return True, n
    return False, None


def insert(T, element):
    if T.root is None:
        T.root = newNode(None)
    node = T.root
    for letter in element:
        letterFound, new = isLetterOnChildren(node, letter)
        if not letterFound:
            new = newNode(letter)
            node.children.append(new)
        new.parent = node
        node = new
    node.isEndOfWord = True
    return


def searchWordLastLetterNode(T, element) -> [bool, TrieNode | None]:
    """Given a word, returns True if it is on the Trie and the last letter node, otw False and None"""
    if T is None or T.root is None or not element:
        raise Warning("Empty Trie, root or word")
    node = T.root
    for letter in element:
        letterFound, node = isLetterOnChildren(node, letter)
        if not letterFound:
            return False, None
    return True, node


def search(T, element):
    return searchWordLastLetterNode(T, element)[0]


def delete(T, element):
    wordFound, lastLetterNode = searchWordLastLetterNode(T, element)
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


def autoCompletar(T, prefijo):
    """Devuelve la parte restante de una raíz de 2 o + palabras que tengan a -prefijo- como parte de su raíz."""
    cadenaEncontrada, nodoUltimaLetra = searchWordLastLetterNode(T, prefijo)
    if not cadenaEncontrada:
        return ''
    resto = ''
    while True:
        if len(nodoUltimaLetra.children) > 1:
            return "''" if not resto else resto
        nodoSigue = nodoUltimaLetra.children[0]
        resto += nodoSigue.key
        nodoUltimaLetra = nodoSigue


if __name__ == "__main__":
    T = Trie()
    for pal in ["Groenlandés", "Groenlandia", "madera", "mamá"]:
        insert(T, pal)
    print(autoCompletar(T, "Groen"))
    print(autoCompletar(T, "ma"))
