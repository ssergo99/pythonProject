import re

pars_result = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_src:
    content = file_src.readlines()[int(input('Введите номер строки для проведения парсинга   '))]
    pars_result.setdefault('remote_addr', (re.search(r'(?:[0-9a-z]*[.:]){3,7}[0-9a-z]*', content)).group(0))
    pars_result.setdefault('request_datetime', (re.search(r'[0-9]{2}[/][A-Za-z]*[/]\d{4}(:[\d]{2}){3}\s[+][0]{4}',
                                                          content)).group(0))
    pars_result.setdefault('request_type', (re.search(r'[A-Z]{3,4}', content)).group(0))
    pars_result.setdefault('requested_resource', (re.search(r'([/][a-z_0-9]+){2}', content)).group(0))
    pars_result.setdefault('response_code', (re.search(r'\d{3}\s[0-9]+', content).group(0)).split(' ')[0])
    pars_result.setdefault('response_size', (re.search(r'\d{3}\s[0-9]+', content).group(0)).split(' ')[1])
    print(pars_result)
