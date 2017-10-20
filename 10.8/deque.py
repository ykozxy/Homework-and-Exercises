class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def palChecker(s):
    d = Deque()
    for cha in s:
        d.addFront(cha)

    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False

    return True

print(palChecker(str(input('Str:'))))


