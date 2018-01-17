def best_stock():
    data = { 'CAC': 91.1,'ATX': 1.01, 'TASI': 120.9}
    keys = list(data.keys())
    for each_stock in keys:
        if data[each_stock] == max(data.values()):
            print(each_stock)

best_stock()
