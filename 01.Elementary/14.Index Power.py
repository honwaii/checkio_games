def index_power(array,n):
    if n < len(array):
        return pow(array[n],n)
    else:
        return -1

print(index_power([1,2,3,4],0))