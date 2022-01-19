sample = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_string = ''
for value in sample:
    if value.isdigit():
        value.split()
        if len(value) == 1:
            value = '0' + value
        value = '"' + value + '"'
    elif value.startswith('+'):
        value.split()
        if len(value) == 2:
            value = value[0] + '0' + value[1]
        value = '"' + value + '"'
    elif value.startswith('-'):
        value.split()
        if len(value) == 2:
            value = value[0] + '0' + value[1]
        value = '"' + value + '"'
    new_string += value
    new_string += ' '
print(new_string)
