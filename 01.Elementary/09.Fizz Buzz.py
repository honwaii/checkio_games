def checkio(number):
    if (not(number % 3)) and (not (number % 5)):
        return 'Fizz Buzz'
    elif not (number % 3):
        return 'Fizz'
    elif not (number % 5):
        return 'Buzz'
    else:
        number = str(number)
        return number


print(checkio(6))