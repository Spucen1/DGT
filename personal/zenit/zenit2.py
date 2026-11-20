a = input()

pole = []
b = ""
for i in a:
    if i == " ":
        pole.append(int(b))
        b = ""
    else:
        b += i

pole.append(int(b))

pole.sort()

pole = list(map(str, pole))

print(" ".join(pole))
