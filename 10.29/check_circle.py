from Remove import ListNode, build_list


def check_circle_0(head):
    if head is None:
        return False
    head.data = 31415926
    head = head.next
    while head is not None:
        if head.data == 31415926:
            return True
        else:
            head.data = 31415926
        head = head.next
    return False


def check_circle(head):
    slow = head
    fast = head

    if head is None:
        return False

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


l1 = ListNode(0)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l4

print(check_circle(l1))
'''start?'''
