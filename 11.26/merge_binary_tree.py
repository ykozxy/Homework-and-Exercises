class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.leftChild = None
        self.rightChild = None

    def is_leaf(self):
        if self.leftChild is None and self.rightChild is None:
            return True
        return False


tree1 = TreeNode(2)
tree1.leftChild = TreeNode(3)
tree1.rightChild = TreeNode(4)
tree1.leftChild.leftChild = TreeNode(5)

tree2 = TreeNode(3)
tree2.leftChild = TreeNode(5)
tree2.rightChild = TreeNode(6)
tree2.rightChild.leftChild = TreeNode(3)
tree2.rightChild.rightChild = TreeNode(4)

def merge_tree(tree1, tree2):
    """
    :type tree1: TreeNode
    :type tree2: TreeNode
    """
    if tree1 is None:
        return tree2
    elif tree2 is None:
        return tree1
    else:
        r = TreeNode(tree1.val + tree2.val)
        r.leftChild = merge_tree(tree1.leftChild, tree2.leftChild)
        r.rightChild = merge_tree(tree1.rightChild, tree2.rightChild)
        return r


def pre_order(tree):
    """

    :type tree: TreeNode
    """
    if tree is not None:
        print(tree.val)
        pre_order(tree.leftChild)
        pre_order(tree.rightChild)


pre_order(merge_tree(tree1, tree2))
