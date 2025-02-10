from random import randrange
velkostPola = 20
polePC = [""] * velkostPola
poleHrac = [""] * velkostPola
for i in range(5):
    pos = randrange(velkostPola)
    while polePC[pos] =="¤":
        pos = randrange(velkostPola)
    polePC[pos] = "¤"
for pos in range(velkostPola):
    minVokoli = 0
    if polePC[pos] != "¤":
        if pos != 0:
            if polePC[pos-1] == "¤":
                minVokoli += 1
        if pos < velkostPola - 1:
            if polePC[pos+1] == "¤":
                minVokoli += 1
        polePC[pos] = str(minVokoli)
hrame = True
while hrame:
    print(" ".join(poleHrac))
    poziciaHrac = int(input("Pozícia? "))
    if poziciaHrac < 0:
        poziciaHrac *= -1
        poleHrac[poziciaHrac] = "¤"
    elif polePC[poziciaHrac] == "¤":
        print("Stupil si na mínu!")
        hrame = False
    else:
        poleHrac[poziciaHrac] = polePC[poziciaHrac]
        defaultPozicia = poziciaHrac
        while poleHrac[poziciaHrac] == "0":
            poziciaHrac += 1
            poleHrac[poziciaHrac] = polePC[poziciaHrac]
        while poleHrac[defaultPozicia] == "0":
            defaultPozicia -= 1
            poleHrac[defaultPozicia] = polePC[defaultPozicia]
        if poleHrac == polePC:
            print("Vyhral si!")
            hrame = False
