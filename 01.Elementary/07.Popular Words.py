def popular_words(text, words):
    text = text.lower()
    print(text)
    words_count = {}
    for each in words:
        words_count[each] = text.count(each)
        if each not in text:
            words_count[each] = 0
        else:
            words_count[each] = text.count(each)
    return words_count

print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))
