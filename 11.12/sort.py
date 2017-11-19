def paopao_sort(lst):
    index = 0
    while index < len(lst)-1:
        if lst[index] > lst[index + 1]:
            lst[index], lst[index + 1] = lst[index +1], lst[index]
            index = 0
            continue
        index += 1
    return lst


def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        now = lst[0]
        former = []
        after = []
        equal = []
        # lst.pop(0)
        for i in lst:
            if i < now:
                former.append(i)
            elif i > now:
                after.append(i)
            else:
                equal.append(i)
        return quick_sort(former) + equal + quick_sort(after)


lst = [23, 45, 12, 5, 21, 13, 1, 2, 4, 2, 1, 3, 4, 7, 45]
print(quick_sort(lst))

'''
[12, 5, 21, 13, 1, 2, 4, 2, 1, 3, 4, 7]
23
[45, 45]


quick_sort()

O(nlgn)

分而治之 
'''
