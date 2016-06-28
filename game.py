import os

import pygame

import graphics
import objects
import events
import map

run = True


def quit(e):
    global run
    if (e.type == pygame.QUIT or
            ((e.key == pygame.K_F4) and
                 (e.mod & pygame.KMOD_ALT))):
        run = False


events.register(pygame.QUIT, quit)
events.register(pygame.KEYUP, quit)

pygame.init()

screen = pygame.display.set_mode((400, 400), pygame.DOUBLEBUF | pygame.HWSURFACE)

current_map = map.sample_map()
graphics.set_map(current_map)

slime = objects.Slime()
slime.x = 128
slime.y = 128
# minotaur.move_to(20, 100)
# minotaur.move_to(250, 100)
# minotaur.move_to(100, 150)
events.register(pygame.KEYDOWN, slime.key_handler)
events.register(pygame.KEYUP, slime.key_handler)
graphics.add_sprite(slime)

clock = pygame.time.Clock()
time_ms = 0
clock.tick()
while run:
    time_ms += clock.tick(50)

    while time_ms > 20:
        slime.update()
        time_ms -= 20

    graphics.draw(screen)
    events.handle()

pygame.quit()
