class Stack:
        def __init__(self):
            self.items=[]

        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def size(self):
            return len(self.items)


s1='()()'
s2='(()())('
s3=')('

def parChecker(str):
    s = Stack()
    try:
        for items in str:
            if items == '(':
                s.push('(')
            elif items == ')':
                if s.size() == 0:
                    return False
                else:
                    s.pop()
        if s.size() != 0:
            return False
        elif s.size() == 0:
            return True
    except:
        return 'error'

print (parChecker(str(input('Expression:'))))

