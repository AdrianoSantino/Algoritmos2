"""La tabla hash resultante es la c).
Primero se introduce 12, cuyo módulo 10 es 2, en i=2
Luego se introduce 18, cuyo módulo 10 es 8, en i=8
Luego se introduce 13, cuyo módulo 10 es 3, en i=3
Luego se introduce 2, cuyo módulo 10 es 2, en i=2...
    ...pero está ocupado => Saltea a i+1=3, pero está ocupado => Saltea a i+1=4
    aquí fallan b) y d), b porque no saltea y d porque usa chaining
    a) falla porque reescribe en los slots donde cae
"""

# De paso compruebo
from ejercicio11 import create, insert, print_hash

if __name__ == "__main__":
    lst = [12, 18, 13, 2, 3, 23, 5, 15]
    D = create(10)
    for ele in lst:
        insert(D, ele, ele)  # edit each insert function to get the desired hash method
    print_hash(D)
    # None None
    # None None
    # (12, 12) True
    # (13, 13) True
    # (2, 2) True
    # (3, 3) True
    # (23, 23) True
    # (5, 5) True
    # (18, 18) True
    # (15, 15) True
    pass
