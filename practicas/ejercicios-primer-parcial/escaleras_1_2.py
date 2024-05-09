def formas_llegar(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return formas_llegar(n - 1) + formas_llegar(n - 2)


if __name__ == "__main__":
    for i in range(6):
        print("N escalones:", i, "Formas:", formas_llegar(i))
