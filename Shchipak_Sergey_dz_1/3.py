ind = 1
while ind <= 100:
    dig1 = ind % 10
    dig2 = (ind % 100) // 10
    dig3 = (ind % 1000) // 100

    if dig2 == 1 or dig1 == 0:
        print(ind, "процентов")
    elif dig1 == 1:
        print(ind, "процент")
    elif dig1 == 2 or dig1 == 3 or dig1 == 4:
        print(ind, "процента")
    elif dig1 == 5 or dig1 == 6 or dig1 == 7 or dig1 == 8 or dig1 == 9:
        print(ind, "процентов")
    ind += 1
