class ListNode:
    def __init__(self, item):
        self.data = item
        self.next = None


def reverse(head):
    prev = None
    while head is not None:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev


def reverse_listnode(head, number):
    print(head.data)
    inverse_head = reverse(head)
    count = 0
    print(inverse_head.data)
    print(head.data)

    #  Count the number of objects in nodelist
    while head is not None:
        head = head.next
        count += 1
    # after this head is None
#    print(head.data)

    #  Create a new nodelist as the output
    current_count = 0
    result = ListNode(0)
    r_temp = result
    while current_count <= count - number:
        result.next = ListNode(head)
        result = result.next
        head = head.next
        current_count += 1
#    print(head.data)
#    print(inverse_head.data)
#    here inverse_head.data is 4 but inverse_head 4->3->2->1  1.next is None
    temp = inverse_head
    while temp is not None:
        print(temp.data)
        temp = temp.next

    while current_count <= count:
        print("******")
        r_temp.next = ListNode(inverse_head.data)
        r_temp = r_temp.next
        inverse_head = inverse_head.next
#        count += 1
        current_count += 1
    return result.next

nodelist1 = ListNode(1)
nodelist1.next = ListNode(2)
nodelist1.next.next = ListNode(3)
nodelist1.next.next.next = ListNode(4)

head = reverse_listnode(nodelist1, 2)
#head = reverse(nodelist1)
while head is not None:
    print(head.data)
    head = head.next
