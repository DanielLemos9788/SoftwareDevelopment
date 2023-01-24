#IMPORTS PYGAME LIBRARY
#pip3 install pygame --pre
import pygame
import random
import math
from pygame import mixer

#INITIATES PYGAME WITH INIT
pygame.init()

#CREATES NEW SCREEN
game_screen = pygame.display.set_mode((800,600))

#GENERATES NEW TITTLE, ICON AND BACKGROUND
pygame.display.set_caption(" SPACE INVADERS")
icon = pygame.image.load("star_wars_ship.png")
pygame.display.set_icon(icon)
background = pygame.image.load("mod_galaxy_two.png")

#ADDS MUSIC AND SOUNDS
mixer.music.load("BackgrounMusic.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

#PLAYER VARIABLES
player_ship = pygame.image.load("player_combat_ship.png")
x_o_loc = 368
y_o_loc = 500
x_play_loc = 0
#Player Location Function
def player_location(x,y):
    game_screen.blit(player_ship,(x, y))

#ENEMY VARIABLES
enemy_ship = []
x_e_loc = []
y_e_loc = []
x_enem_loc = []
y_enem_loc = []
total_enemy_ships = 8

for e in range(total_enemy_ships):
    enemy_ship.append(pygame.image.load("star_wars_enemy_ship.png"))
    x_e_loc.append(random.randint(0, 736))
    y_e_loc.append(random.randint(50, 200))
    x_enem_loc.append(0.5)
    y_enem_loc.append(50)

#Enemy Location Function
def enemy_location(x,y,ene):
    game_screen.blit(enemy_ship[ene],(x, y))

#BULLET VARIABLES
bullet = pygame.image.load("bullet.png")
x_b_loc = 0
y_b_loc = 500
x_bullet_loc = 0
y_bullet_loc = 3
visible_bullet = False
#Bullet Function
def fire_bullet(x,y):
    global visible_bullet
    visible_bullet = True
    game_screen.blit(bullet, (x + 16, y + 10))

#SCORE VARIABLE
score = 0
score_font = pygame.font.Font("fastest.ttf", 32)
score_x = 10
score_y = 10
#Shows the Score
def show_score(x,y):
    text_x = score_font.render(f"Score: {score}", True, (255,255,255))
    game_screen.blit(text_x, (x, y))

#GAME OVER FUNCTION + TEXT
final_font = pygame.font.Font("fastest.ttf", 40)
def game_over():
    over_text = final_font.render("GAME OVER", True, (255,255,255))
    game_screen.blit(over_text, (220,250))


#COLLISION FORMULA - DISTANCE BETWEEN OBJECTS
def collision(x_1,y_1,x_2,y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distance < 27:
        return True
    else:
        False

#LOOP OF THE GAME SPACE INVADERS
running_option = True
while running_option:
    #RGB of the Screen
    #game_screen.fill((205, 144, 228))
    #New Image as Background
    game_screen.blit(background, (-1,0))

    #EVENTS OF THE GAME
    for event in pygame.event.get():
        #Stops the game
        if event.type == pygame.QUIT:
            running_option = False
        #Movement Key Down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_play_loc = -1
            if event.key == pygame.K_RIGHT:
                x_play_loc = 1
            if event.key == pygame.K_SPACE:
                if visible_bullet == False:
                    bullet_sound = mixer.Sound("BulletSound.mp3")
                    bullet_sound.play()
                    x_b_loc = x_o_loc
                    fire_bullet(x_b_loc, y_b_loc)

        #Movement Key Up
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                x_play_loc = 0

    #PLAYER CONFIGURATIONS
    #Updates Value of Player Location
    x_o_loc += x_play_loc
    #Keeps the player inside the screen
    if x_o_loc <= 0:
        x_o_loc = 0
    elif x_o_loc >= 736:
        x_o_loc = 736
    #Updates player location
    player_location(x_o_loc, y_o_loc)

    #ENEMY CONFIGURATIONS
    #Updates Value of Enemy Location
    for e in range(total_enemy_ships):
        #End of the Game
        if y_e_loc[e] > 484:
            for k in range(total_enemy_ships):
                y_e_loc[k] = 1000
            game_over()
            break

        x_e_loc[e] += x_enem_loc[e]
    # Keeps the enemy inside the screen
        if x_e_loc[e] <= 0:
            x_enem_loc[e] = 0.5
            y_e_loc[e] += y_enem_loc[e]
        elif x_e_loc[e] >= 736:
            x_enem_loc[e] = -0.5
            y_e_loc[e] += y_enem_loc[e]
        # COLLISIONS
        collision_x = collision(x_e_loc[e], y_e_loc[e], x_b_loc, y_b_loc)
        if collision_x == True:
            hit_sound = mixer.Sound("HitSound.mp3")
            hit_sound.play()
            y_b_loc = 500
            visible_bullet = False
            score += 100
            x_e_loc[e] = random.randint(0, 736)
            y_e_loc[e] = random.randint(50, 200)
        # Updates enemy location
        enemy_location(x_e_loc[e], y_e_loc[e], e)

    #BULLET CONFIGURATIONS
    #Recharges the bullet once it disappears
    if y_b_loc <= -32:
        y_b_loc = 500
        visible_bullet = False
    #Bullet movement
    if visible_bullet == True:
        fire_bullet(x_b_loc,y_b_loc)
        y_b_loc -= y_bullet_loc

    #Updates and Shows the Score
    show_score(score_x,score_y)

    #Updates the Screen
    pygame.display.update()

