math = []
total = []
for i in range(20):
    a, b = map(int, input().split())
    math.append(a)
    total.append(b)
combine = list(zip(math, total))

# math
combine.sort()
for i in combine:
    print(i[0], i[1])

# total
temp = []
for i in combine:
    a = list(i)
    a.reverse()
    temp.append(a)
temp.sort()
for i in temp:
    print(i[0], i[1])
