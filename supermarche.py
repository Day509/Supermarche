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
                pygame.display.flip()
            elif