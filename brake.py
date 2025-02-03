import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Compteur de vie
life = 3

# Afficher le compteur de vie
print("Vous avez", life, "vies")

# Définition de la fenêtre de jeu
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Définition des couleurs
WHITE = (255, 255, 255)
BLUE = (3, 34, 76)

# Définition de la balle
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_speed_x = 5
ball_speed_y = 5
ball_radius = 10

# Définition de la raquette
paddle_width = 100
paddle_height = 20
paddle_x = screen_width / 2 - paddle_width / 2
paddle_y = screen_height - paddle_height - 20

# Définition des briques
bricks = []
for i in range(5):
    for j in range(10):
        brick_x = j * (60 + 4) + 10
        brick_y = i * (30 + 4) + 10
        bricks.append((brick_x, brick_y))

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Déplacement de la raquette
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 10
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += 10

    # Collision avec les bordures de l'écran
    if ball_x < 0 or ball_x > screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y < 0:
        ball_speed_y = -ball_speed_y
    if ball_y > screen_height:
        life -= 1
        ball_x = screen_width / 2
        ball_y = screen_height / 2
        ball_speed_x = 5
        ball_speed_y = 5

    # Collision avec la raquette
    if ball_y + ball_radius > paddle_y and ball_x > paddle_x and ball_x < paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # Collision avec les briques
    for brick in bricks:
        if (ball_x > brick[0] and ball_x < brick[0] + 60 + 4 and
            ball_y > brick[1] and ball_y < brick[1] + 30 + 4):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y

    # Dessin de l'écran
    screen.fill(BLUE)
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, (brick[0], brick[1], 60, 30))

    # Afficher le nombre de vies
    font = pygame.font.Font(None, 36)
    text = font.render("Vies : " + str(life), True, (255, 255, 255))
    screen.blit(text, (screen_width - 150, screen_height - 40))  # Dessine le texte en bas à droite

    # Afficher le score
    score_text = font.render("Score : " + str(len(bricks)), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Afficher le message "Partie terminée" lorsque le joueur a perdu
    if life <= 0:
        game_over_text = font.render("Partie terminée. Votre score est de " + str(len(bricks)), True, (255, 255, 255))
        screen.blit(game_over_text, (screen_width / 2 - game_over_text.get_width() / 2, screen_height / 2 - game_over_text.get_height() / 2))

    # Mise à jour de l'écran
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    # Fin du jeu si le nombre de vies est à 0
    if life <= 0 and len(bricks) == 0:
        print("Game Over")
        pygame.quit()
        sys.exit()