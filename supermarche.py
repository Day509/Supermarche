import pygame

pygame.init()
pygame.font.init()

pygame.display.set_caption('Supermarché')
largeur = 1920
hauteur = 1080
fenetre = pygame.display.set_mode((largeur, hauteur))
arriere_plan = pygame.image.load('Fenetre/supermarche/mycollection/png/fond_supermarché.jpg')
arriere_plan_2 = pygame.image.load('Fenetre/supermarche/mycollection/png/fond_supermarche_flou.png')
arriere_plan_3 = pygame.image.load('Fenetre/supermarche/mycollection/png/fond_supermarche_flou.png')

bouton_commencer = pygame.image.load('Fenetre/supermarche/mycollection/png/Bouton_Commencer.jpg')
bouton_commencer = pygame.transform.scale(bouton_commencer, (300, 100))
bouton_commencer_rect = bouton_commencer.get_rect()
bouton_commencer_rect.center = (largeur / 2, (hauteur - hauteur / 6) - 10)

bouton_valider_panier = pygame.image.load('Fenetre/supermarche/mycollection/png/bouton_valider_panier.png')
bouton_valider_panier = pygame.transform.scale(bouton_valider_panier, (120, 50))
bouton_valider_panier_rect = bouton_valider_panier.get_rect()
bouton_valider_panier_rect.topright = (largeur - 23, 305)

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

prix_article = [4.0, 1.0, 1.5, 3.5, 3.7, 2.3, 2.1]
prix_totale = 0

achat_terminer = pygame.draw.rect(arriere_plan_2, (100, 193, 70), pygame.Rect(largeur - 170, 0, 170, 300), 5)
achat_terminer.topright = (largeur, 0)

police = pygame.font.SysFont('Arial', 40, False, True)
police.set_underline(True)

police_panier_fini = pygame.font.SysFont("Rockwell", 50)
police_panier_fini.set_bold(True)

titre_panier = police.render("Panier:", True, (0, 0, 0))

police_article = pygame.font.SysFont('Comic sans MS', 30)

coord_y_article = 80

Ecran = fenetre.blit(arriere_plan, (0, 0))
fenetre.blit(bouton_commencer, bouton_commencer_rect)

etape2 = False
boucle = True

while boucle:

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_commencer_rect.collidepoint(event.pos):
                etape2 = True

            if etape2:
                Ecran = fenetre.blit(arriere_plan_2, (0, 0))
                fenetre.blit(charcuterie, charcuterie_rect)
                fenetre.blit(fleur, fleur_rect)
                fenetre.blit(glace, glace_rect)
                fenetre.blit(pizza, pizza_rect)
                fenetre.blit(viandes, viandes_rect)
                fenetre.blit(fruit, fruit_rect)
                fenetre.blit(poisson, poisson_rect)
                fenetre.blit(titre_panier, (1777, 3))
                fenetre.blit(bouton_valider_panier, bouton_valider_panier_rect)
                charcuterie_panier_police = police_article.render("Charcuterie: " + str(panier[0]), True,
                                                                  (255, 255, 255))
                fenetre.blit(charcuterie_panier_police, (1757, coord_y_article))
                fleur_panier_police = police_article.render("fleur: " + str(panier[1]), True, (255, 255, 255))
                fenetre.blit(fleur_panier_police, (1757, coord_y_article + 30))
                glace_panier_police = police_article.render("glace: " + str(panier[2]), True, (255, 255, 255))
                fenetre.blit(glace_panier_police, (1757, coord_y_article + 60))
                pizza_panier_police = police_article.render("pizza: " + str(panier[3]), True, (255, 255, 255))
                fenetre.blit(pizza_panier_police, (1757, coord_y_article + 90))
                viandes_panier_police = police_article.render("viandes: " + str(panier[4]), True, (255, 255, 255))
                fenetre.blit(viandes_panier_police, (1757, coord_y_article + 120))
                fruit_panier_police = police_article.render("fruit: " + str(panier[5]), True, (255, 255, 255))
                fenetre.blit(fruit_panier_police, (1757, coord_y_article + 150))
                poisson_panier_police = police_article.render("poisson: " + str(panier[6]), True, (255, 255, 255))
                fenetre.blit(poisson_panier_police, (1757, coord_y_article + 180))

                if bouton_valider_panier_rect.collidepoint(event.pos):
                    Ecran = fenetre.blit(arriere_plan_3, (0, 0))
                    for i in range(len(panier)):
                        prix_totale += (panier[i] * prix_article[i])

                    panier_fini = police_panier_fini.render(
                        "Votre panier est rempli, Vous devez réglé: " + str(prix_totale) + "€", True, (0, 0, 0))

                    fenetre.blit(panier_fini, ((largeur / 3) - 80, (hauteur / 2) - 200))

                elif charcuterie_rect.collidepoint(event.pos):
                    panier[0] += 1

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
