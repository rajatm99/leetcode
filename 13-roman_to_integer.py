def romanToInt(s):
    r = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    l = 0
    num = 0
    for i in range(len(s)-1, -1, -1):
        if r[s[i]] >= l :
            num += r[s[i]]
            l = r[s[i]]
        else :
            num -= r[s[i]]
    return num

print(romanToInt("LVIII"))