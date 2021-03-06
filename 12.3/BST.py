class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_leaf(self):
        return not (self.left or self.right)

    def is_root(self):
        return not self.parent

    def has_both_children(self):
        return self.left and self.right

    def set_child_of_parent(self):
        if self.parent is None:
            raise AttributeError("Parent do not exist")
        elif self.val < self.parent.val:
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
                self._put(key, value, current_node.left)
            else:
                current_node.leftChile = TreeNode(key=key, val=value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right)
            else:
                current_node.right = TreeNode(key, value, parent=current_node)

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
            current_node.val = smallest_node.value

            if smallest_node.rightChild.key < smallest_node.parent.key:
                smallest_node.parent.leftChild = smallest_node.rightChild
            else:
                smallest_node.parent.rightChild = smallest_node.rightChild

        else:
            if current_node.right is not None:
                current_node.key = current_node.right.key
                current_node.val = current_node.right.value
                if current_node.right.has_right_child():
                    current_node.right = current_node.right.rightChild
                if current_node.right.has_left_child():
                    current_node.left = current_node.right.leftChild

            elif current_node.left is not None:
                current_node.key = current_node.left.key
                current_node.val = current_node.left.value
                if current_node.left.has_right_child():
                    current_node.right = current_node.left.rightChild
                if current_node.left.has_left_child():
                    current_node.left = current_node.left.leftChild

    @staticmethod
    def _find_min(current_node):
        """
        :type current_node: TreeNode
        :param current_node:
        :return:
        """
        current_node = current_node.right
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
        pre_order(tree.left)
        pre_order(tree.right)


a = BST()


for i in range(100):
    a[i] = i

print(a[3])
a.delete(3)
print(a[3])
pre_order(a.root)
