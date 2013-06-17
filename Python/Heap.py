"""
This script illustrates the heap.
@author: C.V.Krishnakumar
"""
import Queue


class HeapNode(object):
    """Represents a node of the heap"""
    def __init__(self, val):
        """ Constructor """
        super(HeapNode, self).__init__()
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def is_root(self):
        """returns if the node is a root"""
        return (self.parent == None)

    def is_leaf(self):
        """check if the node is a leaf"""
        return ((self.left == None) and (self.right == None))

    def set_left(self, child):
        """docstring for set_left"""
        self.left = child
        child.parent = self

    def set_right(self, child):
        """docstring for set_left"""
        self.right = child
        child.parent = self

    def __str__(self):
        """docstring for __str__"""
        s = ""
        s = str(self.val) + "->" \
            + str("" if self.left == None else self.left.val) \
            + " , " + str("" if self.right == None else self.right.val) + "\n"
        if self.left != None:
            s += str(self.left)
        if self.right != None:
            s += str(self.right)
        return s

    def add_child(self, child):
        """Checks if left is empty. Else adds right"""
        if self.is_leaf():
            self.set_left(child)
        else:
            self.set_right(child)
        self.max_heapify()

    def max_heapify(self):
        """docstring for heapify"""
        if self.left != None:
            if self.val < self.left.val:
                self.val, self.left.val = self.left.val, self.val
        if self.right != None:
            if self.val < self.right.val:
                self.val, self.right.val = self.right.val, self.val
        if not self.is_root():
            self.parent.max_heapify()


def generate_states(q):
    """docstring for generate_states"""
    s = []
    for i in q:
        s.append(i.left)
        s.append(i.right)
    return s


def find_place_to_insert(root):
    """returns the node in the binary tree where the item could be inserted"""
    if root == None:
        return None
    if root.is_leaf():
        return root
    q = Queue.Queue()
    q.put(root)

    visited = []
    while not q.empty():
        n = q.get()
        states = [n.left, n.right]
        for state in states:
            if state == None:
                return n
            q.put(state)
            visited.append(state)


def search_in_heap(root, val):
    """returns if val is present in the max-heap or not"""

    if root == None:
        return False

    if val == root.val:
        return True

    return search_in_heap(root.left, val) or search_in_heap(root.right, val)


def add_to_heap(root, val):
    """docstring for add_to_heap"""
    newnode = HeapNode(val)
    to_be_parent_node = find_place_to_insert(root)
    if to_be_parent_node == None:
        root = newnode
    else:
        to_be_parent_node.add_child(newnode)


def main():
    """Driver function"""
    root = HeapNode(10)
    add_to_heap(root, 5)
    add_to_heap(root, 7)
    add_to_heap(root, 3)
    add_to_heap(root, 4)

    # # Adding 6
    add_to_heap(root, 6)
    add_to_heap(root, 8)
    add_to_heap(root, 100)
    add_to_heap(root, 1000)

    print root
    print search_in_heap(root, 1002)


if __name__ == '__main__':
    main()
