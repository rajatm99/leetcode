def isValid(s):
    l = []
    map = {
        ")":"(",
        "]":"[",
        "}": "{"
    }

    opening = ["(", "{", "["]
    for i in s :
        if len(l) == 0 :
            l.append(i)
        elif i in opening :
            l.append(i)
        elif map[i] == l[-1]:
            l.pop()
        else:
            return False
    return l == []

print(isValid("([])"))
        