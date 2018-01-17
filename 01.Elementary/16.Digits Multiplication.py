def digits_multiplication(number):
    number = list(str(number))
    result = 1
    for i in range(len(number)):
        if int(number[i]) != 0:
            result *= int(number[i])
        else:
            continue
    return result


print(digits_multiplication(1034))