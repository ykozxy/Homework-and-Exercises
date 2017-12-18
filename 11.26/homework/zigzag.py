class BinaryTree:
    def __init__(self, root_obj):
        self.val = root_obj
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False


def zigzag(head):
    """
    :type head: BinaryTree
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


a = BinaryTree(3)
a.left = BinaryTree(9)
a.right = BinaryTree(20)
a.right.left = BinaryTree(15)
a.right.right = BinaryTree(7)
zigzag(a)
