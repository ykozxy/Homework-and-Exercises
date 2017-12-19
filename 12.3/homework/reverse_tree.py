class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_leaf(self):
        return not (self.left or self.right)


def reverse_tree(node):
    """
    :type node:TreeNode
    :param node:
    :return:
    """
    if node.has_left_child() and node.has_right_child():
        node.left, node.right = node.right, node.left
        reverse_tree(node.left)
        reverse_tree(node.right)
    elif node.has_left_child() and not node.has_right_child():
        node.left, node.right = node.right, node.left
        reverse_tree(node.right)
    elif not node.has_left_child() and node.has_right_child():
        node.left, node.right = node.right, node.left
        reverse_tree(node.left)
    else:
        pass


a = TreeNode(1, 1)
a.left = TreeNode(2, 2)
a.right = TreeNode(3, 3)
a.right.right = TreeNode(4, 4)
a.left.left = TreeNode(5, 5)
a.left.right = TreeNode(6, 6)
reverse_tree(a)
