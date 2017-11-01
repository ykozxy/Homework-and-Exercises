class ListNode:
    def __init__(self, item):
        self.data = item
        self.next = None


def print_all(head):
    s = ""
    r = head
    while r is not None:
        s += str(r.data) + '->'
        r = r.next
    print(s)


def build_list(lst):
    head = ListNode(lst[0])
    r = head
    for i in lst[1:]:
        r.next = ListNode(i)
        r = r.next
    return head


def reverse(head):
    prev = None
    while head is not None:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev


def remove_d(h):
    head = h
    prev = None
    if head is None:
        return None
    while head.next is not None:
        prev = head
        head = head.next
        if prev.data == head.data:
            prev.next = head.next

    return h


def remove_all(h):
    """1,2,2,3,3,4 --> 1,4"""
    pass


l = None
print_all(l)
remove_d(l)
print_all(l)
