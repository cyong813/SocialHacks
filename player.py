import pygame

class Player:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.width=32
        self.height=32
        self.velocity=0

    def update(self, gravity):
        self.velocity+=gravity
        self.y-=self.velocity

    def render(self, window):
        pygame.draw.rect(window, (0,0,0), (self.x, self.y, self.width, self.height))
