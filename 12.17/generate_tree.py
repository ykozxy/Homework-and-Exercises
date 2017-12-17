import turtle


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deserialize(lst):
    if lst is None:
        return None
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in lst]
    childs = nodes[::-1]
    root = childs.pop()
    for node in nodes:
        if node:
            if childs: node.left = childs.pop()
            if childs: node.right = childs.pop()
    return root


def draw_tree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

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


if __name__ == '__main__':
    draw_tree(deserialize([1, 2, 3, 4, 'null', 2, 4, 'null', 4]))
