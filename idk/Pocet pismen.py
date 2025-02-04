veta = input("Zadaj vetu: ")
pismeno = input("Zadaj pímeno: ")
while len(pismeno) != 1:
    pismeno = input("Zadaj iba jedno pímeno: ")

pocet_pismen = 0
for i in veta:
    if i == pismeno:
        pocet_pismen += 1
print("Písmeno", pismeno, "sa vo vete nachádza", pocet_pismen, "krát.")

pocet = 0
pozicie = []
for pos in range(len(veta)):
    if veta[pos] == pismeno:
        pocet += 1
        pozicie.append(str(pos))
print("Písmeno", pismeno, "sa vo vete nachádza", pocet, "krát.")
print("Pozicie pismena sú:", " ".join(pozicie))