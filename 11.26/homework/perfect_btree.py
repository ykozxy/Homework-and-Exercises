class TreeNode:
    def __init__(self, root_obj):
        self.val = root_obj
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False



def is_binary_tree(head):
    """
    :type head: TreeNode
    :param head:
    :return:
    """
    if head.left is None and head.right is None:
        return True
    elif head.left is not None and head.right is not None:
        lft = head.left
        right = head.right
        if is_binary_tree(lft) and is_binary_tree(right):
            return True
        else:
            return False
    else:
        return False


def perfect_tree(head):
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
            elif not (node.left is None and node.right is None):
                end = False
        if end:
            break

        # Update nodes
        for node in output[-1]:
            temp_lst.append(node.left)
            temp_lst.append(node.right)
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


a = TreeNode(1)
a.left = TreeNode(1)
a.right = TreeNode(1)
a.left.left = TreeNode(1)
a.left.right = TreeNode(1)
a.right.right = TreeNode(1)

print(perfect_tree(a))
