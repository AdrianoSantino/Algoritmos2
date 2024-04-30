from dictionary import *


def unique_elements(lst):
    """O(n) porque es un solo bucle, y la hash la asumo como promedio"""
    dicc = create(40)  # tamaño arbitrario
    for ele in lst:
        if search(dicc, ele):
            return False
        insert(dicc, ele, ele)
    return True


if __name__ == "__main__":
    print(unique_elements([1, 5, 12, 1, 2]))
    print(unique_elements([1, 5, 8, 2]))
