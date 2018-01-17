def first_word(text):
    word1 = text.split(' ')
    word = []
    for each in word1:
        split_word = list(each)
        for each_alpha in split_word:
            if each_alpha.isalpha():
                word.append(each_alpha)
            elif (each_alpha == '\'')and(len(word)):
                word.append(each_alpha)
            elif not (each_alpha.isalpha() and (len(word))):
                break
            else:
                continue
        if len(word):
            break
    print(''.join(word))


first_word(" hello.word ")

