def even_the_last(array):
    sum1 = 0
    if len(array):
        for i in range(len(array)):
            if i % 2 == 0:
                sum1 += array.index(i)
        sum1 = sum1 * array[len(array)-1]  # array[-1]
        return sum1
    else:
        return 0
    # print(sum)


print(even_the_last([0, 1, 2, 3, 4, 5]))