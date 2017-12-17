class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(node):
    # [node.key, node,left, node.right]
    def doit(node):
        if node:
            vals.append(str(node.val))
            doit(node.left)
            doit(node.right)
        else:
            vals.append('null')

    vals = []
    doit(node)
    return vals


def deserialize(lst):
    def doit():
        val = next(vals)
        if val == 'null':
            return None
        node = TreeNode(int(val))
        node.left = doit()
        node.right = doit()
        return node

    vals = iter(lst)
    return doit()

if __name__ == '__main__':
    r = TreeNode(1)
    print(serialize(r))
    # print(deserialize('1 null null'))
    print(serialize(deserialize([3, 'null', 1, 'null', 'null'])))

