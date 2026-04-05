
import pygame
from entities.player import Player
from entities.npc import NPC
from entities.bullet import Bullet
from world.map import World
from ui.hud import HUD
from ui.minimap import MiniMap

class Game:

    def __init__(self, screen):

        self.screen = screen

        self.world = World()

        self.player = Player(300,500)

        self.npcs = [NPC(800+i*150,500) for i in range(6)]

        self.bullets = []

        self.hud = HUD()

        self.minimap = MiniMap()

    def handle_event(self,event):

        bullet = self.player.handle_event(event)

        if bullet:
            self.bullets.append(bullet)

    def update(self,dt):

        self.player.update(dt)

        for npc in self.npcs:
            npc.update(dt,self.player)

        for bullet in self.bullets:
            bullet.update(dt)

        # bullet collision
        for bullet in self.bullets:
            for npc in self.npcs:
                if npc.rect.colliderect(bullet.rect):
                    npc.health -= 50
                    bullet.dead = True

        self.bullets = [b for b in self.bullets if not b.dead]

        self.npcs = [n for n in self.npcs if n.health > 0]

    def draw(self):

        camera = self.player.rect.centerx - 600

        self.screen.fill((120,200,255))

        self.world.draw(self.screen,camera)

        for npc in self.npcs:
            npc.draw(self.screen,camera)

        for bullet in self.bullets:
            bullet.draw(self.screen,camera)

        self.player.draw(self.screen,camera)

        self.hud.draw(self.screen,self.player)

        self.minimap.draw(self.screen,self.player,self.npcs)
