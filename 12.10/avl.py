class Node:

    def __init__(self, value, root=False):
        self.value = value if not root else None
        self.is_root = root
        self.parent = None
        self.left = None
        self.right = None

    @property
    def balance(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return right_height - left_height

    @property
    def height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return 1 + max(left_height, right_height)

    @property
    def grandpa(self):
        if self.parent:
            return self.parent.parent
        else:
            return None

    def insert(self, value):
        if self.value is None or value > self.value:
            if self.right is None:
                self.right = Node(value, root=False)
                self.right.parent = self
                self.right.balance_grandpa()
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = Node(value, root=False)
                self.left.parent = self
                self.left.balance_grandpa()
            else:
                self.left.insert(value)

    def balance_grandpa(self):
        if self.grandpa and self.grandpa.is_root:
            pass
        elif self.grandpa and not self.is_root:
            self.grandpa._balance()
        else:
            pass
        return

    def _balance(self):
        if self.balance > 1:
            if self.right.balance < 0:
                self._rl_case()
            elif self.right.balance > 0:
                self._rr_case()
        elif self.balance < -1:
            if self.left.balance < 0:
                self._ll_case()
            elif self.left.balance > 0:
                self._lr_case()

    def _ll_case(self):
        child = self.left
        if self.parent.is_root or self.value > self.parent.value:
            self.parent.right = child
        else:
            self.parent.left = child

        child.parent, self.parent = self.parent, child
        child.right, self.left = self, child.right

    def _lr_case(self):
        pass

    def _rl_case(self):
        pass

    def _rr_case(self):
        pass


values = [5, 3, 2]
root = Node(None, root=True)
for i in values:
    root.insert(i)

print(root.right.left.value)
