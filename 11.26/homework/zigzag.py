class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.leftChild = None
        self.rightChild = None

    def is_leaf(self):
        if self.leftChild is None and self.rightChild is None:
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
            temp_lst.append(node.leftChild)
            temp_lst.append(node.rightChild)
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
                print(element.key, end=' ')
        reverse = not reverse


a = BinaryTree(3)
a.leftChild = BinaryTree(9)
a.rightChild = BinaryTree(20)
a.rightChild.leftChild = BinaryTree(15)
a.rightChild.rightChild = BinaryTree(7)
zigzag(a)
