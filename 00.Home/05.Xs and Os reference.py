def XS_and_OS_reference():
    result = ['X.O','XO.','.X.']
    temp = ' '.join(result)+' '
    for i in range(0,12,4):
        temp += temp[i]
    temp+=' '
    for i in range(1,12,4):
        temp += temp[i]
    temp += ' '
    for i in range(2,12,4):
        temp += temp[i]
    temp += ' '
    for i in range(0, 12, 5):
        temp += temp[i]
    temp += ' '
    for i in range(2, 12, 3):
        temp += temp[i]
    temp += ' '

    if 'XXX'in temp:
        print('x')
    elif 'OOO' in temp:
        print('O')
    else:
        print('D')
    print(temp)

XS_and_OS_reference()
