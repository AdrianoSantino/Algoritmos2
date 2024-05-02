from dictionary import create


def hash_code_postal(code, m):
    p, dddd, ccc = code[0], code[1:5], code[5:]

    # Convertir p a su valor ASCII y restar 96 para obtener un número del 1 al 26
    hash_p = ord(p.lower()) - 96

    # Convertir dddd a un número entero
    hash_dddd = int(dddd)

    # Convertir ccc a un número sumando los valores ASCII de cada carácter
    hash_ccc = sum(ord(c) for c in ccc.lower())

    # Calcular el hash final como una combinación ponderada de hash_p, hash_dddd y hash_ccc
    w1, w2, w3 = 100, 10, 1  # pesos
    hash_final = (w1 * hash_p + w2 * hash_dddd + w3 * hash_ccc) % m
    print(hash_p, hash_dddd, hash_ccc, hash_final)

    return hash_final


def insert(D, key, value):
    index = hash_code_postal(key, len(D))
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


if __name__ == "__main__":
    P = create(100000)
    for cod, msg in [("M5501EAD", "Factura NRO..."), ("C0001ZXC", "Estimado Carlos..."), ("M5500AAB", "Hola...")]:
        insert(P, cod, msg)
    pass
