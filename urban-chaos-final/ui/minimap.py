
import pygame

class MiniMap:

    def draw(self,screen,player,npcs):

        pygame.draw.rect(screen,(0,0,0),(980,20,200,140))

        px = 980 + (player.rect.x % 200)
        py = 20 + (player.rect.y % 140)

        pygame.draw.circle(screen,(0,255,0),(px,py),4)

        for npc in npcs:
            nx = 980 + (npc.rect.x % 200)
            ny = 20 + (npc.rect.y % 140)

            pygame.draw.circle(screen,(255,0,0),(nx,ny),3)
