import string

from dictionary import *


def insert_count(D, k):
    """Assign the value field as the num of times it has appeared"""
    count = search(D, k)
    if not count:
        insert(D, k, 1)
    else:
        insert(D, k, count + 1)
    return k


def is_permutation(s1, s2):
    """O(n), porque son 3 bucles separados que usan una hash ideal"""
    d1 = create(len(string.ascii_letters))
    d2 = create(len(string.ascii_letters))

    for let in s1:
        insert_count(d1, let)
    for let in s2:
        insert_count(d2, let)

    for let in s1:
        if search(d1, let) != search(d2, let):
            return False
    return True


if __name__ == "__main__":
    print(is_permutation("hola", "ahlo"))
    print(is_permutation("hola", "ahdo"))
