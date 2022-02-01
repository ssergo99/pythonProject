with open('nginx_logs.txt', 'r', encoding='utf-8') as file_src:
    for content in file_src:
        list_of_add = (content.split(' ')[0], content.split(' ')[5].replace('"',""), content.split(' ')[6])
        print(list_of_add)
