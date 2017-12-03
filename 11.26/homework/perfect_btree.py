class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.leftChild = None
        self.rightChild = None


def is_binary_tree(head):
    """
    :type head: BinaryTree
    :param head:
    :return:
    """
    if head.leftChild is None and head.rightChild is None:
        return True
    elif head.leftChild is not None and head.rightChild is not None:
        lft = head.leftChild
        right = head.rightChild
        if is_binary_tree(lft) and is_binary_tree(right):
            return True
        else:
            return False
    else:
        return False


a = BinaryTree(1)
a.leftChild = BinaryTree(1)
a.rightChild = BinaryTree(1)
a.leftChild.leftChild = BinaryTree(1)
a.leftChild.rightChild = BinaryTree(1)
a.rightChild.rightChild = BinaryTree(1)

print(is_binary_tree(a))
