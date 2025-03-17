import random
import pygame
import sys

pygame.init()

display = pygame.display.set_mode((800, 800))
area = [["o"] * 8] * 8
shapes = ["    X XXX", "     XXXX", "   X  XXX"]

game = True
while game:
    for i in area:
        print(*i)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()