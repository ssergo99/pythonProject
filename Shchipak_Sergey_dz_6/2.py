list_of_trace = []
list_of_ip = {}
max_ip = 0
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_src:
    for content in file_src:
        list_of_trace.append((content.split(' ')[0]))
    for ip in list_of_trace:
        count_ip = 1
        if list_of_ip.get(ip):
            count_ip = list_of_ip.get(ip) + 1
        count_of_ip = {ip: count_ip}
        list_of_ip.update(count_of_ip)
        if count_ip > max_ip:
            ip_with_max = ip
            max_ip = count_ip
    print(f"Адрес спамера {ip_with_max}, с него пришло максимальное число запросов: {max_ip}")
