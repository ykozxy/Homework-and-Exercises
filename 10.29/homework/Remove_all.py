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


def remove_all(head):
    h = head
    prev = None
    prev2 = None

    if h is None:
        return None

    found_dul = False
    while h.next is not None:
        if found_dul is False:
            prev2 = prev
        prev = h
        h = h.next

        if h.data == prev.data:
            found_dul = True

            if h.next.data != prev2.next.data:
                found_dul = False
                prev2.next = h.next

    return head


l1 = build_list([1, 2, 2, 2, 3, 3, 4, 5, 5, 6])
print_all(remove_all(l1))
