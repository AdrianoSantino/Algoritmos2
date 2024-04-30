def create(m):
    return [None] * m


def hashf(k, m):
    if type(k) is str and len(k) == 1:
        return ord(k) % m
    if type(k) is int:
        return k % m
    raise TypeError("hashf error.")


def insert(D, key, value):
    index = hashf(key, len(D))
    lst = D[index]

    if not lst:
        D[index] = [(key, value)]
        return D

    for i, (k, v) in enumerate(lst):
        if k == key:  # if pair it was already on list, updates
            lst[i] = (key, value)
            return D
    lst.append((key, value))  # else, adds it
    return D


def search(D, key):
    index = hashf(key, len(D))
    lst = D[index]

    if not lst:
        return None

    for i, (k, v) in enumerate(lst):
        if k == key:
            return v

    return None  # not found on that index


def delete(D, key):
    index = hashf(key, len(D))
    lst = D[index]

    if not lst:
        return D

    for i, (k, v) in enumerate(lst):
        if k == key:
            lst.pop(i)
            if len(lst) == 0:
                D[index] = None
            break

    return D


if __name__ == "__main__":
    dicc = create(5)
    insert(dicc, "A", 20)
    insert(dicc, 20, "G")
    print(dicc)
    print(search(dicc, 20))
    print(search(dicc, "Q"))
    delete(dicc, 20)
    print(dicc)
