import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((640, 480))

# Définition des couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Création du sprite de Mario
mario = pygame.Surface((30, 30))
mario.fill(RED)

# Création de la plateforme
platform = pygame.Surface((2000, 20))
platform.fill(WHITE)

# Position initiale de Mario
mario_x = 100
mario_y = 100

# Vitesse de chute de Mario
mario_vy = 0
mario_gravity = 0.5

# Création des trous
trous = [
    pygame.Rect(300, 300, 50, 20),
    pygame.Rect(600, 300, 50, 20),
    pygame.Rect(900, 300, 50, 20)
]

# Position de la caméra
camera_x = 0

# Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement de Mario
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_x -= 5
    if keys[pygame.K_RIGHT]:
        mario_x += 5
    if keys[pygame.K_SPACE] and mario_vy == 0:
        mario_vy = -15    

    # Chute de Mario
    mario_vy += mario_gravity
    mario_y += mario_vy

    # Vérification de la collision avec la plateforme
    if mario_y + mario.get_height() >= platform.get_rect(topleft=(100, 300)).top and mario_x + mario.get_width() > 100 and mario_x < 100 + platform.get_width():
        for trou in trous:
            if mario_x + mario.get_width() > trou.left and mario_x < trou.right and mario_y + mario.get_height() > trou.top and mario_y < trou.bottom:
                # Mario est dans un trou, il ne peut pas atterrir
                break
        else:
            mario_y = platform.get_rect(topleft=(100, 300)).top - mario.get_height()
            mario_vy = 0

    # Ajustement de la caméra
    camera_x = -mario_x + 300 + 100 if mario_x > 300 else -mario_x + 100 + 100 if mario_x < 100 else camera_x

    # Dessin de la fenêtre
    screen.fill((0, 0, 0))
    screen.blit(mario, (mario_x - camera_x, mario_y))
    screen.blit(platform, (100 + camera_x, 300))
    for trou in trous:
        pygame.draw.rect(screen, (0, 0, 0), (trou.left + camera_x, trou.top, trou.width, trou.height))

    # Mise à jour de la fenêtre
    pygame.display.flip()
    pygame.time.Clock().tick(60)