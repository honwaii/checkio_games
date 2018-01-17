def second_index(text, symbol):
    strings = list(text)
    flag = 0
    print(strings)
    for i in range(len(strings)):
       # print(i)
        if strings[i] == symbol:
            flag+=1
            if flag == 2:
                print(i)
                break
            else :
                continue
    if flag < 2:
        print("None")


second_index('a string for testing', 'n')

