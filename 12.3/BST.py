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


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        """
        :type current_node: TreeNode
        :param key:
        :param value:
        :param current_node:
        :return:
        """
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.leftChild)
            else:
                current_node.leftChile = TreeNode(key=key, val=value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, value, parent=current_node)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def _remove(self, current_node):
        """
        :type current_node: TreeNode
        :param current_node:
        :return:
        """
        if current_node.is_leaf():
            if current_node == current_node.parent.leftChild():
                current_node.parent.leftChild = None
            else:
                current_node.parent.rightChild = None
        elif current_node.has_both_children():
            smallest_node = self._find_min(current_node)
            assert smallest_node is TreeNode
            current_node.key = smallest_node.key
            current_node.value = smallest_node.value

            if smallest_node.rightChild.key < smallest_node.parent.key:
                smallest_node.parent.leftChild = smallest_node.rightChild
            else:
                smallest_node.parent.rightChild = smallest_node.rightChild

        else:
            if current_node.rightChild is not None:
                current_node.key = current_node.rightChild.key
                current_node.value = current_node.rightChild.value
                if current_node.rightChild.has_right_child():
                    current_node.rightChild = current_node.rightChild.rightChild
                if current_node.rightChild.has_left_child():
                    current_node.leftChild = current_node.rightChild.leftChild

            elif current_node.leftChild is not None:
                current_node.key = current_node.leftChild.key
                current_node.value = current_node.leftChild.value
                if current_node.leftChild.has_right_child():
                    current_node.rightChild = current_node.leftChild.rightChild
                if current_node.leftChild.has_left_child():
                    current_node.leftChild = current_node.leftChild.leftChild

    @staticmethod
    def _find_min(current_node):
        """
        :type current_node: TreeNode
        :param current_node:
        :return:
        """
        current_node = current_node.rightChild
        while current_node.leftChild is not None:
            current_node.leftChild.parent = current_node
            current_node = current_node.leftChild
        return current_node


def pre_order(tree):
    """

    :type tree: TreeNode
    """
    if tree is not None:
        print(tree.key)
        pre_order(tree.leftChild)
        pre_order(tree.rightChild)


a = BST()


for i in range(100):
    a[i] = i

print(a[3])
a.delete(3)
print(a[3])
pre_order(a.root)
