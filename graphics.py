import pygame

import map

images = {}
sprites = []
overlay = []
current_map = None


def add_sprite(mobile):
    global sprites
    if mobile not in sprites:
        sprites.append(mobile)


def add_overlay(ui_element):
    global overlay
    if ui_element not in overlay:
        overlay.append(ui_element)


def set_map(newmap):
    global current_map
    current_map = newmap


def del_sprite(mobile):
    global sprites
    if mobile in sprites:
        sprites.remove(mobile)


def del_overlay(ui_element):
    global overlay
    if ui_element in overlay:
        overlay.remove(ui_element)


def draw_map(surface):
    global current_map
    if current_map:
        for x in xrange(current_map.width):
            for y in xrange(current_map.height):
                surface.blit(current_map.sprite_sheet, (x * 16, y * 16), map.map_sprites[current_map[x, y]])


def draw(surface):
    global sprites
    surface.fill(0x000000)
    draw_map(surface)
    for sprite in sprites:
        surface.blit(pygame.transform.flip(sprite.sprite_sheet, sprite.facing, False), (sprite.x, sprite.y),
                     sprite.sprite)
    draw_overlay(surface)

    pygame.display.flip()


def draw_overlay(surface):
    global overlay
    for element in overlay:
        surface.blit(element.img, element.pos)


def load_image(filename):
    global images
    if filename in images:
        return images[filename]

    image = pygame.image.load(filename)
    image.convert()
    images[filename] = image
    return image
