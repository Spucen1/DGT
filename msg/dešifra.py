sprava = input("Sprava: ")
first = sprava[::2]
second = sprava[1::2]
for sym in first:
    numb = second[0]
    second = second[1:]
    sim = ord(sym) - int(numb)
    print(chr(sim), end="")