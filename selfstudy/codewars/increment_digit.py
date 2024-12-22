def increment_string(strng: str):
    if strng.isalpha() or not strng:
        return strng + "1"
    if strng.isnumeric():
        num = int(strng) + 1
        return f"%0{len(strng)}d" % num
    n = len(strng)-1
    for i in range(0, -(len(strng)), -1):
        if strng[n].isdigit():
            n -= 1
        elif strng[i:] == "9" * (-i):
            num = int(strng[n+1:]) + 1
            incr = f"%0{1-i}d" % num
            strng = strng[:n+1]+incr
            return strng
        else:
            num = int(strng[n+1:]) + 1
            incr = f"%0{-i}d" % num
            return strng[:n+1]+incr


print(increment_string('R0481608749'))
