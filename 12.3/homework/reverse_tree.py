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


def reverse_tree(node):
    '''
    :type node:TreeNode
    :param node:
    :return:
    '''
    if node.has_left_child() and node.has_right_child():
        node.leftChild, node.rightChild = node.rightChild, node.leftChild
        reverse_tree(node.leftChild)
        reverse_tree(node.rightChild)
    elif node.has_left_child() and not node.has_right_child():
        node.leftChild, node.rightChild = node.rightChild, node.leftChild
        reverse_tree(node.rightChild)
    elif not node.has_left_child() and node.has_right_child():
        node.leftChild, node.rightChild = node.rightChild, node.leftChild
        reverse_tree(node.leftChild)
    else:
        pass


def pre_order(tree):
    """

    :type tree: TreeNode
    """
    if tree is not None:
        print(tree.key)
        pre_order(tree.leftChild)
        pre_order(tree.rightChild)


a = TreeNode(1, 1)
a.leftChild = TreeNode(2, 2)
a.rightChild = TreeNode(3, 3)
a.rightChild.rightChild = TreeNode(4, 4)
a.leftChild.leftChild = TreeNode(5, 5)
a.leftChild.rightChild = TreeNode(6, 6)
reverse_tree(a)
