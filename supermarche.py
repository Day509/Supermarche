import pygame

pygame.init()
pygame.font.init()

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
pizza_rect.center = (largeur - largeur / 5, hauteur / 3)

viandes = pygame.image.load('Fenetre/supermarche/mycollection/png/005-butcher-shop.png')
viandes_rect = viandes.get_rect()
viandes_rect.center = (largeur / 4, hauteur - hauteur / 3)

fruit = pygame.image.load('Fenetre/supermarche/mycollection/png/006-fruit-stand.png')
fruit_rect = fruit.get_rect()
fruit_rect.center = (largeur / 2, hauteur - hauteur / 3)

poisson = pygame.image.load('Fenetre/supermarche/mycollection/png/007-fish-market.png')
poisson_rect = poisson.get_rect()
poisson_rect.center = (largeur - largeur / 4, hauteur - hauteur / 3)

panier = [0, 0, 0, 0, 0, 0, 0]
print(panier)

achat_terminer = pygame.draw.rect(arriere_plan_2, (100, 193, 70), pygame.Rect(largeur - 170, 0, 170, 300), 5)
achat_terminer.topright = (largeur, 0)
police = pygame.font.SysFont('Arial', 40)

titre_panier = police.render("Panier:", True, (0, 0, 0))

police_article = pygame.font.SysFont('Comic sans MS', 25)

coord_y_article = 60

Ecran = fenetre.blit(arriere_plan, (0, 0))
fenetre.blit(bouton_commencer, bouton_commencer_rect)

boucle = True

while boucle:

    charcuterie_panier = police_article.render("Charcuterie: " + str(panier[0]), True, (0, 0, 0))
    fleur_panier = police_article.render("fleur: " + str(panier[1]), True, (0, 0, 0))
    glace_panier = police_article.render("glace: " + str(panier[2]), True, (0, 0, 0))
    pizza_panier = police_article.render("pizza: " + str(panier[3]), True, (0, 0, 0))
    viandes_panier = police_article.render("viandes: " + str(panier[4]), True, (0, 0, 0))
    fruit_panier = police_article.render("fruit: " + str(panier[5]), True, (0, 0, 0))
    poisson_panier = police_article.render("poisson " + str(panier[6]), True, (0, 0, 0))

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
                fenetre.blit(titre_panier, (1780, 3))

                fenetre.blit(charcuterie_panier, (1760, coord_y_article))
                fenetre.blit(fleur_panier, (1760, coord_y_article + 30))
                fenetre.blit(glace_panier, (1760, coord_y_article + 60))
                fenetre.blit(pizza_panier, (1760, coord_y_article + 90))
                fenetre.blit(viandes_panier, (1760, coord_y_article + 120))
                fenetre.blit(fruit_panier, (1760, coord_y_article + 150))
                fenetre.blit(poisson_panier, (1760, coord_y_article + 180))

            elif charcuterie_rect.collidepoint(event.pos):
                panier[0] += 1
                pygame.display.flip()
            elif fleur_rect.collidepoint(event.pos):
                panier[1] += 1
            elif glace_rect.collidepoint(event.pos):
                panier[2] += 1
            elif pizza_rect.collidepoint(event.pos):
                panier[3] += 1
            elif viandes_rect.collidepoint(event.pos):
                panier[4] += 1
            elif fruit_rect.collidepoint(event.pos):
                panier[5] += 1
            elif poisson_rect.collidepoint(event.pos):
                panier[6] += 1

print(panier)
