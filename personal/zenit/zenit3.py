n = int(input())

one = ["4", "6", "9", "0"]
two = "8"

pocet = 1

for i in range(n):
    a = input()
    for y in a:
        if y in one:
            pocet += 1
        elif y == "8":
            pocet += 2

print(pocet)