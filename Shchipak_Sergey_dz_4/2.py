def currency_rates(cur_tag):
    from requests import get, utils
    i = 0
    tag_find = 0
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency_str = content.split('</Value></Valute>')

    while i < len(currency_str):
        if currency_str[i].find(cur_tag.upper()) != -1:
            tag_find = 1
            print(float((currency_str[i].split('>')[-1]).replace(',', '.')))
            break
        else:
            i += 1
    if tag_find != 1:
        print(None)


print("Курс доллара: "), currency_rates("USD")
print("Курс евро: "), currency_rates("EUR")
currency_rates(input('Введите код валюты для вывода курса:  '))
