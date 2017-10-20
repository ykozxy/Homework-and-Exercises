class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)


    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def pal_checker(s):
    d = Deque()
    for cha in s:
        d.addFront(cha)

    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False

    return True


def long_pal(string):
    current_lenth = len(string)
    current_location = 0

    while current_lenth > 1 and current_location + current_lenth <= len(string):
        current_str = string[current_location: current_lenth + current_location]
        is_pal = pal_checker(current_str)

        if is_pal:  # correct
            return current_lenth, current_str

        else:  # incorrect
            if current_location + current_lenth == len(string):  # arrive the end
                current_location = 0
                current_lenth -= 1

            else:  # in the middle
                current_location += 1

    return 1, string[0]


while True:
    instr = str(input('String:'))
    try:
        print('Result:', long_pal(instr)[0], ' ', long_pal(instr)[1])
    except IndexError:
        print('The string cannot be empty!!!')
        break
