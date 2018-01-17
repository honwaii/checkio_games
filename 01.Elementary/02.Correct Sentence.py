def Correct_Sentence(text):
    text=text.capitalize()
    if (text[len(text)-1]) != '.':
        text = text+'.'
    print(text)

Correct_Sentence('text')