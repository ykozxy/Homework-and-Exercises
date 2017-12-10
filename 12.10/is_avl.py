class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_avl(node):

    def deep(head):
        """
        :type head: TreeNode
        :param head:
        :return:
        """
        if head is None:
            return 0
        left = deep(head.left)
        right = deep(head.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return deep(node) != -1


a = TreeNode(5)
a.left = TreeNode(4)
a.right = TreeNode(3)
a.left.left = TreeNode(1)
a.right.right = TreeNode(2)

print(is_avl(a))
