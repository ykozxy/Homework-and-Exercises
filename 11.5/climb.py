def myfact(n):
    assert n >= 0, "Factorial not definied for negative values."
    if n < 2:
        return 1
    else:
        return n * myfact(n-1)


def climb(n):
    up = myfact(n)
    down = myfact(n-2)
    return up // down


print(climb(3))
