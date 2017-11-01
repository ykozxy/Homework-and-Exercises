class ListNode:
    def __init__(self, item):
        self.data = item
        self.next = None


def circle_checker(head, replace_number='97129083764171'):

    h = head
    while h is not None:
        try:
            if h.data[0] == replace_number:
                return h.data[1]

        except TypeError or IndexError:
            data = h.data
            h.data = [replace_number, data]
            h = h.next

    return False


l1 = ListNode(0)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

print(circle_checker(l1))
