import pygame
import sys
import random
pygame.init()
screen=pygame.display.set_mode(size=(750,750))
pygame.display.set_caption('Apple Catch Game')


apple_img = pygame.image.load('PyGame/Templates/app;y.png')


apple_img = pygame.transform.scale(apple_img, (100, 100))
apple_x = random.randint(0, 750 - 100)
apple_y = -100
fall_speed = 5

player_width, player_height = 150, 30
player_x = 750 // 2 - player_width // 2
player_y = 750 - 50
player_speed = 10

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 750 - player_width:
        player_x += player_speed
    apple_y += fall_speed
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    apple_rect = pygame.Rect(apple_x, apple_y, 100, 100)

    if player_rect.colliderect(apple_rect):
        apple_x = random.randint(0, 750 - 100)
        apple_y = -100

    if apple_y > 750:
        apple_x = random.randint(0, 750 - 100)
        apple_y = -100

    screen.fill("lightblue")
    screen.blit(apple_img, (apple_x, apple_y))
    pygame.draw.rect(screen, (255, 0, 0), player_rect)


    pygame.display.update()
    clock.tick(60)