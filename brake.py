import pygame
import sys

# Initialisation de Pygame
pygame.init()
# compteur de vie 
life = 3
#afficher le compteur de vie 
print("Vous avez", life, "vies")

#Game over
if life == 0:
    print("Game over")
    
# Définition de la fenêtre de jeu
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
 
# Définition des couleurs
WHITE = (255, 255, 255)
BLUE =(3,34,76)

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
        brick_x = j * 60 + 10
        brick_y = i * 30 + 10
        bricks.append((brick_x, brick_y))
## Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement de la balle
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    #Deplacement de la raquette
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += 5

    # Collision avec les bordures de l'écran
    if ball_x < 0 or ball_x > screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y < 0:
        ball_speed_y = -ball_speed_y
    if ball_y> screen_height:
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
        if (ball_x > brick[0] and ball_x < brick[0] + 60 and
            ball_y > brick[1] and ball_y < brick[1] + 30):
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
    
    

    # Mise à jour de l'écran
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    # Fin du jeu si le nombre de vies est à 0
    if life <= 0:
        print("Game Over")
        pygame.quit()
        sys.exit()