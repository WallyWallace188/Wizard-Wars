import pygame
WHITE = (255, 255, 255)
 
class Spell(pygame.sprite.Sprite):


    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        spell = pygame.image.load("flame_up.png")
        spell = pygame.transform.scale(spell, (20, 20))
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = spell.convert_alpha()
     
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def castRight(self, pixels):
        self.rect.x += pixels
        spell = pygame.image.load("flame_right.png")
        spell = pygame.transform.scale(spell, (20, 20))
        self.image = spell.convert_alpha()
    def castLeft(self, pixels):
        self.rect.x -= pixels
        spell = pygame.image.load("flame_left.png")
        spell = pygame.transform.scale(spell, (20, 20))
        self.image = spell.convert_alpha()
    def castUp(self, pixels):
        self.rect.y -= pixels
        spell = pygame.image.load("flame_up.png")
        spell = pygame.transform.scale(spell, (20, 20))
        self.image = spell.convert_alpha()
    def castDown(self, pixels):
        self.rect.y += pixels
        spell = pygame.image.load("flame_down.png")
        spell = pygame.transform.scale(spell, (20, 20))
        self.image = spell.convert_alpha()
