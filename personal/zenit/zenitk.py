n = int(input())

p = input()
x = ""
pole = []
predosle = 0
sucet = 0
akt = []

idk = 0

for i in input:
    if i == " ":
        pole.append(int(x))
        x = ""
    else:
        x += i
else:
    pole.append(int(x))

for i in pole:
    mi = []

    if i < predosle:
        mi.append(i)
        for a in akt[::-1]:
            if a < mi[]
    else:
        mi = []
        akt.append(i)

    if sum(mi) > sum