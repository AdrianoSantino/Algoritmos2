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


def isLetterOnChildren(node, char) -> [bool, TrieNode | None]:
    """Given a letter, returns (True and node) oth (False, None)"""
    for n in node.children:
        if n.key == char:
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
    """Given a word, returns (True and LastLetterNode) oth (False, None)"""
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
    if len(lastLetterNode.children) > 0:  # is inner, job done
        return True

    node = lastLetterNode
    while True:
        if node is None or node.isEndOfWord:
            return True
        nodeParent = node.parent
        nodeParent.children.remove(node)
        if len(nodeParent.children) > 0:
            return True
        node = nodeParent


def autoCompletar(T, prefijo):
    """Devuelve la parte restante de una raíz de 2 o + palabras que tengan a -prefijo- como parte de su raíz."""
    cadenaEncontrada, nodoUltimaLetra = searchWordLastLetterNode(T, prefijo)
    if not cadenaEncontrada:
        return ''
    resto = ''
    while True:
        if len(nodoUltimaLetra.children) != 1:
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
    delete(T, "mamá")
    print(autoCompletar(T, "ma"))
