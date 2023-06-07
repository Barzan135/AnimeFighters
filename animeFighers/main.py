import pygame
from fighter import Fighter
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Anime Fighers")

#set FPS
clock = pygame.time.Clock()
FPS = 30

bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#define for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#create two instances of fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#game loop
loop = True
while loop:

    #set FPS variables
    clock.tick(FPS)
    #draw background
    draw_bg()

    #movement initialization
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
   # fighter_2.move()

    #Draw fighers 
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    #update display
    pygame.display.update()

pygame.quit()