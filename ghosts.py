import funcs
import pygame

pygame.init()

Blue = pygame.image.load('C:\\Users\\Admin\\Pictures\\Saved Pictures\\ghost1.jpg')
blue = pygame.transform.scale(Blue, (40, 40))
Pink = pygame.image.load('C:\\Users\\Admin\\Pictures\\Saved Pictures\\ghost2.jpg')
pink = pygame.transform.scale(Pink, (40, 40))
Red = pygame.image.load('C:\\Users\\Admin\\Pictures\\Saved Pictures\\ghost3.jpg')
red = pygame.transform.scale(Red, (40, 40))
Orange = pygame.image.load('C:\\Users\\Admin\\Pictures\\Saved Pictures\\ghost4.jpg')
orange = pygame.transform.scale(Orange, (40, 40))
Scared = pygame.image.load('C:\\Users\\Admin\\Pictures\\Saved Pictures\\scard_ghost.jpg')
scared = pygame.transform.scale(Scared, (40, 40))

class Ghost:
    current_direction = None
    out = False
    run = False

    def __init__(self, color, height, width, horizontal, vertical, home_x, home_y):
        self.color = color
        self.height = height
        self.width = width
        self.horizontal = horizontal
        self.vertical = vertical
        self.home_x = home_x
        self.home_y = home_y

    def which_ghost(self):
        if self.run is True:
            return scared
        else:
            if self.color == 'blue':
                return blue
            elif self.color == 'pink':
                return pink
            elif self.color == 'red':
                return red
            elif self.color == 'orange':
                return orange
