
def contiene_suma(A, n):  # (O(n*logn))

    A.sort()  # (O(n*logn)) Timsort algorithm
    lo = 0
    hi = len(A) - 1

    # Mientras que el puntero low sea menor al high, continuemos intentando
    while lo < hi:  # O(n) en el peor de los casos se recorre todo la lista
        # Si la suma de los dos punteros cumple el objetivo, devolvemos True
        if A[lo] + A[hi] == n:
            return True
        # Si no, si no alcanza con la suma, adelantemos low
        elif A[lo] + A[hi] < n:
            lo += 1
        # Si ni la suma cumple, y hi nos sobrepasa (la lista está ordenada), entonces bajemos high
        else:
            hi -= 1

    # Si no hemos hallado habiendo recorrido toda la lista (lo >= hi), no existe tal caso
    return False

