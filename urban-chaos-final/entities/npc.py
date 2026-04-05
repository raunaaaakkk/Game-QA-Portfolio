
import pygame, random
from settings import NPC_SPEED

class NPC:

    def __init__(self,x,y):

        self.image = pygame.Surface((40,60))
        self.image.fill((200,80,80))

        self.rect = self.image.get_rect(topleft=(x,y))

        self.direction = random.choice([-1,1])

        self.health = 100

    def update(self,dt,player):

        self.rect.x += self.direction * NPC_SPEED * dt

        if random.randint(0,200) < 2:
            self.direction *= -1

    def draw(self,screen,camera):

        screen.blit(self.image,(self.rect.x-camera,self.rect.y))
