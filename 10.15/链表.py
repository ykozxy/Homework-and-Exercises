class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def printAll(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        while current != None:
            if item == current.getData():
                return True
            else:
                current = current.getNext()
        return False

    def remove(self,item):
        current = self.head
        prev = None
        found = False
        while not found:
            if item == current.getData():
                found = True
                break
            else:
                prev = current
                current = current.getNext()


        if found == False:
            return False

        if prev == None:
            self.head = self.head.getNext()
        else:
            prev.setNext(current.getNext())
        return True

mylist = LinkedList()
mylist.add(5)
mylist.add(4)
mylist.add(3)
print(mylist.remove(4))

mylist.printAll()
print(mylist.size())
print(mylist.search(4))
