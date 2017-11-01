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


def is_palindrome(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    if fast is None:
        z = reverse(slow)
    else:
        z = reverse(slow.next)
    while z is not None:
        if z.data != head.data:
            return False
        z = z.next
        head = head.next
    return True


def main():
    in_lst = input("input list: ")
    lst = [x for x in in_lst.split()]
    head = build_list(lst)
    print_all(head)
    print(is_palindrome(head))

if __name__ == main():
    main()