class ListNode:
    def __init__(self, item):
        self.data = item
        self.next = None

def listnode_add(listnode1, listnode2):
    temp = ListNode(0)
    result = temp
    excess = False

    while listnode1 != None and listnode2 != None:
        sum_node = listnode1.data + listnode2.data
        if excess:
            sum_node += 1
            excess = False
        if sum_node >= 10:
            sum_node -= 10
            excess = True

        temp.next = ListNode(sum_node)
        listnode1 = listnode1.next
        listnode2 = listnode2.next
        temp = temp.next

    return result.next

node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)

node2 = ListNode(8)
node2.next = ListNode(8)
node2.next.next = ListNode(8)

r_head = listnode_add(node1, node2)
head = r_head
while head != None:
    print(head.data)
    head = head.next
