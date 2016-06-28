import os
import math

import pygame

import graphics

RIGHT = True
LEFT = False


class Mobile(object):
    def __init__(self, sprite_sheet=None):
        self.x = 0
        self.y = 0
        self.sprite_sheet = sprite_sheet
        self.sprite = (0, 0, 0, 0)

    def move(self, src, dest, speed):
        diff_v = (dest[0] - src[0], dest[1] - src[1])
        norm = math.sqrt(diff_v[0] ** 2 + diff_v[1] ** 2)

        if norm <= speed:
            return dest

        scalar = speed / norm
        move_v = (diff_v[0] * scalar, diff_v[1] * scalar)

        return src[0] + move_v[0], src[1] + move_v[1]


class Actions(object):
    IDLE = 0
    ROLL = 1
    JUMP = 2
    ATTACK = 3
    DIE = 4


class Dir(object):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 4
    RIGHT = 8


class Slime(Mobile):
    frames = {
        Actions.IDLE:   [((9 - x) * 32, 32 * 0, 32, 32) for x in xrange(0, 10)],
        Actions.ROLL:   [((9 - x) * 32, 32 * 1, 32, 32) for x in xrange(0, 10)],
        Actions.JUMP:   [((9 - x) * 32, 32 * 2, 32, 32) for x in xrange(0, 10)],
        Actions.ATTACK: [((9 - x) * 32, 32 * 3, 32, 32) for x in xrange(0, 10)],
        Actions.DIE:    [((9 - x) * 32, 32 * 4, 32, 32) for x in xrange(0, 10)],
    }

    def __init__(self):
        super(Slime, self).__init__(graphics.load_image(os.path.join("img", "slime spritesheet calciumtrice.png")))
        self.sprite = (0, 0, 32, 32)
        self.waypoints = []

        self.speed = 2
        self.frame = 0.0
        self.facing = RIGHT
        self.action = Actions.IDLE

        self.dir = Dir.NONE

    def attack(self):
        self.action = Actions.ATTACK

    def walk(self):
        self.action = Actions.JUMP
        if self.dir & Dir.UP:
            self.y = self.y - self.speed
        if self.dir & Dir.DOWN:
            self.y = self.y + self.speed
        if self.dir & Dir.LEFT:
            self.x = self.x - self.speed
        if self.dir & Dir.RIGHT:
            self.x = self.x + self.speed

    def move_to(self, x, y):
        self.action = Actions.ROLL
        self.waypoints.append((x, y))

    def key_handler(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                self.dir = self.dir | Dir.UP
            elif e.key == pygame.K_DOWN:
                self.dir = self.dir | Dir.DOWN
            elif e.key == pygame.K_LEFT:
                self.dir = self.dir | Dir.LEFT
            elif e.key == pygame.K_RIGHT:
                self.dir = self.dir | Dir.RIGHT
        else:  # This should be e.type == pygame.KEYUP
            if e.key == pygame.K_UP:
                self.dir = self.dir & ~Dir.UP
            elif e.key == pygame.K_DOWN:
                self.dir = self.dir & ~Dir.DOWN
            elif e.key == pygame.K_LEFT:
                self.dir = self.dir & ~Dir.LEFT
            elif e.key == pygame.K_RIGHT:
                self.dir = self.dir & ~Dir.RIGHT

    def update(self):
        self.walk()

        #		if self.waypoints:
        #			self.facing = self.waypoints[0][0] > self.x
        #			(self.x, self.y) = self.move((self.x, self.y), self.waypoints[0], self.speed)
        #			if (self.x, self.y) == self.waypoints[0]:
        #				self.waypoints.pop(0)
        #		else:
        #			self.action = Actions.IDLE

        self.frame = (self.frame + 0.3) % 10
        self.sprite = self.frames[self.action][int(self.frame)]
