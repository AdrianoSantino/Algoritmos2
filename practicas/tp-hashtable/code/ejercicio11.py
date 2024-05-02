"""¿La lista debe estar doblemente enlazada o con una simplemente enlazada alcanza?
Con que sea simplemente enlazada basta, en ese caso es necesario reiniciar el puntero una vez llega al índice máximo
y bien mantener un contador (o una referencia de partida) para evitar bucles infinitos.
Para el caso de la doblemente enlazada es más sencillo, ya que la búsqueda acaba cuando ambos punteros se tornan None"""


class slot:
    val = None
    flag = None
    """flag as 'isOccupied', possible values: (None, True, False) = (empty, occupied, deleted)"""


def create(m):
    """Each tuple (a, b) represents (key-value-pair, slot-flag)"""
    table = []
    for i in range(m):
        new = slot()
        table.append(new)
    return table


def hashf(k):
    return k


def linear_probing(k, i, m):
    return (hashf(k) + i) % m


def quadratic_probing(k, i, m, c1=1, c2=2):
    return (hashf(k) + c1 * i + c2 * i) % m


def double_hashing(k, i, m):
    def hash_1(k):
        return k

    def hash_2(k):
        return 1 + (k % (m - 1))

    return (hash_1(k) + i * hash_2(k)) % m


def insert(D, key, value):
    i = 0
    while True:
        if i >= len(D):
            raise Exception("hash table is full")

        index = linear_probing(key, i, len(D))
        if index >= len(D):  # resets pointer to beginning of list
            index = 0

        slot = D[index]
        if slot.flag is None or slot.flag is False:
            slot.val = (key, value)
            slot.flag = True
            return D
        else:
            k, v = slot.val
            if k == key:
                slot.val = (key, value)  # overwrites if key already exists

        i += 1


def search(D, key):
    i = 0
    while True:
        if i >= len(D):
            return None

        index = linear_probing(key, i, len(D))
        if index >= len(D):  # resets pointer to beginning of list
            index = 0

        slot = D[index]
        if slot.flag is True:
            k, v = slot.val
            if k == key:
                return v
        elif slot.flag is None:
            return None

        i += 1


def delete(D, key):
    i = 0
    while True:
        if i >= len(D):
            return None

        index = linear_probing(key, i, len(D))
        if index >= len(D):  # resets pointer to beginning of list
            index = 0

        slot = D[index]
        if slot.flag is True:
            k, v = slot.val
            if k == key:
                slot.val = None
                slot.flag = False
                return D
        elif slot.flag is None:  # key not found
            return D
        else:  # slot occupied
            pass

        i += 1


def print_hash(D):
    print("\n==========> HASH")
    for index in range(len(D)):
        slot = D[index]
        print(slot.val, slot.flag)
    print("")
    return


if __name__ == "__main__":
    table = create(4)
    insert(table, 2, 2)
    insert(table, 8, 3)
    insert(table, 11, "ASD")
    print_hash(table)
    # insert(table, 3, 5)
    print(search(table, 5))
    print(search(table, 8))
    delete(table, 11)
    print_hash(table)
    pass
