class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


'''
def ysf(namelist, num):
    list(namelist)
    q = Queue()
    turn = 0
    out = None
    while len(namelist) > 0:
        while turn < num:
            if q.size() <= len(namelist):
                q.enqueue(namelist[turn])
            elif q.size() > len(namelist):
                q.dequeue()
                
            out = q.dequeue()

            turn += 1

        print(out)
        namelist.remove(out)

    return str(namelist)

ysf(['a', 'b', 'c', 'd'], 3)

  d,c,b,a
  a,d,c,b
  b,a,d,c
  c,b,a,d

a, b, c, d, e
1, 2, 3, 4, 5 
6, 7
'''

def ysf(namelist, num):
    q = Queue()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        print(q.dequeue())

    return q.dequeue()


print(ysf(['A', 'B', 'C', 'D'], 7))
