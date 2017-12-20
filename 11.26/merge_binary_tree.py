from Tree import draw_tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False


tree1 = TreeNode(2)
tree1.left = TreeNode(3)
tree1.right = TreeNode(4)
tree1.left.left = TreeNode(5)

tree2 = TreeNode(3)
tree2.left = TreeNode(5)
tree2.right = TreeNode(6)
tree2.right.left = TreeNode(3)
tree2.right.right = TreeNode(4)

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
        r.left = merge_tree(tree1.left, tree2.left)
        r.right = merge_tree(tree1.right, tree2.right)
        return r


def pre_order(tree):
    """

    :type tree: TreeNode
    """
    if tree is not None:
        print(tree.val)
        pre_order(tree.left)
        pre_order(tree.right)


draw_tree(tree1, 3)
draw_tree(tree2, 3)
a = merge_tree(tree1, tree2)
draw_tree(a)
