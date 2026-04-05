
import pygame

class World:

    def draw(self,screen,camera):

        for x in range(-2000,4000,80):

            pygame.draw.rect(screen,(100,200,100),(x-camera,560,80,40))

            pygame.draw.rect(screen,(60,60,60),(x-camera,600,80,60))
