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

    def _put(self, key, value, currentNode):
        """
        :type currentNode: TreeNode
        :param key:
        :param value:
        :param currentNode:
        :return:
        """
        if key < currentNode.key:
            if currentNode.has_left_child():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChile = TreeNode(key=key, val=value, parent=currentNode)
        else:
            if currentNode.has_right_child():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

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

    def _remove(self, currentNode):
        """
        :type currentNode: TreeNode
        :param currentNode:
        :return:
        """
        if currentNode.is_leaf():
            if currentNode == currentNode.parent.leftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.has_both_children():
            smallest_node = self._find_min(currentNode)
            assert smallest_node is TreeNode
            currentNode.key = smallest_node.key
            currentNode.value = smallest_node.value

            if smallest_node.rightChild.key < smallest_node.parent.key:
                smallest_node.parent.leftChild = smallest_node.rightChild
            else:
                smallest_node.parent.rightChild = smallest_node.rightChild

        else:
            if currentNode.rightChild is not None:
                currentNode.key = currentNode.rightChild.key
                currentNode.value = currentNode.rightChild.value
                if currentNode.rightChild.has_right_child():
                    currentNode.rightChild = currentNode.rightChild.rightChild
                if currentNode.rightChild.has_left_child():
                    currentNode.leftChild = currentNode.rightChild.leftChild

            elif currentNode.leftChild is not None:
                currentNode.key = currentNode.leftChild.key
                currentNode.value = currentNode.leftChild.value
                if currentNode.leftChild.has_right_child():
                    currentNode.rightChild = currentNode.leftChild.rightChild
                if currentNode.leftChild.has_left_child():
                    currentNode.leftChild = currentNode.leftChild.leftChild

    def _find_min(self, currentNode):
        """
        :type currentNode: TreeNode
        :param currentNode:
        :return:
        """
        currentNode = currentNode.rightChild
        while currentNode.leftChild is not None:
            currentNode.leftChild.parent = currentNode
            currentNode = currentNode.leftChild
        return currentNode


a = BST()
# a[3] = 'hi'
# a[6] = 'hoho'

for i in range(100):
    a[i] = i

print(a[76])
