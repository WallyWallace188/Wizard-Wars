import pygame, random, sys
from pygame.locals import *
from pygame.math import Vector2
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5
PLAYERSIZE = 15
PROJSPEED = 7

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False
    

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    

# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Wizard Wars')
pygame.mouse.set_visible(True)

# set up fonts
font = pygame.font.SysFont(None, 48)

# set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

# set up images
playerImage = pygame.image.load('mage.png')
playerImage = pygame.transform.scale(playerImage, (30, 30))
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')
attack1 = pygame.image.load('flame_left.png')
attack2 = pygame.image.load('flame_right.png')
attack3 = pygame.image.load('flame_up.png')
attack4 = pygame.image.load('flame_down.png')
projRect = attack1.get_rect()

# show the "Start" screen
drawText('Wizard Wars', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


while True:
    # set up the start of the game
    projs=[]
    baddies = []
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    
    baddieAddCounter = 0
    #pygame.mixer.music.play(-1, 0.0)
    proj_velocity = Vector2(PROJSPEED, 0)

    while True: # the game loop runs while the game part is playing

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveRight = False
                    moveLeft = True
                    proj_velocity = Vector2(-PROJSPEED, 0)
           
                if event.key == K_RIGHT:
                    moveLeft = False
                    moveRight = True
                    proj_velocity = Vector2(-PROJSPEED, 0)
                
                if event.key == K_UP:
                    moveDown = False
                    moveUp = True
                    proj_velocity = Vector2(-PROJSPEED, 0)
  
                if event.key == K_DOWN:
                    moveUp = False
                    moveDown = True
                    proj_velocity = Vector2(-PROJSPEED, 0)
                  

                #shooting
                if event.key == K_SPACE:
                   newProj = {'rect': pygame.Rect(playerRect),
                        'speed': proj_velocity,
                        'surface':pygame.transform.scale(attack1, (30, 30)),
                        }
                   
                   projs.append(newProj)

                   
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                        terminate()
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False


                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False

        # Add new baddies at the top of the screen, if needed.
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }

            baddies.append(newBaddie)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)        
            

        # Move the baddies down.        CHANGE TO ATTACK PLAYER
        for b in baddies:
                b['rect'].move_ip(0, b['speed'])


         # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        # delete projectiles at the end
##        for proj in projs:
##            if 

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the player's rectangle
        windowSurface.blit(playerImage, playerRect)

        #draw in projectile
        for p in projs:
               p['rect'].move_ip(p['speed'],p['speed'])
            
    

        # Draw each baddie
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            break

        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()
