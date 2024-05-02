from ejercicio11 import create, insert, print_hash

if __name__ == "__main__":
    lst = [10, 22, 31, 4, 15, 28, 17, 88, 59]
    D = create(11)
    for ele in lst:
        insert(D, ele, ele)  # edit each insert function to get the desired hash method
    print_hash(D)
    pass

"""
1. Linear probing
(22, 22) True
(88, 88) True
None None
None None
(4, 4) True
(15, 15) True
(28, 28) True
(17, 17) True
(59, 59) True
(31, 31) True
(10, 10) True

2. Quadratic probing con c1 = 1 y c2 = 3
(22, 22) True
(17, 17) True
(59, 59) True
(88, 88) True
(4, 4) True
None None
(28, 28) True
(15, 15) True
None None
(31, 31) True
(10, 10) True

3. Double hashing con h1(k) = k y h2(k) = 1 +(k mod ( m - 1))
(22, 22) True
None None
(59, 59) True
(17, 17) True
(4, 4) True
(15, 15) True
(28, 28) True
(88, 88) True
None None
(31, 31) True
(10, 10) True


"""
