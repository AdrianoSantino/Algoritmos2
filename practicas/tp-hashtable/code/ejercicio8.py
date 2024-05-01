from dictionary import hashf, create, search


def insert(D, key, value):
    index = hashf(key, len(D))
    lst = D[index]

    if not lst:
        D[index] = [(key, value)]
        return D

    for i, (k, v) in enumerate(lst):
        if k == key:  # EDIT regarding original: if pair it was already on list, returns, we just want 1st time appeared
            return D
    lst.append((key, value))  # else, adds it
    return D


def first_app(p, s):
    """O(k-l+1 + k/l) => O(k/l), con k y l las longitudes de p y s, respectivamente"""
    if len(s) > len(p):
        return None
    dicc = create(len(p))
    for i in range(len(p) - len(s) + 1):  # O(k-l+1) => O(k), siempre
        part = p[i:i + len(s)]
        insert(dicc, part, i)
    return search(dicc, s)  # O(k/l), ya que depende de la longitud de l, y la naturaleza de p, ya que si en p hay
    # permutaciones de s, sin ser alguna estrictamente p, la lista enlazada puede extenderse (hasta tener len = k)???


if __name__ == "__main__":
    print(first_app("abracadabra", "cada"))
    print(first_app("hola, estoy buscando esta palabra, no esta", "esta"))
    print(first_app("aaxxaaaxxxaaaxxxaaaxxxxax", "xax"))  # caso ineficiente
    print(first_app("abcdefgh", "X"))
