def bst(num):
    value = [1, 1]
    for i in range(num):
        value.append(0)

    for i in range(2, num+1):
        for j in range(1, i+1):
            value[i] += value[j-1] * value[i-j]

    return value[num]


print(bst(4))
