
import pygame, sys
from game import Game
from settings import WIDTH, HEIGHT, FPS

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Urban Chaos Final")

clock = pygame.time.Clock()

game = Game(screen)

while True:

    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        game.handle_event(event)

    game.update(dt)
    game.draw()

    pygame.display.flip()
