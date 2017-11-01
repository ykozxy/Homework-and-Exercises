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


def sort_ln(head):
    h = head
    odd = []
    even = []

    while h is not None:
        if int(h.data) % 2 == 0:
            even.append(h.data)
            print('even', even)
        else:
            odd.append(h.data)
            print('odd', odd)
        h = h.next

    odd.extend(even)
    return build_list(odd)


l1 = build_list([1, 2, 2, 2, 3, 3, 4, 5, 5, 6])
print_all(sort_ln(l1))
