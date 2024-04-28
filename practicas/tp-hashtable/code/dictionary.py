from math import floor, sqrt


def dictionary(size):
    return [None] * size


def hashf_division_method(key, D):
    return key % len(D)


def hashf_multiplication_method(key, D):
    A = (sqrt(5) - 1) / 2
    return floor(len(D) * ((key * A) % 1))


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
