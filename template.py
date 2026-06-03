import pygame
import sys

# Initialize pygame
pygame.init()

# Create the display window
screen = pygame.display.set_mode((1700, 1000))
pygame.display.set_caption('Apple Falling Template')
apple = pygame.image.load('PyGame/Templates/app;y.png')  
appl = pygame.transform.scale(apple, (100, 100))
ax = 0  
ay = 800 
fall_speed = 5  
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ax += fall_speed
    if ax > 1000:
        ax = -100 
    screen.fill("lightblue")
    screen.blit(appl, (ay, ax))
    pygame.display.update()
    clock.tick(60)