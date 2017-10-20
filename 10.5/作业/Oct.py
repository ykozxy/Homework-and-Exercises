class stack:
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

def oct(num):
    if num == 0:
        return 0
    s = stack()
    while num > 0:
        remain = num % 8
        num //= 8
        s.push(remain)
    output = ''
    while s.isEmpty() is False:
        output += str(s.pop())
    return int(output)

while True:
    try:
        print(oct(int(input('Number:'))))
    except ValueError:
        print('Error')
        break
