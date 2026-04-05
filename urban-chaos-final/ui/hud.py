
import pygame

class HUD:

    def __init__(self):

        self.font = pygame.font.SysFont(None,28)

    def draw(self,screen,player):

        pygame.draw.rect(screen,(200,0,0),(20,20,200,20))

        pygame.draw.rect(screen,(0,200,0),(20,20,2*player.health,20))

        text = self.font.render("Health",True,(0,0,0))

        screen.blit(text,(20,0))
