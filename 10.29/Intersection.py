from Remove import ListNode, build_list

def intersection(head1, head2):
    h1 = head1
    h2 = head2
    while h1 is not h2:
        h1 = head2 if h1 is None else h1.next
        h2 = head1 if h2 is None else h2.next
    return h1

l1 = ListNode(0)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4

r1 = ListNode(4)
r1.next = l3

print(intersection(l1,r1).data)


