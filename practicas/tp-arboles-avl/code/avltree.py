import random


class AVLTree:
    root = None


class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = 0  # balance factor

    def display(self):
        """Functions that prints the structure an AVLTree on console by showing each node's (key, bf)"""
        print("\n\nAVL TREE (key, bf, parent.key):\n")
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
        print('')

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.rightnode is None and self.leftnode is None:
            if self.parent is not None:
                line = f"({self.key}, {self.bf}, {self.parent.key})"
            else:
                line = f"({self.key}, {self.bf}, {None})"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only leftnode child.
        if self.rightnode is None:
            lines, n, p, x = self.leftnode._display_aux()
            if self.parent is not None:
                s = f"({self.key}, {self.bf}, {self.parent.key})"
            else:
                s = f"({self.key}, {self.bf}, {None})"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line
                    ] + shifted_lines, n + u, p + 2, n + u // 2

        # Only rightnode child.
        if self.leftnode is None:
            lines, n, p, x = self.rightnode._display_aux()
            if self.parent is not None:
                s = f"({self.key}, {self.bf}, {self.parent.key})"
            else:
                s = f"({self.key}, {self.bf}, {None})"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line
                    ] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.leftnode._display_aux()
        right, m, q, y = self.rightnode._display_aux()
        if self.parent is not None:
            s = f"({self.key}, {self.bf}, {self.parent.key})"
        else:
            s = f"({self.key}, {self.bf}, {None})"
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
    """Creates an AVLNode by specifying key and op. value"""
    if val is None:
        val = key
    new = AVLNode()
    new.key = key
    new.value = val
    return new


def access(AVL, key) -> AVLNode:
    """Accesses an AVLNode by key and returns it - O(log(n))"""

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
    """Inserts an AVLNode using the divide and conquer method, returns the current root"""

    def insertR(new, node):
        if node is None:
            return new
        new.parent = node
        if new.key < node.key:
            node.leftnode = insertR(new, node.leftnode)
        else:
            node.rightnode = insertR(new, node.rightnode)
        return node

    new = newNode(key, val)
    AVL.root = insertR(new, AVL.root)
    rebalance(AVL)
    return AVL.root


def delete(AVL, key):
    """Deletes an AVLNode by key, returns the current root"""

    def deleteR(node, key):
        if node is None:
            return None
        if node.key == key:
            if node.leftnode is None and node.rightnode is None:  # the node is a leaf
                return None
            elif node.leftnode is not None and node.rightnode is None:  # only has left child
                return node.leftnode
            elif node.leftnode is None and node.rightnode is not None:  # only has right child
                return node.rightnode
            else:
                #  has both left and right children
                temp = maximum(node.leftnode)  # or minimum(node.rightnode)
                node.key = temp.key
                node.value = temp.value
                node.leftnode = deleteR(node.leftnode, node.value)
        node.leftnode = deleteR(node.leftnode, key)
        node.rightnode = deleteR(node.rightnode, key)
        return node

    AVL.root = deleteR(AVL.root, key)
    rebalance(AVL)
    return AVL.root


def minimum(node) -> AVLNode:
    """Given a Tree node, returns its minimum successor"""
    if node.leftnode is None and node.rightnode is None:
        return node
    return minimum(node.leftnode)


def maximum(node) -> AVLNode:
    """Given a Tree node, returns its maximum successor"""
    if node.leftnode is None and node.rightnode is None:
        return node
    return maximum(node.rightnode)


def traverseIn(AVL) -> list:
    """Returns a list of nodes after traverseIn order - 0(n): all nodes need to be reached"""

    def traverseInR(node, lst):
        if node is None:
            return lst
        traverseInR(node.leftnode, lst)
        lst.append(node)
        traverseInR(node.rightnode, lst)
        return lst

    return traverseInR(AVL.root, [AVL.root])


def traverseBreadth(AVL):
    """Returns a list of nodes after traverseBreadth - 0(n): all nodes need to be reached"""

    def traverseBreadthR(Q, current):
        L = []
        Q.append(current)
        while len(Q) > 0:
            current = Q.pop(0)
            L.append(current)
            if current.leftnode:
                Q.append(current.leftnode)
            if current.rightnode:
                Q.append(current.rightnode)
        return L

    if AVL.root is not None:
        return traverseBreadthR([], AVL.root)
    return None


def height(node) -> int:
    if node is None:
        return 0
    return 1 + max(height(node.leftnode), height(node.rightnode))


def balanceFactor(node) -> int:
    if node is None:
        return 0
    leftH = height(node.leftnode)
    rightH = height(node.rightnode)
    return leftH - rightH


def rotateLeft(AVL, node) -> AVLNode:
    """Returns the new root"""

    nodeR = node.rightnode
    node.rightnode = nodeR.leftnode
    nodeR.leftnode = node
    node.parent = node.rightnode
    nodeR.parent = None
    refresh_parents(AVL)
    calculateBalance(AVL)
    return nodeR


def rotateRight(AVL, node) -> AVLNode:
    """Returns the new root"""

    nodeL = node.leftnode
    node.leftnode = node.leftnode.rightnode
    nodeL.rightnode = node
    node.parent = node.leftnode
    nodeL.parent = None
    refresh_parents(AVL)
    calculateBalance(AVL)
    return nodeL


def rotateCases(AVL, node) -> AVLNode | None:
    """Given an unbalanced node (defined as root), performs the corresponding rotation, returns the resulting root"""
    if node is None:
        return None

    if node.bf in [-1, 0, 1]:
        return node

    elif node.bf == -2:
        nodeR = node.rightnode
        if nodeR.bf in [0, 1]:
            node.rightnode = rotateRight(AVL, nodeR)
        return rotateLeft(AVL, node)

    elif node.bf == 2:
        nodeL = node.leftnode
        if nodeL.bf in [-1, 0]:
            node.leftnode = rotateLeft(AVL, nodeL)
        return rotateRight(AVL, node)

    else:
        raise Exception("Not an AVL construct")


def calculateBalance(AVL):
    """Calculates balance factors by reference, no need to reassign. O(n^2)"""
    trv_in = traverseIn(AVL)
    for node in trv_in:
        node.bf = balanceFactor(node)
    return AVL


def find_low_unb(AVL) -> AVLNode | None:
    trv_bre = traverseBreadth(AVL)
    trv_bre.reverse()
    for node in trv_bre:
        if abs(node.bf) > 1:
            return node
    return None


def rebalance(AVL):
    """Given a nearby-unbalanced AVL tree construction, rebalances and returns the AVL"""

    refresh_parents(AVL)
    calculateBalance(AVL)

    while True:
        low = find_low_unb(AVL)
        if low is None:
            break
        if low is AVL.root:
            AVL.root = rotateCases(AVL, low)
            refresh_parents(AVL)
            calculateBalance(AVL)
            break

        lowP = low.parent
        if lowP.leftnode is low:
            lowP.leftnode = rotateCases(AVL, low)
        else:  # lowP.rightnode is low
            lowP.rightnode = rotateCases(AVL, low)

        refresh_parents(AVL)
        calculateBalance(AVL)

    return AVL


def refresh_parents(AVL) -> None:
    """Assign each node its current parent"""

    def refresh_parentsR(node):
        if node is None:
            return
        if node.leftnode is not None:
            node.leftnode.parent = node
        if node.rightnode is not None:
            node.rightnode.parent = node
        refresh_parentsR(node.leftnode)
        refresh_parentsR(node.rightnode)
        return

    return refresh_parentsR(AVL.root)


def test():
    random.seed(9)
    A = AVLTree()
    for key in range(7):
        A.root = insert(A, random.randint(0, 50))
    A.root.display()
    A.root = delete(A, A.root.rightnode.leftnode.key)  # after this deletion, AVL becomes highly unbalanced
    A.root.display()


test()
