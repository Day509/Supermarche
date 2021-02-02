import pygame

pygame.init()

pygame.display.set_caption('Le jeu')
pygame.display.set_mode((500, 300))

boucle = True

while boucle:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False
            pygame.quit()
