def findDigits(n):
    count = 0
    print(list(str(n)))
    for i in list(str(n)):
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count
