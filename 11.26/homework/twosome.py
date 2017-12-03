def two_some(lst, num):
    """

    :type lst: list
    :type num: int
    :param lst:
    :param num:
    :return:
    """

    small = 0
    big = len(lst) - 1
    output = []

    while small <= big:
        if lst[small] + lst[big] > num:
            big -= 1
        elif lst[small] + lst[big] < num:
            small += 1
        else:
            output.append([lst[small], lst[big]])
            small += 1
            big -= 1

    return output


print(two_some([1, 2, 3, 5, 8, 9, 10, 11, 12], 13))
