class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False


def generate_trees(n):
    def generate(first, last):
        trees = []
        for root in range(first, last + 1):
            for left in generate(first, root - 1):
                for right in generate(root + 1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees += node,
        return trees or [None]

    return generate(1, n)


def zigzag(head):
    """
    :type head: TreeNode
    :param head:
    :return:
    """
    output = [[head]]

    while True:
        # Add Nodes
        temp_lst = []

        # Exit?
        end = True
        for node in output[-1]:
            if node is None:
                continue
            elif not node.is_leaf():
                end = False
        if end:
            break

        # Update nodes
        for node in output[-1]:
            if node:
                temp_lst.append(node.left)
                temp_lst.append(node.right)
        output.append(temp_lst)

    # Output
    reverse = False
    for node_lst in output:
        print('\n', end='')
        if reverse:
            node_lst.reverse()
        for element in node_lst:
            if element is None:
                print('Null', end=' ')
            else:
                print(element.val, end=' ')
        reverse = not reverse


def pre_order(tree):
    """

    :type tree: TreeNode
    """
    if tree is not None:
        if not pre_order(tree.right):
            return [tree.val] + pre_order(tree.left)
        elif not pre_order(tree.left):
            return [tree.val] + ['null'] + pre_order(tree.right)
        else:
            return [tree.val] + pre_order(tree.left) + pre_order(tree.right)
    else:
        return []


a = generate_trees(4)
for i in a:
    print(pre_order(i))
    print('----------------------------')
