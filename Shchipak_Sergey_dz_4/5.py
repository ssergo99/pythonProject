def utils_cur(argv):
    program, args = argv
    from requests import get, utils
    from datetime import datetime
    i = 0
    tag_find = 0
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency_str = content.split('</Value></Valute>')
    while i < len(currency_str):
        if currency_str[i].find(args.upper()) != -1:
            tag_find = 1
            print("Курс  1 " + args.upper() + " =", (float((currency_str[i].split('>')[-1]).replace(',', '.'))),
                  "рублей")
            print("На дату:  ", ((datetime.strptime(currency_str[0].split('"')[5], '%d.%m.%Y')).date()))
            break
        else:
            i += 1
    if tag_find != 1:
        return None

if __name__ == '__main__':
    import sys

    exit(utils_cur(sys.argv))
