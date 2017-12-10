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
    '''
    :type node:TreeNode
    :param node:
    :return:
    '''
    if node.is_leaf():
        pass

