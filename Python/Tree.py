# Tree


class TreeNode(object):
    """ Structure for a Node in the Tree"""
    def __init__(self, val, parent):
        """ Constructor """
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self):
        """ Display function"""
        return self.val


def inorder(root):
    """Inorder Traversal"""
    if root == None:
        return
    else:
        inorder(root.left)
        print str(root.val), "->",
        inorder(root.right)


def preorder(root):
    """Inorder Traversal"""
    if root == None:
        return
    else:
        print str(root.val), "->",
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """Inorder Traversal"""
    if root == None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print str(root.val), "->",


def is_leaf_node(node):
    """Returns if the node is a leaf node"""
    if node == None:
        return False
    else:
        return ((node.left == None) and (node.right == None))


def depth(root):
    """returns the depth of the tree"""
    if root == None:
        return 0
    if is_leaf_node(root):
        return 1
    else:
        return 1 + max(depth(root.left), depth(root.right))
    pass


def main():
    """Main function"""
    root = TreeNode(1, None)
    x = TreeNode(2, root)
    y = TreeNode(3, root)
    root.left = x
    root.right = y
    z = TreeNode(4, x)
    w = TreeNode(5, x)
    x.left = z
    x.right = w
    # Do it now
    print "\nInorder Traversal:"
    inorder(root)
    print "\nPreorder Traversal:"
    preorder(root)
    print "\nPostorder Traversal:"
    postorder(root)

    print "\nDepth of the tree: ", depth(root)


if __name__ == '__main__':
    main()
