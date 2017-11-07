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

                #  check whether the length of sub-list == the length input at the beginning
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


print(combination(4, 2))
