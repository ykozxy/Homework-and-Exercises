class ListNode:
    def __init__(self, item):
        self.data = item
        self.next = None


def addList(l1, l2):
    temp = ListNode(0)
    result = temp
    while l1 != None and l2 != None:
        temp.next = ListNode(l1.data + l2.data)
        l1 = l1.next
        l2 = l2.next
        temp = temp.next
    return result.next

h1 = ListNode(3)
h1.next = ListNode(4)
h1.next.next = ListNode(5)

h2 = ListNode(6)
h2.next = ListNode(7)
h2.next.next = ListNode(8)

head = addList(h1, h2)
print(head.next.next.data)

'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

reverse(head, n)

Input: (2 -> 4 -> 3 ->5 -> 6 -> 4) , 3
Output: (2 -> 4 -> 3 ->4 -> 6 -> 5)
'''
