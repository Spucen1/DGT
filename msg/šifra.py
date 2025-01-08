import random
text = input("Správa: ")
for znak in text:
    num = random.randint(0, 9)
    ynak = ord(znak) + num
    print(chr(ynak), end="")
    print(num, end="")