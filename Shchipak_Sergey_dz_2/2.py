sample = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_sample = []
for value in sample:

    if value.isdigit():
        value.split()
        if len(value) == 1:
            value = '0' + value
        new_sample.append('"')
        new_sample.append(value)
        new_sample.append('"')
    elif value.startswith('+') or value.startswith('-'):
        value.split()
        if len(value) == 2:
            value = value[0] + '0' + value[1]
        new_sample.append('"')
        new_sample.append(value)
        new_sample.append('"')
    else:
        new_sample.append(value)
print(" ".join(new_sample))
