# Import the pygame library and initialise the game engine
import pygame,sys,random
from pygame.locals import *
from mage import Mage
from Spell import Spell
from Baddie import Baddie
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PLAYERSPEED = 5
SPELLSPEED = 8
health = 100
SPELLDAMAGE = 10
BADDIESPEED = 2

WINDOWWIDTH = 700
WINDOWHEIGHT = 700
# Open a new window
size = (WINDOWWIDTH, WINDOWHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wizard Wars")

#set up font
font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 32)

#functions
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
baddie_sprites_list = pygame.sprite.Group()
spell_sprites_list = pygame.sprite.Group()

playerMage = Mage(BLACK,20,30)
playerMage.rect.x = 200
playerMage.rect.y = 300
all_sprites_list.add(playerMage)
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
spell = []
direction = []
kills = 0
baddies = []
max_Baddies= 10
baddie_Counter = 0
previous_time = pygame.time.get_ticks()
drawText('Wizard Wars', font, screen, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, screen, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
drawText('aswd to shoot.', font, screen, (WINDOWWIDTH / 3) - 30, WINDOWHEIGHT-300)
drawText('arrows to move.', font, screen, (WINDOWWIDTH / 3) - 30, WINDOWHEIGHT-200)
pygame.display.update()
waitForPlayerToPressKey()
# -------- Main Program Loop -----------
while carryOn:
    facing = ""
    cast = 0
    moveLeft = moveRight = moveUp = moveDown = False
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
 
        #while running:
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP] and playerMage.rect.y >=0:
        playerMage.moveUp(5)
    if keys[pygame.K_DOWN] and playerMage.rect.y <=WINDOWHEIGHT:
        playerMage.moveDown(5)
    if keys[pygame.K_LEFT] and playerMage.rect.x >=0:
        playerMage.moveLeft(5)
    if keys[pygame.K_RIGHT] and playerMage.rect.x <=WINDOWWIDTH:
        playerMage.moveRight(5)

        #use the aswd keys to shoot
    keyss = pygame.key.get_pressed()
    if keyss[pygame.K_a]:
        facing = "w"
        cast = 1
    if keyss[pygame.K_s]:
        facing = "s"
        cast = 1
    if keyss[pygame.K_w]:
        facing = "n"
        cast = 1
    if keyss[pygame.K_d]:
        facing = "e"
        cast = 1
        
    if cast == 1:    
        current_time = pygame.time.get_ticks()
        if current_time - previous_time > 500:
            playerSpell = Spell(BLACK,20,30)
            playerSpell.rect.x = playerMage.rect.x
            playerSpell.rect.y = playerMage.rect.y
            all_sprites_list.add(playerSpell)
            spell.append(playerSpell)
            direction.append(facing)
            #all_sprites_list.add(playerSpell)
            spell_sprites_list.add(playerSpell)
            previous_time = current_time
            facing = ""

    for s, d in zip(spell, direction):
        if d == "n":
            s.castUp(SPELLSPEED)
            if s.rect.y >= WINDOWHEIGHT:
                spell.remove(s)
                direction.remove(d)
                spell_sprites_list.remove(s)
        if d == "s":
            s.castDown(SPELLSPEED)
            if s.rect.y <= 0:
                spell.remove(s)
                direction.remove(d)
                spell_sprites_list.remove(s)
        if d == "e":
            s.castRight(SPELLSPEED)
            if s.rect.x >= WINDOWWIDTH:
                spell.remove(s)
                direction.remove(d)
                spell_sprites_list.remove(s)
        if d == "w":
            s.castLeft(SPELLSPEED)
                
    ##move baddie to player
    for b in baddie_sprites_list:
        if b.rect.x > playerMage.rect.x:
            b.moveLeft(BADDIESPEED)
        if b.rect.x < playerMage.rect.x:
            b.moveRight(BADDIESPEED)
        if b.rect.y < playerMage.rect.y:
            b.moveDown(BADDIESPEED)
        if b.rect.y > playerMage.rect.y:
            b.moveUp(BADDIESPEED)

    #adding baddies
    if baddie_Counter <= max_Baddies:
        if random.randrange(0, 100)<1:
            if kills > 10:
                newBaddie = Baddie(RED,100,100,30)
                newBaddie.rect.x = random.randrange(0,WINDOWWIDTH)
                newBaddie.rect.y = 0
                baddie_sprites_list.add(newBaddie)
                baddie_Counter += 1
            else:
                newBaddie = Baddie(RED,50,50,10)
                newBaddie.rect.x = random.randrange(0,WINDOWWIDTH)
                newBaddie.rect.y = random.randrange(0,WINDOWHEIGHT)
                baddie_sprites_list.add(newBaddie)
                baddie_Counter += 1
          
        
        
 
    all_sprites_list.update()
    baddie_sprites_list.update()
    spell_sprites_list.update()

    #adding to kill counter and removing baddies
    prev = len(baddie_sprites_list)
    for b in baddie_sprites_list:
        baddie_collision_list = pygame.sprite.spritecollide(b,spell_sprites_list,True,pygame.sprite.collide_mask)
        for baddie in baddie_collision_list:
              b.health -= SPELLDAMAGE
              if b.health <=0:
                baddie_Counter-=1
                baddie_sprites_list.remove(b)
    pygame.sprite.groupcollide(spell_sprites_list, baddie_sprites_list, True, False)

    cur = len(baddie_sprites_list)
    kills+=(prev-cur)
    #checking to see if a baddie has collided with the mage
    mage_collision_list = pygame.sprite.spritecollide(playerMage,baddie_sprites_list,False,pygame.sprite.collide_mask)
    for mage in mage_collision_list:
        print("Dead")
        #End Of Game
        carryOn=False

         
     
            
     # --- Drawing code should go here
     # First, clear the screen to white. 
    screen.fill(BLACK)
    drawText('kills: %s' % (kills), font2, screen, 10, 0)

    #draw all the sprites
    all_sprites_list.draw(screen)
    baddie_sprites_list.draw(screen)
    spell_sprites_list.draw(screen)
     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
     # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
