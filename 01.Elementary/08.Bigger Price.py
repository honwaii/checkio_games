def bigger_price(limit, data):
    item = {}
    it = []
    most_expensive = {}
    all_expensive = []
    for each in data:
        item[each['price']] = each['name']
    price = (list(item.keys()))
    price.sort(reverse=True)
    # print(item)
    for i in range(limit):
        most_expensive_price = price[i]
        most_expensive['name'] = item[most_expensive_price]
        most_expensive['price'] = most_expensive_price
        all_expensive.append(most_expensive.copy())
    print(all_expensive)


def bigger_price2(limit, data):
    sorted_data = sorted(data, key=(lambda x: x['price']), reverse=True)
    print(sorted_data[0:limit])


bigger_price2(2, [{"price": 100, "name": "bread"}, {"price": 138, "name": "wine"}, {"price": 15, "name": "meat"},
    {"price": 1, "name": "water"}])
