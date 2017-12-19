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


def is_bst(node):
    """
    :type node:TreeNode
    :param node:
    :return:
    """
    if not node:
        return True
    current_key = node.key
    if node.is_leaf():
        return True
    elif node.has_left_child() and node.has_right_child():
        if node.left.key >= current_key:
            return False
        if node.right.key <= current_key:
            return False
        return is_bst(node.left) and is_bst(node.right)
    elif node.has_left_child() and not node.has_right_child():
        if node.left.key >= current_key:
            return False
        return is_bst(node.left) and is_bst(node.right)
    elif not node.has_left_child() and node.has_right_child():
        if node.right.key <= current_key:
            return False
        return is_bst(node.left) and is_bst(node.right)


a = TreeNode(3, 3)
a.left = TreeNode(1, 1)
a.right = TreeNode(5, 5)
a.left.left = TreeNode(0, 1)

print(is_bst(a))
