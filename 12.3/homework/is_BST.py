class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def has_left_child(self):
        return self.leftChild

    def has_right_child(self):
        return self.rightChild

    def is_leaf(self):
        return not (self.leftChild or self.rightChild)


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
        if node.leftChild.key >= current_key:
            return False
        if node.rightChild.key <= current_key:
            return False
        return is_bst(node.leftChild) and is_bst(node.rightChild)
    elif node.has_left_child() and not node.has_right_child():
        if node.leftChild.key >= current_key:
            return False
        return is_bst(node.leftChild) and is_bst(node.rightChild)
    elif not node.has_left_child() and node.has_right_child():
        if node.rightChild.key <= current_key:
            return False
        return is_bst(node.leftChild) and is_bst(node.rightChild)


a = TreeNode(3, 3)
a.leftChild = TreeNode(1, 1)
a.rightChild = TreeNode(5, 5)
a.leftChild.leftChild = TreeNode(0, 1)

print(is_bst(a))
