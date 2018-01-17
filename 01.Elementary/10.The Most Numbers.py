def The_Most_Numbers(*args):
    numbers = [*args]
    if len(numbers) :
        min_number = min(numbers)
        max_number =max(numbers)
        return max_number - min_number
    else:
        return 0


def checkio2(*args):
    return (max(args) - min(args)) if (len(args) > 0) else 0
        # all(isinstance(x, (int, float)) for x in args: print(x))
        # print(all)

print(The_Most_Numbers())