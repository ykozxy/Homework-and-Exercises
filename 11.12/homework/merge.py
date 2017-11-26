def sort_lst(lst1, lst2):
    if type(lst1) is int:
        lst1 = [lst1]
    if type(lst2) is int:
        lst2 = [lst2]

    len1 = len(lst1)
    len2 = len(lst2)
    if len1 > len2:
        lst1, lst2 = lst2, lst1

    current_location = 0
    for element in lst1:
        while current_location < len(lst2):
            if element <= lst2[current_location]:
                lst2.insert(current_location, element)
                break
            else:
                current_location += 1
    return lst2


def sort_list(lst1, lst2):
    if type(lst1) is int:
        lst1 = [lst1]
    if type(lst2) is int:
        lst2 = [lst2]

    final_lst = []

    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] >= lst2[0]:
            final_lst.append(lst2.pop(0))
        else:
            final_lst.append(lst1.pop(0))
    if len(lst1) != 0:
        final_lst += lst1
    elif len(lst2) != 0:
        final_lst += lst2

    return final_lst


def merge_sort_0(lst):
    length = len(lst)
    split_list = []

    # split
    for each in lst:
        split_list.append(each)

    # combine
    length_mod = length % 2
    length -= length_mod

    cur_length = 2
    while (2 * cur_length) <= length:
        length = len(lst)
        length_mod = length % 2
        length -= length_mod
        for k in range(0, length, 2):
            print(k, len(lst))
            clst1 = lst[k]
            clst2 = lst[k+1]
            split_list.pop(k//2)
            split_list[k//2] = sort_list(clst1, clst2)

        if length_mod:
            split_list[-1] = sort_list(split_list[-1], split_list[-2])
            split_list.pop(-2)

        cur_length += 1
        lst = split_list

    return split_list

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        l = merge_sort(left)
        r = merge_sort(right)
        return sort_list(l, r)
    else:
        return lst

lst = [1, 3, 2, 4, 3, 5, 4]

print(merge_sort_0(lst))
# print(sort_list([1, 2, 5, 8], [0, 1, 2, 3, 4]))