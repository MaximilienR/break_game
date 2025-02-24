import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définition de la fenêtre de jeu
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Définition du titre de la fenêtre
pygame.display.set_caption("Pendu")

# Définition des variables de jeu
mots = {
    "python": "Langage de programmation",
    "pygame": "Bibliothèque de jeux pour Python",
    "jeu": "Activité ludique",
    "pendu": "Jeu de mots",
    "algorithmique": "Étude des algorithmes",
    "base de données": "Système de gestion de données",
    "cloud computing": "Modèle de calcul informatique en ligne",
    "cyber sécurité": "Sécurité des systèmes et des données informatiques",
    "développement ": "Création de sites web et d'applications web",
    "intelligence artificielle": "Domaine de l'informatique qui simule l'intelligence humaine",
    "langage de programmation": "Système de notation pour écrire des programmes informatiques",
    "machine learning": "Domaine de l'informatique qui permet aux machines d'apprendre",
    "network": "Réseau de communication informatique",
    "programmation": "Écriture de programmes informatiques",
    "réseau": "Système de communication informatique",
    "sécurité informatique": "Protection des systèmes et des données informatiques",
    "système d'exploitation": "Logiciel qui gère les ressources d'un ordinateur",
    "télécommunication": "Transmission de données à distance",
    "virtualisation": "Création d'environnements virtuels informatiques"
}

mot_a_trouver = random.choice(list(mots.keys())).lower()
definition = mots[mot_a_trouver]
lettres_trouvees = []
chances = 7
pendu_etat = 0

# Boucle de jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            lettre = event.unicode
            if lettre in mot_a_trouver and lettre not in lettres_trouvees:
                lettres_trouvees.append(lettre)
            elif lettre not in mot_a_trouver and lettre not in lettres_trouvees:
                chances -= 1
                pendu_etat += 1  # Incrémentation de l'état du pendu

    # Dessin de la fenêtre de jeu
    screen.fill(WHITE)

    # Dessin du pendu en fonction de l'état
    pygame.draw.line(screen, BLACK, (100, 50), (200, 50), 2)  # Barre horizontale
    pygame.draw.line(screen, BLACK, (150, 50), (150, 200), 2)  # Poteau vertical
    pygame.draw.line(screen, BLACK, (150, 200), (200, 200), 2)  # Base du pendu

    if pendu_etat >= 1 and lettre not in lettres_trouvees:
        pygame.draw.line(screen, BLACK, (150, 70), (170, 90), 2)  # Corde
    if pendu_etat >= 2:
        pygame.draw.circle(screen, BLACK, (170, 110), 20)  # Tête
    if pendu_etat >= 3:
        pygame.draw.line(screen, BLACK, (170, 130), (170, 160), 2)  # Corps
    if pendu_etat >= 4:
        pygame.draw.line(screen, BLACK, (170, 140), (150, 160), 2)  # Bras gauche
    if pendu_etat >= 5:
        pygame.draw.line(screen, BLACK, (170, 140), (190, 160), 2)  # Bras droit
    if pendu_etat >= 6:
        pygame.draw.line(screen, BLACK, (170, 160), (150, 180), 2)  # Jambe gauche
    if pendu_etat >= 7:
        pygame.draw.line(screen, BLACK, (170, 160), (190, 180), 2)  # Jambe droite

    # Dessin des lettres trouvées
    for i, lettre in enumerate(mot_a_trouver):
        if lettre in lettres_trouvees:
            font = pygame.font.Font(None, 36)
            text = font.render(lettre, True, BLACK)
            screen.blit(text, (200 + i * 30, 200))
            
    
# Dessin de la définition
    font = pygame.font.Font(None, 24)
    text = font.render(definition, True, BLACK)
    screen.blit(text, (200, 250))

    # Dessin des chances restantes
    font = pygame.font.Font(None, 36)
    text = font.render("Chances : " + str(chances), True, BLACK)
    screen.blit(text, (200, 300))

    # Mise à jour de la fenêtre de jeu
    pygame.display.flip()

    # Vérification de la victoire ou de la défaite
    if all(lettre in lettres_trouvees for lettre in mot_a_trouver):
        print("Vous avez gagné !")
        pygame.quit()
        sys.exit()
    elif chances == 0:
        print("Vous avez perdu !")
        pygame.quit()
        sys.exit()

    # Limitation de la vitesse de la boucle de jeu
    pygame.time.Clock().tick(60)