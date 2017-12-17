class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def has_left_child(self):
        return self.leftChild

    def has_right_child(self):
        return self.rightChild

    def is_leaf(self):
        return not (self.leftChild or self.rightChild)

    def is_root(self):
        return not self.parent

    def has_both_children(self):
        return self.leftChild and self.rightChild

    def set_child_of_parent(self):
        if self.parent is None:
            raise AttributeError("Parent do not exist")
        elif self.value < self.parent.value:
            self.parent.leftChild = self
        else:
            self.parent.rightChild = self


def avl_to_node(node):
    """
    :type node: TreeNode
    :param node:
    :return:
    """
    output = [[node]]

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

    return output


a = TreeNode(5, 5)
a.leftChild = TreeNode(3, 3)
a.rightChild = TreeNode(7, 7)
a.leftChild.leftChild = TreeNode(2, 2)
a.leftChild.rightChild = TreeNode(4, 4)

# todo Need to sort the output list (may use enumerator)
lst = avl_to_node(a)
print(lst)
b = []
for i in lst:
    for x in i:
        if x is None:
            continue
        else:
            b.append(x.key)
print(b)
