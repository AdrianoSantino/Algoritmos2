from math import floor, sqrt


def dictionary(size):
    return [None] * size


def hashf_division_method(key, D):
    return key % len(D)


def hashf_multiplication_method(key, D):
    A = (sqrt(5) - 1) / 2
    return floor(len(D) * ((key * A) % 1))


"""Ejercicio 2"""


def insert(D, key, value):
    index = hashf_division_method(key, D)
    if not D[index]:
        D[index] = []
    D[index].append(value)
    return index


def search(D, key):
    index = hashf_division_method(key, D)
    return key if D[index] else None


def delete(D, key):
    index = hashf_division_method(key, D)
    if D[index]:
        D[index] = None  # deletes the complete slot
    return D


"""Ejercicio 4"""


def isPermutation(s1: str, s2: str):
    """Para una hash ideal: O(2n+m), siendo n y m las longitudes de las cadenas s1 y s2, respectivamente."""

    def hashf_ascii_placement(key, D):
        return ord(key) % len(D)

    def insert(D, key):
        index = hashf_ascii_placement(key, D)
        if not D[index]:
            D[index] = 1
        else:
            D[index] += 1  # se agrega un contador de letras!
        return index

    def search(D, key):
        index = hashf_ascii_placement(key, D)
        return D[index] if D[index] else None

    size = 27  # tomando abecedario español en minúsculas
    D1 = dictionary(size)
    D2 = dictionary(size)

    for l1 in s1:  # se insertan todas las keys en un diccionario
        insert(D1, l1)
    for l2 in s2:  # se insertan todas las keys en otro diccionario O(m)
        insert(D2, l2)

    # se toma uno de los string y se lo barre letra a letra
    # se verifica si cada letra existe y si existe, se chequea la cantidad de letras"""
    for l1 in s1:
        if search(D1, l1) != search(D2, l1):
            return False
    return True
