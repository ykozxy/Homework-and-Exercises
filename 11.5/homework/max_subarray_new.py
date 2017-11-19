def max_subarray(lst):
    if lst == []:
        return None
    currmax, summax = lst[0], lst[0]

    for c in lst[1:]:
        currmax = max(c, currmax + c)
        summax = max(currmax, summax)

    return summax

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

'''
O(n)
O(lgN)
O(n**2)
O(2**n)

log2 记为 lg 

lg8 = 3
lg1024 = 10

#1  ([2, 5, 7, 11, 21, 24] , 13)  return : [2, 11]  O(n) ; 
'''