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
    child = nodes[::-1]
    root = child.pop()
    for node in nodes:
        if node:
            if child: node.left = child.pop()
            if child: node.right = child.pop()
    return root


def draw_tree(root):
    def height(head):
        return 1 + max(height(head.left), height(head.right)) if head else -1

    def jump_to(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jump_to(x, y - 20)
            t.write(node.val, align='center')
            draw(node.left, x - dx, y - 60, dx / 2)
            jump_to(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jump_to(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    draw_tree(deserialize([1, 2, 3, 4, 'null', 2, 4, 'null', 4]))
