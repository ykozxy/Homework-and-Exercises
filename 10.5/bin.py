class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def bin(num):
    s = Stack()
    while num > 0:
        remain = num % 2
        num //= 2
        s.push(remain)
    output = []
    while s.isEmpty() is False:
        output.append(s.pop())
    return str(output)

print (bin(int(input('Number:'))))
