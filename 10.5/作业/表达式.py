class Par:
    def __init__(self):
        self.small = []
        self.middle = []
        self.large = []

    def isEmpty(self, type):
        if type == 'small':
            return self.small == []
        elif type == 'middle':
            return self.middle == []
        elif type == 'large':
            return self.large == []

    def push(self, type, item=0):
        if type == 'small':
            self.small.append(item)
        elif type == 'middle':
            self.middle.append(item)
        elif type == 'large':
            self.large.append(item)

    def pop(self, type):
        if type == 'small':
            return self.small.pop()
        elif type == 'middle':
            return self.middle.pop()
        elif type == 'large':
            return self.large.pop()

    def size(self, type):
        if type == 'small':
            return len(self.small)
        elif type == 'middle':
            return len(self.middle)
        elif type == 'large':
            return len(self.large)


def parcheck(expression):
    s = Par()

    # 朝向+数量+包含
    for character in expression:
        # ()
        if character == '(':
            if s.isEmpty('large') is False and s.isEmpty('middle'):
                return False
            else:
                s.push('small')
        elif character == ')':
            if s.isEmpty('small'):
                return False
            else:
                s.pop('small')
        # []
        elif character == '[':
            if s.isEmpty('small'):
                s.push('middle')
            else:
                return False
        elif character == ']':
            if s.isEmpty('middle'):
                return False
            else:
                s.pop('middle')
        # {}
        elif character == '{':
            if s.isEmpty('small') and s.isEmpty('middle'):
                s.push('large')
            else:
                return False
        elif character == '}':
            if s.isEmpty('large'):
                return False
            else:
                s.pop('large')

    return True


while True:
    try:
        print(parcheck(str(input('Expression:'))))
    except:
        print('Error!')
        break
