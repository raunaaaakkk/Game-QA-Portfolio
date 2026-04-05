
import pygame
from settings import BULLET_SPEED

class Bullet:

    def __init__(self,x,y):

        self.rect = pygame.Rect(x,y,10,4)

        self.speed = BULLET_SPEED

        self.dead = False

    def update(self,dt):

        self.rect.x += self.speed * dt

        if self.rect.x > 5000:
            self.dead = True

    def draw(self,screen,camera):

        pygame.draw.rect(screen,(255,220,0),(self.rect.x-camera,self.rect.y,10,4))
