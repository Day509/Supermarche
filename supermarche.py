import pygame

pygame.init()

pygame.display.set_caption('Supermarché')
fenetre = pygame.display.set_mode((1920, 1080))
arriere_plan = pygame.image.load('Fenetre/supermarche/mycollection/png/fond_supermarché.jpg')
Ecran = fenetre.blit(arriere_plan, (0, 0))

rectangle = pygame.Rect((1920 * (2 / 5)), 840, 400, 100)
pygame.draw.rect(fenetre, (0, 0, 0), rectangle)

boucle = True

while boucle:

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            boucle = False
            pygame.quit()
