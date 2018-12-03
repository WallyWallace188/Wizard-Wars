#-----!!!!SPACE INVADERS!!!!-----
import pygame, sys
from pygame.locals import *
#-----MAIN FUNCTIONS-----
def movement(move_x):
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            move_x = -5
        if event.key == K_RIGHT:
            move_x = 5
    if event.type == KEYUP:
        if event.key == K_LEFT:
            move_x = 0
        if event.key == K_RIGHT:
            move_x = 0
    return move_x


#-----FFRAME RAEE / SCREEN SIZE-----
clock = pygame.time.Clock()
w,h = 800,800
screen = pygame.display.set_mode((w,h))

#-----SETTING IMAGES-----
pygame.mouse.set_visible(0)

ship = pygame.image.load("baddie.png")
ship = pygame.transform.scale(ship,(100,50))
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2

screen.blit(ship, (ship_left,ship_top))

shot1 = pygame.image.load("mage.png")
shot1 = pygame.transform.scale(shot1,(25,25))
shot2 = shot1
shot_count = 0
shot_y = 0
shot_y_2 = 0

#-----GLOBAL VARIABLES-----
x = 200
resetShot = 0
move_x = 0
#-----MAIN GAME LOOP-----
while True:
    clock.tick(60)
    screen.fill((0,0,0))
    #x,y = pygame.mouse.get_pos()
    screen.blit(ship, (x-ship.get_width()/2,ship_top))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        move_x = movement(move_x)

        if event.type == KEYDOWN:
            if event.key == K_SPACE and shot_count == 0:
                shot_y = h-50
                shot_x = x
            elif event.type == K_SPACE and shot_count == 1:
                shot_y_2 = h-50
                shot_x_2 = x
            print(h, ' ', shot_y, shot_count)
        if event.type == KEYUP:
            if event.key == K_SPACE and shot_count == 0:
                resetShot = 0 
            elif event.type == K_SPACE and shot_count == 1:
                resetShot = 0


    if shot_y > 0:
        screen.blit(shot1, (shot_x-shot1.get_width()/2,shot_y))
        shot_y -= 15
    if shot_y_2 > 0:
        screen.blit(shot2, (shot_x_2-shot1.get_width()/2,shot_y_2))
        shot_y_2 -= 15

    x+=move_x
    pygame.display.update()
