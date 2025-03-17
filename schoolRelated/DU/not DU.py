from random import randrange
import pygame
import sys

pygame.init()
display = pygame.display.set_mode((100, 100))
velkost = 100
priestor = [" "] * velkost
hrac = "X"
okraj = "#"
sirka = 10
posLO = (velkost - sirka) // 2
posH = velkost // 2
priestor[posLO] = okraj
priestor[posLO + sirka] = okraj
priestor[posH] = hrac
hrame = True
idk = 0
idk1 = 3.0
score = 0

def posunZnaku(pozicia, posun, znak, delta=0):
    global priestor
    if 0 <= pozicia + posun < velkost and 0 <= pozicia + posun + delta < velkost:
        priestor[pozicia] = " "
        priestor[pozicia + posun] = znak
        return posun
    return 0

while hrame:
    idk += 1
    if idk == 10:
        idk1 += 0.1
        idk = 0
    hodiny = pygame.time.Clock()
    print("|" + "".join(priestor) + "| " + str(score))
    score += 1
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_a:
                posH += posunZnaku(posH, -1, hrac)
            elif udalost.key == pygame.K_d:
                posH += posunZnaku(posH, +1, hrac)
    zmena = randrange(-1, 2)
    posunZnaku(posLO, zmena, okraj, sirka)
    posLO += posunZnaku(posLO + sirka, zmena, okraj, -sirka)
    if hrac not in priestor:
        print("Havária! SCORE: " + str(score - 1))
        hrame = False
    hodiny.tick(idk1)

pygame.quit()