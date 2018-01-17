def most_frequent(data):
    frequent = {}
    items = list(set(data))
    print(items)
    for each in items:
        frequent[each] = data.count(each)
    print(frequent)
    frequent = dict(zip(frequent.values(), frequent.keys()))
    print(frequent)
    return frequent[max(frequent.keys())]


def most_frequent2(data):
    return sorted(data, key=data.count)[-1]    # 注意此处count 的使用，关键字的应用

print(most_frequent2([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))