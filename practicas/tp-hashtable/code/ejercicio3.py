from math import sqrt, floor

from dictionary import *


def hashf(k, m):
    A = (sqrt(5) - 1) / 2
    return floor(m * (k * A % 1))


if __name__ == "__main__":
    dicc = create(1000)
    for num in range(61, 66):
        print(hashf(num, 1000))
