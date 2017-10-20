from ListNode import ListNode


def reverse(head):
    prev = None
    while head != None:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev



h1 = ListNode(3)
h1.next = ListNode(4)
h1.next.next = ListNode(5)

r_head = reverse(h1)
head = r_head
while head != None:
    print(head.data)
    head = head.next