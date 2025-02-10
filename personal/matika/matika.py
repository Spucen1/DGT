cislo = int(input("Zadaj čislo: "))
while cislo != 1:
    if cislo % 2 == 0:
        cislo = cislo // 2
    else:
        cislo = 3 * cislo + 10
    print(cislo, end=" ")