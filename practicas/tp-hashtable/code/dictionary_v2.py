import random
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

    # puede usarse solamente key % m o bien ord(key) % m, según sean caracteres numéricos o alfanuméricos

    """Ejercicio 2"""

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

    def boolean_search(self, key, value):
        """O(n): where n is the slot-chained-linked-list length.
        Returns True if (key, value) exists, oth. False"""
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

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


"""Ejercicio 4"""


def is_permutation(string1, string2) -> bool:
    """Peor caso: O(3n) >> O(n) --- Mejor caso: O(1)
    Siendo n y m las longitudes de las cadenas s1 y s2, respectivamente."""
    dicc1 = HashTable(len(string.ascii_lowercase))
    dicc2 = HashTable(len(string.ascii_lowercase))

    if len(string1) != len(string2):  # len is 0(1)
        return False

    # el diccionario utilizado no influye en tiempo (es uno ideal), ya que a priori se conocía el universo dominio
    for letter1 in string1:  # se insertan todas las keys en un diccionario O(n)
        dicc1.insert_count(letter1)
    for letter2 in string2:  # se insertan todas las keys en otro diccionario O(n)
        dicc2.insert_count(letter2)

    for letter1 in string1:  # O(n)
        if dicc1.search_count(letter1) != dicc2.search_count(letter1):  # both dicc counts should be the same
            return False
    return True


"""Ejercicio 5
El ejercicio está prácticamente resuelto mediante las operaciones que se han implementado en este módulo. 
La función insert utiliza el método de encadenamiento, por lo tanto, si dos keys resultasen tener el mismo slot, el nodo
 a insertar se coloca en la cabeza de la lista anteriormente creada en el slot, caso contrario, será su único 1er nodo.
Aquí también los nodos tienen un campo key y un campo value. Cuando hagamos una búsqueda y nos encontremos con un slot 
que posee una lista, debemos verificar si elemento a insertar está presente, y devolver Falso en ese caso.

Mejor Caso - Si nuestra función hash es ideal y m es lo suficientemente grande
    inserción y búsqueda: O(1), se aprovecha la función al máximo y nunca hay problema de espacio, búsqueda directa
Peor Caso - Si tenemos un número considerable de colisiones y el tiempo de barrido influye:
    inserción y búsqueda: O(n), lo que se asemejaría a un array
Promedio -> NUESTRO CASO: ya que pueden cierta cantidad colisiones, de elementos diferentes, pero colisiones al fin
    inserción y búsqueda: O(n/m), lo que se asemejaría a una mezcla de array y hash ideal
"""


def unique_elements(lst):
    """Promedio de O(n/m): donde n es el len(lst) y m -arbitrario- es len(tabla)."""
    dicc = HashTable(random.randint(1, len(lst) ** 2))  # tomo un tamaño arbitrario
    for ele in lst:
        if dicc.boolean_search(ele, ele):
            return False
        dicc.insert(ele, ele)
    return True


"""Ejercicio 6
Referencias:
    https://es.wikipedia.org/wiki/ISO_3166-2:AR (1)
    https://www.escribaniavildosola.com.ar/codigos-postales-argentina.html  (2)
Criterio:
Haré 3 hashes anidadas: una para la 1er letra, otra para los 4 dígitos, y una 3ra para los últimos 3 chars
Para la 1era tomé (1) como referencia, 24 espacios únicos
Para la 2da calculé la cantidad de códigos postales por provincia en base a (2)
Para la 3era, la de las las manzanas, tomé todas las posibilidades: 26**3"""

"""Este es mi intento"""
# def argentina_postal_codes():
#     file_path = "/home/admin1/Documents/Algoritmos2/practicas/tp-hashtable/code/ex6_data.csv"
#     with open(file_path, "r") as file:
#         reader = csv.reader(file, delimiter=',')
#         province_count = sum(1 for _ in reader)
#         file.seek(0)  # reset the pointer
#         province_hash = HashTable(province_count)
#
#         for row in reader:
#             province_code, postal_count = row[0], int(row[2])
#             postal_hash = HashTable(postal_count)
#             # Generate all possible 3-character combinations
#             addresses = [''.join(i) for i in itertools.product(string.ascii_uppercase, repeat=2)]
#             for address in addresses:
#                 address_hash = HashTable(26 ** 3)
#                 postal_hash.insert(address, address_hash)
#             province_hash.insert(province_code, postal_hash)
#     return province_hash


"""Formato más sencillo, para usar una sola tabla"""


def argentina_postal_codes_hash(code):
    return sum(ord(c) for c in code)


"""Un compañero me transmitió una posible idea para implementar este ejercicio: usar una hash ponderada."""



# Driver code
if __name__ == '__main__':
    pass
    # print(argentina_postal_codes_hash("Z1636FDA"))
    # print(unique_elements([1, 5, 12, 9, 2]))
    # print(unique_elements([1, 5, 12, 2, 2]))
    # print(is_permutation("hola", "ahol"))
    # print(is_permutation("hola", "ahodl"))
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
