def absolute_sorting(numbers_array):
    return sorted(list(numbers_array),key= lambda x:abs(x))


print(absolute_sorting((-20, -5, 10, 15)))
