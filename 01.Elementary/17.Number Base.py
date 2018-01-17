# 就是转换成十进制，进制可以选择的范围是2～36，并用 0～9+A~Z来表示十进制以上的数.
def number_base(str_number, radix):
    str_number = list(str_number)
    number = 0
    for i in range(len(str_number)):
        each = str_number[len(str_number)-1-i]
        if 47 < ord(each) < 58:
            if int(each) < radix:
                number += int(each)*radix**i
            else:
                return -1
        else:
            if (ord(each)-55) < radix:
                number += (ord(each)-55) * radix ** i
            else:
                return -1
    return number


def number_base2(str_number, radix):
    alnum = "0123456789ABCDEFGHIJELMNOPQRSTUVWXYZ"
    sum = 0
    for index, n in enumerate(str_number):
        if alnum.index(n) >= radix:
            return -1
            break
        sum = sum + alnum.index(n) * radix ** (len(str_number) - index - 1)
    return sum

print(number_base("5",16))
