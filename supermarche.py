import pygame


pygame.init()

pygame.display.set_caption('Supermarché')
largeur = 1920
hauteur = 1080
fenetre = pygame.display.set_mode((largeur, hauteur))
arriere_plan = pygame.image.load('Fenetre/supermarche/mycollection/png/fond_supermarché.jpg')
arriere_plan_2 = pygame.image.load('Fenetre/supermarche/mycollection/png/fond_supermarche_flou.png')
bouton_commencer = pygame.image.load('Fenetre/supermarche/mycollection/png/Bouton_Commencer.jpg')
bouton_commencer = pygame.transform.scale(bouton_commencer, (300, 100))
bouton_commencer_rect = bouton_commencer.get_rect()
bouton_commencer_rect.center = (largeur / 2, (hauteur - hauteur / 6) - 10)

charcuterie = pygame.image.load('Fenetre/supermarche/mycollection/png/001-salami.png')
charcuterie_rect = charcuterie.get_rect()
charcuterie_rect.center = (largeur / 5, hauteur / 3)

fleur = pygame.image.load('Fenetre/supermarche/mycollection/png/002-garden-centre.png')
fleur_rect = fleur.get_rect()
fleur_rect.center = (largeur / 3 + 150, hauteur / 3)

glace = pygame.image.load('Fenetre/supermarche/mycollection/png/003-ice-cream-shop.png')
glace_rect = glace.get_rect()
glace_rect.center = (largeur / 2 + 200, hauteur / 3)

pizza = pygame.image.load('Fenetre/supermarche/mycollection/png/004-pizza-shop.png')
pizza_rect = pizza.get_rect()
pizza_rect.center = (largeur - largeur / 5, hauteur /3)

viandes = pygame.image.load('Fenetre/supermarche/mycollection/png/005-butcher-shop.png')
viandes_rect = viandes.get_rect()
viandes_rect.center = (largeur / 4, hauteur - hauteur /3)

fruit = pygame.image.load('Fenetre/supermarche/mycollection/png/006-fruit-stand.png')
fruit_rect = fruit.get_rect()
fruit_rect.center = (largeur / 2, hauteur - hauteur /3)

poisson = pygame.image.load('Fenetre/supermarche/mycollection/png/007-fish-market.png')
poisson_rect = poisson.get_rect()
poisson_rect.center = (largeur - largeur/ 4, hauteur - hauteur /3)

Ecran = fenetre.blit(arriere_plan, (0, 0))
fenetre.blit(bouton_commencer, bouton_commencer_rect)

boucle = True

while boucle:

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_commencer_rect.collidepoint(event.pos):
                Ecran = fenetre.blit(arriere_plan_2, (0, 0))
                fenetre.blit(charcuterie, charcuterie_rect)
                fenetre.blit(fleur, fleur_rect)
                fenetre.blit(glace, glace_rect)
                fenetre.blit(pizza, pizza_rect)
                fenetre.blit(viandes, viandes_rect)
                fenetre.blit(fruit, fruit_rect)
                fenetre.blit(poisson, poisson_rect)
                pygame.display.flip()
