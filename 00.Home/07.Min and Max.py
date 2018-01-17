def min(*args, **kwargs):
    print(args)
    if isinstance(args[0],int):
        numbers = sorted(args,reverse=True)
        return numbers[0]
    elif isinstance(args[0],str):
        # print(list(args[0]))
        alpha = sorted(list(args[0]), key=lambda x:ord(x))
        return alpha[0]
    elif isinstance(args[0],float):
        

    # key = kwargs.get("key", None)
    # return numbers[0]


def max(*args, **kwargs):
    numbers = args
    # key = kwargs.get("key", None)
    return numbers


print(min('hello'))