import pygame

import map

images = {}
sprites = []
current_map = None


def add_sprite(mobile):
    '''Add an object to the draw list
	'''
    global sprites
    if mobile not in sprites:
        sprites.append(mobile)


def set_map(newmap):
    global current_map
    current_map = newmap


def del_sprite(mobile):
    global sprites
    if mobile in sprites:
        sprites.remove(mobile)


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

    pygame.display.flip()


def load_image(filename):
    global images
    if filename in images:
        return images[filename]

    image = pygame.image.load(filename)
    image.convert()
    images[filename] = image
    return image
