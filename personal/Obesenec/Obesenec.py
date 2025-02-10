import random
slova = ["auto", "pes", "kocka", "stol", "stolica", "kniha", "skola", "kvet", "strom", "okno", "dvere", "kreslo", "kompas", "kompot", "kompresor", "kompresia", "kompromis", "komplex", "komplikacia", "kompliment", "komplikovany", "komplikovat", "komplikacia", "komplikovanie",
         "dom", "mama", "tata", "pes", "mesto", "vlak", "strom", "list", "slnko", "mesiac", "hviezda", "ryba", "vtak", "motyl", "trava", "kvet", "les", "hora", "rieka", "jazero", "more", "oceán", "pláž", "piesok"]
slovo = random.choice(slova)
pokusy = 9
vipis = "_" * len(slovo)
pouzite = ""
pouzyte = ""
print(vipis)
while pokusy > 0:
    pismeno = str(input("Zadaj pismeno: "))
    x = -1
    vypis = ""
    if len(pismeno) > 1:
        if pismeno == slovo:
            print("Vyhral si!")
            print("Spravne slovo bolo:", slovo + ".")
            break
        pouzyte = pouzyte + ", " + pismeno
    elif len(pismeno) == 1:       
        for pysmeno in slovo:
            x = x + 1
            if pismeno == pysmeno:
                vypis = vypis + pismeno
            else:
                vypis = vypis + vipis[x]
        pouzite = pouzite + ", " + pismeno
    if vypis == vipis:
        pokusy = pokusy - 1
    elif vypis == slovo:
        print("Vyhral si!")
        print("Spravne slovo bolo:", slovo + ".")
        break
    elif vypis == "":
        if len(pismeno) < 1:
            print("Nezadal si pismeno!") 
            vypis = vipis
            pokusy = pokusy - 1
        else:
            print("Zle slovo!")
            vypis = vipis
            pokusy = pokusy - 1
    vipis = vypis
    print(vipis)
    print("Pokusy:", pokusy)
    if pouzite != "":
        print("Použité písmená:", pouzite[2:])
    if pouzyte != "":
        print("Použité slová:", pouzyte[2:])
else:
    print("Prehral si!")
    print("Spravne slovo bolo:", slovo + ".")