import pygame
WHITE = (255, 255, 255)
 
class Baddie(pygame.sprite.Sprite):


    def __init__(self, color, width, height,health):
        # Call the parent class (Sprite) constructor
        super().__init__()
        baddie = pygame.image.load("jack2.png")
        baddie = pygame.transform.scale(baddie, (width, height))
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = baddie.convert_alpha()
        self.health = health
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def moveRight(self, pixels):
        self.rect.x += pixels
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    def moveUp(self, pixels):
        self.rect.y -= pixels
    def moveDown(self, pixels):
        self.rect.y += pixels

