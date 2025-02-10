import random
text = input("Správa: ")
dot = text[0]
if dot == ":":
    text = text[1:]
    first = text[::2]
    second = text[1::2]
    for sym in first:
        numb = second[0]
        second = second[1:]
        sim = ord(sym) - int(numb)
        print(chr(sim), end="")
else:
    print(":", end="")
    for znak in text:
        num = random.randint(0, 9)
        ynak = ord(znak) + num
        print(chr(ynak), end="")
        print(num, end="")