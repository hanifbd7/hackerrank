def pangrams(s):
    s = s.lower()
    a = "abcdefghijklmnopqrstuvwxyz"
    j = 0
    for i in range(0,len(a)):
        if a[i] in s and j <= 26:
            j += 1
        if j == len(a):
            break
    if j == 26:
        return("pangram")
    else:
        return("not pangram")
