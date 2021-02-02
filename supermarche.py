import pygame

pygame.init()

pygame.display.set_caption('Supermarché')
fenetre = pygame.display.set_mode((1920, 1080))
arriere_plan = pygame.image.load('Fenetre/supermarche/mycollection/png/grocery-store-2619380_1920.jpg')
Ecran = fenetre.blit(arriere_plan, (0, 0))

rectangle = pygame.Rect((1920 * (2 / 5)), 40, 400, 100)
pygame.draw.rect(fenetre, (0, 0, 0), rectangle)

boucle = True

while boucle:

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False
            pygame.quit()
