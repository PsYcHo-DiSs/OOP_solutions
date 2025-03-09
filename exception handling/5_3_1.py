def input_int_numbers(values):
    try:
        output_res = tuple((int(elem) for elem in values))
    except:
        raise TypeError('все числа должны быть целыми')

    return output_res


while True:
    input_data = input().split()
    try:
        res = input_int_numbers(input_data)
    except TypeError:
        continue
    else:
        print(*res)
        break
