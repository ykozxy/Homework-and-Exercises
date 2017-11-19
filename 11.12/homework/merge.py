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


def merge_sort(lst):
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
        for k in range(0, length, 2):
            clst1 = lst[k]
            clst2 = lst[k+1]
            split_list.pop(k)
            split_list[k] = sort_lst(clst1, clst2)

        if length_mod:
            split_list[-1] = sort_lst(split_list[-1], split_list[-2])
            split_list.pop(-2)

        cur_length += 1
        lst = split_list

    return split_list


print(merge_sort([1, 3, 2, 4, 3, 5]))
