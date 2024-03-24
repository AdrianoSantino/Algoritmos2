import random
import string


class AVLTree:
    root = None


class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = 0

    def display(self):
        print("\n\nAVL TREE (key, bf):\n")
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
        print('')

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.rightnode is None and self.leftnode is None:
            line = f"({self.key}, {self.bf})"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only leftnode child.
        if self.rightnode is None:
            lines, n, p, x = self.leftnode._display_aux()
            s = f"({self.key}, {self.bf})"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line
                    ] + shifted_lines, n + u, p + 2, n + u // 2

        # Only rightnode child.
        if self.leftnode is None:
            lines, n, p, x = self.rightnode._display_aux()
            s = f"({self.key}, {self.bf})"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line
                    ] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.leftnode._display_aux()
        right, m, q, y = self.rightnode._display_aux()
        s = f"({self.key}, {self.bf})"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x -
                                      1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u +
                                       y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line
                 ] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def newNode(key, val=None):
    if val is None:
        val = key
    new = AVLNode()
    new.key = key
    new.value = val
    return new


def access(AVL, key):
    def accessR(node, key):
        if node is None:
            return None

        if key < node.key:
            return accessR(node.leftnode, key)
        elif key > node.key:
            return accessR(node.rightnode, key)
        else:
            return node

    return accessR(AVL.root, key)


def insert(AVL, key, val=None):
    def insertR(node, new):
        if node is None:
            return new
        new.parent = node
        if new.key < node.key:
            node.leftnode = insertR(node.leftnode, new)
        else:
            node.rightnode = insertR(node.rightnode, new)
        return node

    new = newNode(key, val)
    AVL.root = insertR(AVL.root, new)
    return key


def delete(AVL, key):
    def deleteR(node, key):
        if node is None:
            return None
        if node.key == key:
            if node.leftnode is None and node.rightnode is None:
                return None
            elif node.leftnode is not None and node.rightnode is None:
                return node.leftnode
            elif node.leftnode is None and node.rightnode is not None:
                return node.rightnode
            else:
                temp = maximum(node.leftnode)  # or minimum(node.rightnode)
                node.key = temp.key
                node.value = temp.value
                node.leftnode = deleteR(node.leftnode, node.value)
        node.leftnode = deleteR(node.leftnode, key)
        node.rightnode = deleteR(node.rightnode, key)
        return node

    AVL.root = deleteR(AVL.root, key)
    return key


def minimum(node):
    if node.leftnode is None and node.rightnode is None:
        return node
    return minimum(node.leftnode)


def maximum(node):
    if node.leftnode is None and node.rightnode is None:
        return node
    return maximum(node.rightnode)


def rotateLeft(AVL, node):
    nodeR = node.rightnode

    if nodeR.leftnode is None and nodeR.rightnode is not None:
        if node is AVL.root:
            node.rightnode = None
            AVL.root = nodeR
        else:
            node.parent.rightnode = nodeR
        nodeR.leftnode = node

    elif nodeR.leftnode is not None and nodeR.rightnode is None:
        node.rightnode = None
        nodeR.leftnode = node
        if node is AVL.root:
            AVL.root = nodeR
        else:
            node.parent.rightnode = nodeR

    else:
        nodeRL = nodeR.leftnode
        nodeP = node.parent
        node.rightnode = nodeRL
        nodeR.leftnode = node
        if node is AVL.root:
            AVL.root = nodeR
        else:
            nodeP.leftnode = nodeR
    return AVL.root


def rotateRight(AVL, node):
    nodeL = node.leftnode

    if nodeL.rightnode is None and nodeL.leftnode is not None:
        if node is AVL.root:
            node.leftnode = None
            AVL.root = nodeL
        else:
            node.parent.leftnode = nodeL
        nodeL.rightnode = node

    elif nodeL.rightnode is not None and nodeL.leftnode is None:
        node.leftnode = None
        nodeL.rightnode = node
        if node is AVL.root:
            AVL.root = nodeL
        else:
            node.parent.leftnode = nodeL

    else:
        nodeLR = nodeL.rightnode
        nodeP = node.parent
        node.leftnode = nodeLR
        nodeL.rightnode = node
        if node is AVL.root:
            AVL.root = nodeL
        else:
            nodeP.rightnode = nodeL
    return AVL.root


def traverseIn(AVL):
    def traverseInR(node, lst):
        if node is None:
            return lst
        traverseInR(node.leftnode, lst)
        lst.append(node)
        traverseInR(node.rightnode, lst)
        return lst

    return traverseInR(AVL.root, [AVL.root])


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.leftnode), height(node.rightnode))


def balanceFactor(node):
    if node is None:
        return 0
    leftH = height(node.leftnode)
    rightH = height(node.rightnode)
    return leftH - rightH


def calculateBalance(AVL):
    lst = traverseIn(AVL)
    for node in lst:
        node.bf = balanceFactor(node)
    return AVL


def traverseBreadth(node, lst):
    lst.append(node)
    if node.leftnode is not None:
        traverseBreadth(node.leftnode, lst)
    if node.rightnode is not None:
        traverseBreadth(node.rightnode, lst)
    return


def rebalance(AVL):
    def rebalanceR(node):
        ll = list()
        traverseBreadth(node, ll)
        ll.reverse()
        root = node

        node = ll[0]
        i = 0
        while node is not root:
            if abs(node.bf) == 2:
                if node.bf == -2:
                    AVL.root = rotateLeft(AVL, node)
                elif node.bf == 2:
                    AVL.root = rotateRight(AVL, node)
                if node.parent == root:
                    break
                calculateBalance(AVL)
            elif abs(node.bf) <= 2:
                pass
            else:
                raise TypeError("Tree passed does not correspond to an AVL construction.")
            i += 1
            node = ll[i]
            # print(node.key)
            # AVL.root.display()
        return AVL

    if AVL.root is None:
        return None
    return rebalanceR(AVL.root)


def create_tree(size):
    random.seed(44)
    A = AVLTree()
    for i in range(size):
        val = random.choice(string.ascii_letters.upper())
        key = random.randint(-20, 20)
        insert(A, key, val)
    A.root.display()
    return A


A = create_tree(10)
A = calculateBalance(A)
A.root.display()
rotateLeft(A, access(A, -13))
A = calculateBalance(A)
A.root.display()
