import os

import graphics

# 30 x 33
map_sprites = [((i % 30) * 16, (i / 30) * 16, 16, 16) for i in xrange(990)]

c = [i for i in xrange(30, 30 + 57)]
w = [i for i in xrange(120, 120 + 18)]
f = [i for i in xrange(210, 210 + 72)]


class Map(object):
    def __init__(self, x, y):
        self.width = x
        self.height = y
        self._map = [0 for i in xrange(x * y)]
        self.sprite_sheet = graphics.load_image(os.path.join("img", "dungeon tileset calciumtrice.png"))

    def __getitem__(self, coords):
        (x, y) = coords
        return self._map[x + y * self.width]

    def __setitem__(self, coords, val):
        (x, y) = coords
        self._map[x + y * self.width] = val

    def __str__(self):
        out = []
        for i in xrange(self.height):
            out.append(", ".join([str(s) for s in self._map[i * self.width: i * self.width + self.width]]))

        return "\n".join(out)


def sample_map():
    smap = Map(10, 10)
    map_data = [
        w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[5], w[4], w[3],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2],
        w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[5], w[4], w[3],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2],
        w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[5], w[4], w[3],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2],
        w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[5], w[4], w[3],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2],
        w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[5], w[4], w[3],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2],
        w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[5], w[4], w[3],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2],
        w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[5], w[4], w[3],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2],
        w[0], w[1], w[2], w[3], w[4], w[5], w[6], w[5], w[4], w[3],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2],
        w[3], w[2], w[1], w[2], w[4], w[5], w[4], w[6], w[0], w[2]
    ]

    for y in xrange(10):
        for x in xrange(10):
            smap[x, y] = map_data[x + y * 10]

    return smap
