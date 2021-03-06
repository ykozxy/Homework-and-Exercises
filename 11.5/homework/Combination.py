def combination(total, length):
    output = []

    if length == 1:
        output = list(range(1, total + 1))
        output2 = []
        for elements in output:
            output2.append(list(elements))
        return output2

    elif total < length:
        return 'Error'

    for first in range(1, total-length+2):
        input_list = list(range(1, total+1))
        current_position = 0
        sub_output = []

        # pop all the element before "first"
        pop_position = 1
        while pop_position < first:
            input_list.pop(0)
            pop_position += 1

        while len(sub_output) <= length:
            while current_position < (len(input_list) - 1):
                sub_output.append(input_list[current_position])  # append an element to the sub-output
                current_position += 1
                print(sub_output)

                #  check whether the length of sublist == the length input at the beginning
                jump_out = False
                if len(sub_output) == length:
                    jump_out = True
                    break

            #  If the length of sub-list == input, jump out of "while"
            if jump_out:
                break

            current_position = 0
            input_list.pop(0)
            print('------------------------')

        # check if there has already exist a same list in the output
        if sub_output in output:
            continue
        else:  # if not, add sub-output into the output list
            output.append(sub_output)

    return output


def ncr(a, b):
    def myfact(n):
        assert n >= 0, "Factorial not defined for negative values."
        if n < 2:
            return 1
        else:
            return n * myfact(n - 1)

    up = myfact(a)
    down = myfact(b) * myfact(a-b)
    return up // down


def combination_new(n, r):
    import random
    outcome = []
    current_location = 0
    all_round = ncr(n, r)

    while len(outcome) < all_round:
        sublist = []
        while current_location < r:
            while True:
                ren_number = random.randrange(1, n+1)
                if ren_number not in sublist:
                    break
            sublist.append(ren_number)
            current_location += 1

        sublist.sort()
        current_location = 0
        #  Check is the list has already existed.
        if sublist in outcome:
            continue
        else:
            outcome.append(sublist)

    outcome.sort()
    return outcome


def combination_rec(n, r):
    if n == r:
        sub_list = []
        for i in range(1, r+1):
            sub_list.append(i)
        return [sub_list]

    elif r == 1:
        sub_list = []
        for i in range(1, n+1):
            sub_list.append([i])
        return sub_list

    else:
        sub_list = combination_rec(n-1, r)
        ad = combination_rec(n-1, r-1)
        for each in ad:
            each.append(n)
        return sub_list + ad


print(combination_rec(5, 3))

'''(3,2)  [1,2] [1,3] [2,3]
(3,1) [[1,4],[2,4],[3,4]]
c(n,k ) = c(n-1, k) + c(n-1, k-1 ).append(n)'''