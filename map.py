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
        c[0], c[0], c[0], c[0], c[0], c[0], c[0], c[0], c[0], c[0],
        c[0], c[52], c[11], c[12], c[13], c[11], c[12], c[13], c[51], c[0],
        c[0], c[14], f[1], f[8], f[9], f[10], f[8], f[2], c[5], c[0],
        c[0], c[15], f[7], f[65], f[61], f[61], f[63], f[14], c[6], c[0],
        c[0], c[16], f[6], f[68], f[67], f[64], f[66], f[15], c[7], c[0],
        c[0], c[14], f[5], f[64], f[61], f[63], f[61], f[16], c[5], c[0],
        c[0], c[15], f[7], f[61], f[66], f[65], f[68], f[14], c[6], c[0],
        c[0], c[16], f[3], f[11], f[12], f[13], f[11], f[4], c[7], c[0],
        c[0], c[50], c[9], c[8], c[9], c[10], c[9], c[10], c[49], c[0],
        c[0], c[0], c[0], c[0], c[0], c[0], c[0], c[0], c[0], c[0],
    ]

    for y in xrange(10):
        for x in xrange(10):
            smap[x, y] = map_data[x + y * 10]

    return smap
