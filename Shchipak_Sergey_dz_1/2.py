qubes = []
up_seven = []
up_seventeen = []
ind = 1
sum7 = 0
sum7_plus17 = 0
while ind <= 1000:
    if ind%2 != 0:
        qube = ind ** 3
        qube_plus17 = qube + 17
        dig1 = qube%10
        dig2 = (qube % 100)//10
        dig3 = (qube % 1000) // 100
        dig4 = (qube % 10000) // 1000
        dig5 = (qube % 100000) // 10000
        dig6 = (qube % 1000000) // 100000
        dig7 = (qube % 10000000) // 1000000
        dig8 = (qube % 100000000) // 10000000
        dig9 = (qube % 1000000000) // 100000000
        # далее блок кода для задания "с", вариант "b" предполагает более простой вариант с добавлением в еще один список значений плюс 17 на каждом положительном прохождении цикла
        dig1_plus17 = qube_plus17%10
        dig2_plus17 = (qube_plus17 % 100)//10
        dig3_plus17 = (qube_plus17 % 1000) // 100
        dig4_plus17 = (qube_plus17 % 10000) // 1000
        dig5_plus17 = (qube_plus17 % 100000) // 10000
        dig6_plus17 = (qube_plus17 % 1000000) // 100000
        dig7_plus17 = (qube_plus17 % 10000000) // 1000000
        dig8_plus17 = (qube_plus17 % 100000000) // 10000000
        dig9_plus17 = (qube_plus17 % 1000000000) // 100000000
        sum_dig = dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8 + dig9
        sum_dig_plus17 = dig1_plus17 + dig2_plus17 + dig3_plus17 + dig4_plus17 + dig5_plus17 + dig6_plus17 + dig7_plus17 + dig8_plus17 + dig9_plus17
        if sum_dig%7 == 0:
            up_seven.append(qube)
            sum7 += qube
# далее блок кода для задания "с"
        if sum_dig_plus17 % 7 == 0:
            up_seventeen.append(qube_plus17)
            sum7_plus17 += qube_plus17
        qubes.append(qube)
        ind += 1
    else:
        ind += 1
print(qubes)
print (up_seven)
print (up_seventeen)
print (sum7)
print (sum7_plus17)
