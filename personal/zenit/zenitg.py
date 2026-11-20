n = int(input())

pocet = 0

while n > 2:
    n = n//2
    if n % 2 == 0:
        pocet += 1
    else:
        print("nie")
        break
else:
    print("ano")
    print(pocet + 1)
