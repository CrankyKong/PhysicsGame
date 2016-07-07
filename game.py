import os

import pygame

import graphics
import objects
import events
import map
import id
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
slime.x = 200
slime.y = 200

platform = objects.Platform()
platform.x = 200
platform.y = 250
# platform.move_to(20, 100)
# minotaur.move_to(250, 100)
# minotaur.move_to(100, 150)
events.register(pygame.KEYDOWN, slime.key_handler)
events.register(pygame.KEYUP, slime.key_handler)
graphics.add_sprite(slime)
graphics.add_sprite(platform)

clock = pygame.time.Clock()
time_ms = 0
clock.tick()

button = id.Button(10, 10, 32, 32, graphics.load_image(os.path.join("img", "info.png")))
graphics.add_overlay(button)
events.register(pygame.MOUSEBUTTONUP, button.click_handler)



while run:
    time_ms += clock.tick(50)

    while time_ms > (20):
        slime.update()
        time_ms -= 20

    graphics.draw(screen)
    events.handle()

pygame.quit()
