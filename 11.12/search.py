def sequential_search(lst, item):
    for i, j in enumerate(lst):
        if j == item:
            return i
    return False


def bin_search(lst, item):
    head = 0
    tail = len(lst) - 1
    mid = 0
    while head <= tail:
        mid = (head + tail) // 2
        if lst[mid] > item:
            tail = mid - 1
        elif lst [mid] < item:
            head = mid + 1
        else:
            return mid
    return None

lst = range(0, 10240000000000)

print(bin_search(lst, 1010000000))





'''
1024  10 ; 
O(lgN)
O(1) Hash search 
key: value
[54, 26, 93, 17, 77, 31]  mod 11

0  1 2 3 4  5  6  7 8 9  10 
77 0 0 0 26 93 17 0 0 31 54

hash_search(77):
    key = hash(77)  # = 0
    arr(0)

'''

