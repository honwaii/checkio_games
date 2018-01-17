def right_to_left(phrases):
    phrases =','.join(phrases)
    phrases = phrases.replace("right","left")
    print(phrases)


right_to_left(("left", "right", "left", "stop"))
