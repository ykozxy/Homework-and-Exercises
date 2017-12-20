from Tree import draw_tree, deserialize


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
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


a = deserialize([1,
                 2, 3,
                 4, 5, 6, 7,
                 8, 9, 1, 2, 'null', 'null', 5, 6])
draw_tree(a, 5)
reverse_tree(a)
draw_tree(a)
