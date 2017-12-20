from Tree import deserialize, draw_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recover_tree(node):
    first = None
    second = None
    prev = TreeNode(-1000000)

    def start(root):
        inorder_travesal(root)
        first.val, second.val = second.val, first.val

    def inorder_travesal(root):
        nonlocal first, second, prev
        if root is None:
            return
        inorder_travesal(root.left)
        if first is None and prev.val >= root.val:
            first = prev

        if first is not None and prev.val >= root.val:
            second = root

        prev = root
        inorder_travesal(root.right)

    start(node)


# Test data 1
a = deserialize([5,
                 2, 7,
                 9, 3, 6, 1])
draw_tree(a, notstay=3)
recover_tree(a)
draw_tree(a, notstay=3)

# Test data 2
a = deserialize([8,
                 5, 11,
                 'null', 'null', 12, 9])
draw_tree(a, notstay=3)
recover_tree(a)
draw_tree(a, notstay=3)

# Test data 3
a = deserialize([2,
                 'null', 1])
draw_tree(a, notstay=3)
recover_tree(a)
draw_tree(a, notstay=3)
