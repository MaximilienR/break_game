import pygame
import sys
import math
import random

# Initialisation de Pygame
pygame.init()

screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Définition des couleurs
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Définition du centre du cercle
center_x = screen_width // 2
center_y = screen_height // 2

# Définition du rayon du cercle
radius = 200

# Dessin du cercle
pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), radius, 1)

# Dessin des quatre secteurs du cercle
angle = 0
sectors = []
for color in [RED, GREEN, BLUE, YELLOW]:
    sector = pygame.draw.polygon(screen, color, [
        (center_x, center_y),
        (center_x + radius * math.cos(math.radians(angle)), center_y + radius * math.sin(math.radians(angle))),
        (center_x + radius * math.cos(math.radians(angle + 90)), center_y + radius * math.sin(math.radians(angle + 90)))
    ])
    sectors.append(sector)
    angle += 90

# Variable pour stocker l'état des secteurs
sector_states = [False, False, False, False]

# Variable pour stocker la couleur choisie par l'ordinateur
computer_color = None

# Fonction pour choisir une couleur au hasard
def choose_color():
    return random.choice([RED, GREEN, BLUE, YELLOW])

# Choix de la couleur par l'ordinateur
computer_color = choose_color()

# Dessin du cercle avec la couleur choisie par l'ordinateur
screen.fill((0, 0, 0))
pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), radius, 1)

# Dessin des quatre secteurs du cercle
angle = 0
for i, color in enumerate([RED, GREEN, BLUE, YELLOW]):
    if color == computer_color:
        pygame.draw.polygon(screen, (255, 255, 255), [
            (center_x, center_y),
            (center_x + radius * math.cos(math.radians(angle)), center_y + radius * math.sin(math.radians(angle))),
            (center_x + radius * math.cos(math.radians(angle + 90)), center_y + radius * math.sin(math.radians(angle + 90)))
        ])
    else:
        pygame.draw.polygon(screen, color, [
            (center_x, center_y),
            (center_x + radius * math.cos(math.radians(angle)), center_y + radius * math.sin(math.radians(angle))),
            (center_x + radius * math.cos(math.radians(angle + 90)), center_y + radius * math.sin(math.radians(angle + 90)))
        ])
    angle += 90

# Mise à jour de l'écran
pygame.display.flip()

# Variable pour stocker le temps où le secteur a été cliqué
sector_click_time = [0, 0, 0, 0]

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, sector in enumerate(sectors):
                if sector.collidepoint(mouse_pos):
                    sector_states[i] = True
                    sector_click_time[i] = pygame.time.get_ticks()

    # Dessin du cercle
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), radius, 1)


    # Dessin des quatre secteurs du cercle
    angle = 0
    for i, color in enumerate([RED, GREEN, BLUE, YELLOW]):
        if sector_states[i] and pygame.time.get_ticks() - sector_click_time[i] < 1000:
            pygame.draw.polygon(screen, (255, 255, 255), [
                (center_x, center_y),
                (center_x + radius * math.cos(math.radians(angle)), center_y + radius * math.sin(math.radians(angle))),
                (center_x + radius * math.cos(math.radians(angle + 90)), center_y + radius * math.sin(math.radians(angle + 90)))
            ])
        else:
            sector_states[i] = False
            pygame.draw.polygon(screen, color, [
                (center_x, center_y),
                (center_x + radius * math.cos(math.radians(angle)), center_y + radius * math.sin(math.radians(angle))),
                (center_x + radius * math.cos(math.radians(angle + 90)), center_y + radius * math.sin(math.radians(angle + 90)))
            ])
        angle += 90

    # Mise à jour de l'écran
    pygame.display.flip()
    
    # Simuler le clic sur la couleur choisie par l'ordinateur
    for i, color in enumerate([RED, GREEN, BLUE, YELLOW]):
        if color == computer_color:
            sector_states[i] = True
            sector_click_time[i] = pygame.time.get_ticks()
            
 
