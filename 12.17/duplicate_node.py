from Tree import deserialize, draw_tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def has_duplicate_node(head):
    def dul(node):
        """
        :type node:TreeNode
        :param node:
        :return:
        """
        nonlocal total_node, dul_node
        if not node:
            return
        elif node.val in total_node:
            if node.val not in [r.val for r in dul_node]:
                dul_node.append(node)

        total_node.append(node.val)
        dul(node.left)
        dul(node.right)

    total_node = []
    dul_node = []
    dul(head)
    return dul_node


a = deserialize([1, 2, 3, 4, 'null', 2, 4, 'null', 'null', 4])
b = has_duplicate_node(a)
print(b)
for i in b:
    print(i.val)
draw_tree(a)
