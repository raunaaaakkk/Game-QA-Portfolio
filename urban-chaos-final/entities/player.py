
import pygame
from settings import PLAYER_SPEED
from entities.bullet import Bullet

class Player:

    def __init__(self,x,y):

        self.image = pygame.Surface((40,60))
        self.image.fill((40,120,255))

        self.rect = self.image.get_rect(topleft=(x,y))

        self.vel = pygame.Vector2(0,0)

        self.health = 100

    def handle_event(self,event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_f:
                return Bullet(self.rect.centerx,self.rect.centery)

        return None

    def update(self,dt):

        keys = pygame.key.get_pressed()

        self.vel.x = 0
        self.vel.y = 0

        if keys[pygame.K_w]:
            self.vel.y = -PLAYER_SPEED

        if keys[pygame.K_s]:
            self.vel.y = PLAYER_SPEED

        if keys[pygame.K_a]:
            self.vel.x = -PLAYER_SPEED

        if keys[pygame.K_d]:
            self.vel.x = PLAYER_SPEED

        self.rect.x += self.vel.x * dt
        self.rect.y += self.vel.y * dt

    def draw(self,screen,camera):

        screen.blit(self.image,(self.rect.x-camera,self.rect.y))
