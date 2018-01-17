def three_words(words):
    words = words.split()
    print(words)
    if len(words) > 2:
        for i in range(len(words)-2):
            if words[i].isalpha() and words[i+1].isalpha() and words[i+2].isalpha():
                return True
            else:
                continue
        return False
    else :
        return False


print(three_words('one two 3 '))

