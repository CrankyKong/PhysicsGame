import sys

import pygame

handlers = {
    pygame.QUIT: [],
    pygame.KEYUP: [],
    pygame.KEYDOWN: [],
}


def register(e_type, handler):
    if handler not in handlers[e_type]:
        handlers[e_type].append(handler)


def handle():
    global handlers
    for e in pygame.event.get():
        if e.type in handlers:
            for handler in handlers[e.type]:
                handler(e)
