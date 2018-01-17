def secret_message(text):
    message = []
    if len(text):
        text = list(text)
        for each in text:
            if each.isupper():
                message.append(each)
            else:
                continue
        return ''.join(message)
    else:
        return ''


def secret_message2(text):
    wielkie_litery = [literka for literka in text if literka.isupper()]
    kod=""
    return kod.join(wielkie_litery)


print(secret_message('HELLO WORLD!'))
