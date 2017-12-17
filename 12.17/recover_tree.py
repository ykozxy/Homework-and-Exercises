class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

first = None
second = None
prev = TreeNode(-1000000)

def revocer_tree(root):
    inorder_travesal(root)
    first.val, second.val = second.val, first.val

def inorder_travesal(root):
    global first, second, prev
    if root is None:
        return
    inorder_travesal(root.left)
    if first is None and prev.val >= root.val:
        first = prev

    if first is not None and prev.val >= root.val:
        second = root

    prev = root
    inorder_travesal(root.right)

r = TreeNode(3)
r.left = TreeNode(4)
r.right = TreeNode(2)
r.right.right = TreeNode(5)
