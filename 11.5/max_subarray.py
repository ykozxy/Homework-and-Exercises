# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def add_lst(lst):
    sum1 = 0
    for num in lst:
        sum1 += num
    return sum1


def max_subarray(lst):
    maxnum = lst[0]
    for long in range(0, len(lst)):
        for position in range(0, len(lst)-long):
            sumnum = add_lst(lst[position: position + long])
            if sumnum > maxnum:
                maxnum = sumnum
    return maxnum


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# 优化到O(n)


