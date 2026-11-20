pole = list(input())

sucet = 0
a = False
b = ""
kolo = 0

for i in pole:
    if i == " ":
        continue
    if int(i) % 2 != 0:
        a = True

    if kolo >= 10:
        b += " TEROR"
    elif a:
        b += " ERROR"
        kolo += int(1)
    else:
        sucet += int(i)
        b += " " + str(sucet)

print(b[1:])