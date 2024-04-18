from trie import *


def withPrefix(T: Trie, prefix: str, size: int):
    wordFound, lastLetterNode = searchNode(T, prefix)
    if not wordFound or size <= 0 or size <= len(prefix):
        return []

    def _withPrefix(node, size, finalList, remaining):
        if size == 0 and node.isEndOfWord:
            finalList.append(remaining + node.key)

        for child in node.children:
            _withPrefix(child, size - 1, finalList, remaining + node.key)
        return finalList

    remainingSize = size - len(prefix)
    return _withPrefix(lastLetterNode, remainingSize, [], prefix[:-1])


def test():
    T = Trie()
    for palabra in ["casa", "cosa", "coso", "cortina", "corazon", "corazones", "coraje", "coro", "cero", "cera"]:
        insert(T, palabra)
    print(withPrefix(T, "cor", 7))


test()
