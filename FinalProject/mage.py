import pygame
WHITE = (255, 255, 255)
 
class Mage(pygame.sprite.Sprite):


    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        mage = pygame.image.load("tile006.png")
        mage = pygame.transform.scale(mage, (40, 30))
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = mage.convert_alpha()
     
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        	
        self.mask = pygame.mask.from_surface(self.image)
        
    def moveRight(self, pixels):
        self.rect.x += pixels
        mage = pygame.image.load("tile003.png")
        mage = pygame.transform.scale(mage, (40, 30))
        self.image = mage.convert_alpha()
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        mage = pygame.image.load("tile009.png")
        mage = pygame.transform.scale(mage, (40, 30))
        self.image = mage.convert_alpha()
    def moveUp(self, pixels):
        self.rect.y -= pixels
        mage = pygame.image.load("tile002.png")
        mage = pygame.transform.scale(mage, (40, 30))
        self.image = mage.convert_alpha()
    def moveDown(self, pixels):
        self.rect.y += pixels
        mage = pygame.image.load("tile006.png")
        mage = pygame.transform.scale(mage, (40, 30))
        self.image = mage.convert_alpha()
