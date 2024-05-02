from dictionary import create, insert, search


def contains(setS, setT):
    """Verifica si setS ⊆ setT.
    Caso Promedio: O(t + s): se tiene que crear el hash de T y la búsqueda de los s siempre se hace"""
    if len(setS) > len(setT):
        return False
    dicT = create(len(setT))
    for t in setT:
        insert(dicT, t, t)
    for s in setS:
        if search(dicT, s) is None:
            return False
    return True


if __name__ == "__main__":
    print(contains([2, 0], [0, 1, 2, -1000, 5]))
    print(contains([0], [0]))
    print(contains([0], [1, 2]))
