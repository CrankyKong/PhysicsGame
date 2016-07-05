
import pygame

class Button(object):
    def __init__(self, left, top, width, height, img):
        self.pos = pygame.Rect(left, top, width, height)
        self.img = img

    def click_handler(self, e):
        if (e.button == 1 and self.pos.collidepoint(e.pos)):
            print("Clicked")

