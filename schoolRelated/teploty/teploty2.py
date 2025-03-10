subor = open("teploty2.txt", "r")
pocetDni = 0
rano = 0
obed = 0
vecer = 0
for den in subor:
    den = den.strip()
    den = den.split(" ")
    pocetDni += 1
    rano += int(den[0])
    obed += int(den[1])
    vecer += int(den[2])
print("Priemerne teploty za", pocetDni, "dni:")
print("rano:", rano/pocetDni)
print("obed:", obed/pocetDni)
print("vecer:", vecer/pocetDni)