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


def multi(num1, num2):
    return int(num1 * num2 / gcd(num1, num2))


n1, n2 = int(input()), int(input())
print(gcd(n1, n2), multi(n1, n2))
