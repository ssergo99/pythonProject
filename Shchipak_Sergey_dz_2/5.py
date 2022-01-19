prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
str_price = ''
idx = 0
print(id(prices))
prices.sort()

print(id(prices))
down_price = prices.copy()
down_price.reverse()

for value in prices:
    if type(value) == float:
        value1000 = value * 1000
        rub = int(value)
        kop = (value1000 - rub * 1000) / 10
        if rub < 10:
            if kop < 10:
                price = '0%s руб 0%d коп' % (rub, kop)
            price = '0%s руб %d коп' % (rub, kop)
        elif kop < 10:
            price = '%s руб 0%d коп' % (rub, kop)
        else:
            price = '%s руб %d коп' % (rub, kop)
    else:
        price = '%s руб 00 коп' % value
    if len(str_price) == 0:
        str_price = str_price + price
    else:
        str_price = str_price + ", " + price

print(str_price)

print('Цены 5 самых дорогих товаров:')
for i in down_price:
    if idx == 5:
        break
    print(i)
    idx += 1
