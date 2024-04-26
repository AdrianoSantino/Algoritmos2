import string


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# noinspection PyTypeChecker
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def insert_count(self, key):
        index = ord(key.lower()) % self.capacity

        if self.table[index] is None:
            self.table[index] = 1
        else:
            self.table[index] += 1
        self.size += 1

    def search_count(self, key):
        index = ord(key.lower()) % self.capacity
        return self.table[index]

    def __len__(self):
        return self.size

    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False


def efficient_len_comparison(string1, string2):
    """O(n). Compara el len de dos strings de manera eficiente, sin tener que usar el len dos veces"""
    len1 = len(string1)  # toma arbitrariamente un string de referencia
    try:
        if string2[len1 - 1]:  # si el otro string tiene algo en esa última posición, sigue
            try:
                if string2[len1]:  # si excede en tamaño, devuelve Falso
                    return False
            except:
                return True  # si no, Verdadero
    except:
        return False


def is_permutation(string1, string2) -> bool:
    """Peor caso: O(4n) >> O(n)
    Mejor caso O(n)
    Siendo n y m las longitudes de las cadenas s1 y s2, respectivamente."""
    dicc1 = HashTable(len(string.ascii_lowercase))
    dicc2 = HashTable(len(string.ascii_lowercase))

    if not efficient_len_comparison(string1, string2):  # O(n)
        return False  # retorna si son diferentes
    # continúa si tienen el mismo tamaño, digamos, n
    # edit: el len en Python es de O(1), ¡acabo de enterarme!

    # el diccionario utilizado no influye en tiempo (ideal), ya que a priori se conocía el universo dominio
    for letter1 in string1:  # se insertan todas las keys en un diccionario O(n)
        dicc1.insert_count(letter1)
    for letter2 in string2:  # se insertan todas las keys en otro diccionario O(n)
        dicc2.insert_count(letter2)

    for letter1 in string1:
        if dicc1.search_count(letter1) != dicc2.search_count(letter1):  # both dicc counts should be the same
            return False
    return True


# Driver code
if __name__ == '__main__':
    print(is_permutation("hola", "ahol"))
    print(is_permutation("hola", "ahodl"))
    # # Create a hash table with
    # # a capacity of 5
    # ht = HashTable(5)
    #
    # # Add some key-value pairs
    # # to the hash table
    # ht.insert("apple", 3)
    # ht.insert("banana", 2)
    # ht.insert("cherry", 5)
    # print(str(ht))
    #
    # # Check if the hash table
    # # contains a key
    # print("apple" in ht)  # True
    # print("durian" in ht)  # False
    #
    # # Get the value for a key
    # print(ht.search("banana"))  # 2
    #
    # # Update the value for a key
    # ht.insert("banana", 4)
    # print(ht.search("banana"))  # 4
    #
    # ht.remove("apple")
    # ht.remove("cherry")
    # # Check the size of the hash table
    # print(str(ht))
    # print(len(ht))  # 1
