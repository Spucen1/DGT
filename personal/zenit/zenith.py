n = int(input())

ponozky = []
pocet = 0
ponozka = ""


for i in range(n):
    ponozky.append(input())

for i in ponozky:
    ponozky.remove(i)
    for y in i:
        match y:
            case "q":
                ponozka += "p"
            case "p":
                ponozka += "q"
            case "d":
                ponozka += "b"
            case "b":
                ponozka += "d"
            case "o":
                ponozka += "o"
    if ponozka[::-1] in ponozky:
        pocet += 1
        ponozky.remove(ponozka[::-1])
        ponozka = ""

print(pocet)
