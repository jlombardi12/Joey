mystery_int = 7
s = 0
if mystery_int < 0:
    while mystery_int < 0:
        s = mystery_int + s
        mystery_int += 1
    print(s)
elif mystery_int > 0:
    while mystery_int > 0:
        s = mystery_int + s
        mystery_int -= 1
    print(s)