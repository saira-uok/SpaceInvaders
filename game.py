# importing our modules.  
import pygame  
import random  
import math  
  
# initiating our programming  
pygame.init()  
  
# window settings  
window = pygame.display.set_mode((800, 600))  
pygame.display.set_caption("Space Invaders")  
icon = pygame.image.load('spaceship.png')  
pygame.display.set_icon(icon)  
  
# background image  
background = pygame.image.load('2352.jpg')  
  
# player code  
playerImg = pygame.image.load('space-invaders (1).png')  
playerX = 370  
playerY = 480  
playerX_change = 0  
  
# enemies code  
enemyImg = []  
enemyX = []  
enemyY = []  
enemyX_change = []  
enemyY_change = []  
  
num_enemies = 6  
for i in range(num_enemies):  
    enemyImg.append(pygame.image.load('space-invaders (2).png'))  
    enemyX.append(random.randint(0, 735))  
    enemyY.append(random.randint(5, 150))  
    enemyX_change.append(1)  
    enemyY_change.append(40)  
  
# Bullet code  
bulletImg = pygame.image.load('bullet.png')  
bulletX = 0  
bulletY = 480  
bulletX_change = 0  
bulletY_change = 10  
bullet_state = "ready"  
  
# score  
score = 0  
  
  
# displaying our spaceships on the window  
def player(x, y):  
    window.blit(playerImg, (x, y))  
  
  
def enemy(x, y):  
    window.blit(enemyImg, (x, y))  
  
  
def fire_bullet(x, y):  
    global bullet_state  
    bullet_state = "fire"  
    window.blit(bulletImg, (x + 16, y + 10))  
  
  
def isCollision(enemyX, enemyY, bulletX, bulletY):  
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))  
    if distance < 27:  
        return True  
    else:  
        return False  
  
  
run = True  
while run:  
    # setting the background of our game.  
    window.fill((0, 0, 0))  
  
    # background image  
    window.blit(background, (0, 0))  
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False  
  
        # check which key is pressed  
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT:  
                playerX_change = -2  
  
            if event.key == pygame.K_RIGHT:  
                playerX_change = 2  
  
            if event.key == pygame.K_SPACE:  
                bulletX = playerX  
                fire_bullet(bulletX, bulletY)  
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  
                playerX_change = 0  
  
    # making our space ships stop at boundaries  
    # player movement  
    playerX += playerX_change  
    if playerX <= 0:  
        playerX = 0  
  
    elif playerX >= 736:  
        playerX = 736  
    for i in range(num_enemies):  
       # enemy movement  
       enemyX += enemyX_change  
       if enemyX <= 0:  
            enemyX_change = 1  
            enemyY += enemyY_change  
  
       elif enemyX >= 736:  
            enemyX_change = -1  
  
    # bullet movement  
    if bulletY <= 0:  
        bulletY = 480  
        bullet_state = "ready"  
  
    if bullet_state == "fire":  
        fire_bullet(bulletX, bulletY)  
        bulletY -= bulletY_change  
  
    # collision  
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)  
    if collision:  
        bulletY = 480  
        bullet_state = "ready"  
        score += 1  
        print(score)  
        enemyX = random.randint(0, 735)  
        enemyY = random.randint(5, 150)  
  
    player(playerX, playerY)  
    enemy(enemyX, enemyY)  
    pygame.display.update()  
