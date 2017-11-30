class TreeNode:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None


tree2 = TreeNode(1)
tree2.leftChild = TreeNode(5)
tree2.rightChild = TreeNode(6)
tree2.rightChild.leftChild = TreeNode(3)
tree2.rightChild.rightChild = TreeNode(4)


def pre_order(tree):
    """

    :type tree: TreeNode
    """
    if tree is not None:
        print(tree.key)
        pre_order(tree.leftChild)
        pre_order(tree.rightChild)


def post_order(tree):
    """
    :type tree: TreeNode
    :param tree:
    :return:
    """
    if tree is not None:
        pre_order(tree.leftChild)
        pre_order(tree.rightChild)
        print(tree.key)


def in_order(tree):
    """
    :type tree: TreeNode
    :param tree:
    :return:
    """
    if tree is not None:
        pre_order(tree.leftChild)
        print(tree.key)
        pre_order(tree.rightChild)
