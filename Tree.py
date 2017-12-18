import turtle


class TreeNode(object):
    def __init__(self, *args, left=None, right=None, parent=None):
        assert len(args) <= 2, 'Too many arguments!!'
        if len(args) == 1:
            self.val = args[0]
        else:
            self.key, self.val = args
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
                current_node.leftChile = TreeNode(key, value, parent=current_node)
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


# Generate and output Tree
def draw_tree(root):
    """
    This function can use turtle to draw a binary tree
    :type root:TreeNode
    :param root:
    :return:
    """

    def height(head):
        return 1 + max(height(head.left), height(head.right)) if head else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center')
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


def serialize(node):
    """
    This function can turn a binary tree into a list
    :type node:TreeNode
    :param node:
    :return:
    """

    def doit(head):
        if head:
            vals.append(str(head.val))
            doit(head.left)
            doit(head.right)
        else:
            vals.append('null')

    vals = []
    doit(node)
    return vals


def deserialize(lst):
    """
    This function can turn a formatted list into a binary tree
    :type lst: list
    :param lst:
    :return:
    """
    if lst is None:
        return None
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in lst]
    childs = nodes[::-1]
    root = childs.pop()
    for node in nodes:
        if node:
            if childs:
                node.left = childs.pop()
            if childs:
                node.right = childs.pop()
    return root


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


def pre_order(tree):
    """

    :type tree: TreeNode
    """
    if tree is not None:
        print(tree.val)
        pre_order(tree.left)
        pre_order(tree.right)


def post_order(tree):
    """
    :type tree: TreeNode
    :param tree:
    :return:
    """
    if tree is not None:
        pre_order(tree.left)
        pre_order(tree.right)
        print(tree.val)


def in_order(tree):
    """
    :type tree: TreeNode
    :param tree:
    :return:
    """
    if tree is not None:
        pre_order(tree.left)
        print(tree.val)
        pre_order(tree.right)


# Relevant operation of sorting trees
def merge_tree(tree1, tree2):  # todo: This function has some issues
    """
    :type tree1: TreeNode
    :type tree2: TreeNode
    """
    if tree1 is None:
        return tree2
    elif tree2 is None:
        return tree1
    else:
        r = TreeNode(tree1.val + tree2.val)
        r.leftChild = merge_tree(tree1.left, tree2.left)
        r.rightChild = merge_tree(tree1.right, tree2.right)
        return r


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



if __name__ == '__main__':
    pass
