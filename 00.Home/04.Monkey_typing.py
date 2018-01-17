import re
def monkey_typing():
    text=input('the text:')
    text=text.lower()
    words=input('the words:')
    words=set(words.split(', '))
    m=0
    for item in words:
        if item in text:
            m+=1
    print(m)

monkey_typing()

#The best solution ^-^ ^_^
def count_words(text, words):
    return sum(w in text.lower() for w in words)
