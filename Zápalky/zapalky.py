import random
N = int(input("Počet zápaliek: "))
N = abs(N)
l = "|" * N
while l != "":
    print(l)
    i = 0
    while i < 1 or i > 3:
        i = int(input("Kolko zápaliek odoberiete? "))
        if i < 1:
            print("Minimálne jednu!")
        elif i > 3:
            print("Maximálne tri!")
    l = l[:-i]
    if l == "":
        print("Prehral si!")
    else:
        i = random.randint(1, 3)
        print("Počítač odoberá", i, "zápalky.")
        l = l[:-i]
        if l == "":
            print("Vyhral si!")