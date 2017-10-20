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
    inverse_head = reverse(head)
    count = 0

    #  Count the number of objects in nodelist
    while head is not None:
        head = head.next
        count += 1

    #  Create a new nodelist as the output
    current_count = 0
    result = ListNode(0)
    while current_count <= count - number:
        result.next = ListNode(head)
        result = result.next
        head = head.next
        current_count += 1

    while current_count <= count:
        result.next = ListNode(inverse_head)
        result = result.next
        inverse_head = inverse_head.next
        count += 1

    return result.next

nodelist1 = ListNode(1)
nodelist1.next = ListNode(2)
nodelist1.next.next = ListNode(3)
nodelist1.next.next.next = ListNode(4)

head = reverse_listnode(nodelist1, 2)

while head is not None:
    print(head.data)
    head = head.next
