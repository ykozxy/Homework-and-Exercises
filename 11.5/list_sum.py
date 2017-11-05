def listsum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + listsum(lst[1:])


print(listsum([1, 2, 3, 4, 5]))

def fib_0(n):
    pos = 0
    a, b = 1, 1
    while pos < n:
        a, b = b, a + b
        pos += 1
    return a

count = 0
def fib(n):
    if n < 3:
        return 1
    else:
        global count
        count += 1
        return fib(n-1) + fib(n-2)

print(fib(10))

print(count)


def gcd(m, n):
    if m == 0:
        return n
    elif n == 0:
        return m
    else:
        if m <= n:
            return gcd(m, n-m)
        elif m > n:
            return gcd(n, m-n)


print(gcd(38, 56))


def han(num, x='x', y='y', z='z'):
    if num == 1:
        print(x, '->', z)
    else:
        han(num-1, x, z, y)
        han(1, x, y, z)
        han(num-1, y, x, z)

han(3)

