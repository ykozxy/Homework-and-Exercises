class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.leftChild = None
        self.rightChild = None

    def is_leaf(self):
        if self.leftChild is None and self.rightChild is None:
            return True
        return False



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


def perfect_tree(head):
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

    for node_lst in output[: -2]:
        if None in node_lst:
            return False

    for node_lst in output[-2 :]:
        have_none = False
        for element in node_lst:
            if element:
                if have_none:
                    return False
            elif element is None:
                have_none = True

    return True


a = BinaryTree(1)
a.leftChild = BinaryTree(1)
a.rightChild = BinaryTree(1)
a.leftChild.leftChild = BinaryTree(1)
a.leftChild.rightChild = BinaryTree(1)
a.rightChild.rightChild = BinaryTree(1)

print(perfect_tree(a))
