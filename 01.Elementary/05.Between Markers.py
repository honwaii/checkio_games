# Python find()方法
# Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    strings = list(text)
    begin = list(begin)
    end = list(end)
    start_position = 0
    end_position = 0
    # 获取开始的位置
    if (''.join(begin)) in (''.join(strings)):
        for i in range(len(text)):
            if strings[i] == begin[0]:
                if strings[i:(i + len(begin))] == begin:
                    start_position = i + len(begin)
                    break
                else:
                    continue
            else:
                continue
    else:
        start_position = 0

    # 获取结束的位置
    if (''.join(end)) in (''.join(strings)):
        for i in range(len(text)):
            if strings[i] == end[0] and (i > start_position):
                if strings[i:(i + len(end))] == end:
                    end_position = i
                    break
                else:
                    continue
            else:
                continue
    else:
        end_position = len(strings)

    if end_position < start_position:
        return ''
    else:
        # print(start_position,end_position)
        print(strings[start_position:end_position])
        return ''.join(strings[start_position:end_position])


# 简洁的程序

def between_markers2(text: str, begin: str, end: str) -> str:
    start = 0
    if begin in text:
        start = text.find(begin) + len(begin)
    if end in text:
        endspot = text.find(end)
    else:
        endspot = len(text)

    return text[start:endspot]


print(between_markers('No [b]hi', '[b]', '[/b]'))
print(between_markers2('No [b]hi', '[b]', '[/b]'))
