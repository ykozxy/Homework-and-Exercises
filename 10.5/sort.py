def sort(str1, str2):

    alist = list(str2)
    pos = 0

    stillOK = True

    while pos < len(str1) and stillOK:
        pos2 = 0
        found = False

        while pos2 < len(alist) and not found:
            if str1[pos] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos += 1

    return stillOK

'''   
    for x in str1:
        find = False
        for y in str2:
            if x == y:
                find = True
                
                break
        if find:
            continue
        else:
            return False

    return True
'''
print (sort('aacd', 'dcaa'))

