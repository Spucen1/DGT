from random import randrange  # Import funkcie randrange na generovanie náhodných čísel
import pygame
import sys
pygame.init()
#obtiaznost = int(input("Obtiaznost(1-10): "))
display = pygame.display.set_mode((10,10))
velkost = 20  # Veľkosť herného poľa
priestor = [" "] * velkost  # Inicializácia herného poľa ako zoznam prázdnych znakov
hrac = "X"  # Znak predstavujúci hráča
okraj = "#"  # Znak predstavujúci prekážky
posLO = velkost // 4  # Začiatočná pozícia prvej prekážky
sirka = velkost // 2  # Vzdialenosť medzi dvoma časťami prekážky
posH = velkost // 2  # Začiatočná pozícia hráča
priestor[posLO] = okraj  # Umiestnenie prvej časti prekážky
priestor[posLO + sirka] = okraj  # Umiestnenie druhej časti prekážky
priestor[posH] = hrac  # Umiestnenie hráča na hracie pole
hrame = True  # Premenná určujúca, či hra beží
#obtiaznost = int(input("Obtiaznost(1-10): "))
score = 0
def posunZnaku(pozicia, posun, znak, delta=0):  
    """ Funkcia na presunutie znaku v hernom poli.  
        Ak je posun možný, presunie znak na novú pozíciu.  
        Ak nie, ponechá ho na pôvodnom mieste.  
    """
    global priestor  # Použitie globálnej premennej priestor
    if 0 <= pozicia + posun < velkost and 0 <= pozicia + posun + delta < velkost:
        priestor[pozicia] = " "  # Vymazanie znaku zo starej pozície
        priestor[pozicia + posun] = znak  # Umiestnenie znaku na novú pozíciu
        return posun  # Vracia hodnotu posunu
    return 0  # Ak nie je možné posunúť, vráti 0
while hrame:  # Hlavná herná slučka
    hodiny = pygame.time.Clock()
    print("|" + "".join(priestor) + "| " + str(score))  # Vykreslenie herného poľa
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
    zmena = randrange(-1, 2)  # Náhodná zmena pozície prekážky (-1, 0 alebo 1)
    posunZnaku(posLO, zmena, okraj, sirka)  # Posun prvej časti prekážky
    posLO += posunZnaku(posLO + sirka, zmena, okraj, -sirka)  # Posun druhej časti prekážky
    if hrac not in priestor:  # Ak sa hráč už nenachádza v poli, znamená to kolíziu
        print("Havária! SCORE: " + str(score - 1))  # Vypíše správu o kolízii
        hrame = False  # Ukončenie hry
    #hodiny.tick(obtiaznost)
    hodiny.tick(5)
pygame.quit()