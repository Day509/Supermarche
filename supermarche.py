import pygame

pygame.init()

pygame.display.set_caption('Le jeu')
fenetre = pygame.display.set_mode((1920, 1080))
arriere_plan = pygame.image.load('Fenetre/supermarche/mycollection/png/grocery-store-2619380_1920.jpg')
Ecran = fenetre.blit(arriere_plan, (0, 0))


boucle = True

while boucle:

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False
            pygame.quit()
