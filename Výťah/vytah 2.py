nosnost = int(input("Nosnost: "))
vaha = int(input("Váha: "))
x = 0
ludia = 0
while int(x) + vaha < nosnost:
    x += vaha
    ludia += 1
    print(str(x) + "/" + str(nosnost))
    vaha = int(input("Váha: "))
if int(x) + vaha <= nosnost:
    ludia += 1
print("Výťah je plný.")
print("Do výťahu sa zmestili " + str(ludia) + " ludia.")
    
           
