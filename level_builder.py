import json
from tile import Tile
from pygame.sprite import Group
from pygame import Rect
from factory.map_image_factory import MapImageFactory
from pygame import Surface
from dot import Dot
from energizer import Energizer


class LevelBuilder:

    def __init__(self, level_file, screen_size):
        self.__platforms = Group()
        self.__dots = Group()
        self.images = []
        self.map_factory = MapImageFactory()
        self.backround = Surface(screen_size)
        with open(level_file) as f:
            self.data = json.load(f)
        self.world_size = Rect(
            0,
            0,
            self.data['width'] * self.data['tilewidth'],
            self.data['height'] * self.data['tileheight']
        )

    def build(self):
        layer = self.data['layers'][0]
        x = 0
        y = 3
        for item in layer['data']:
            if item == 0:
                pass
            if item == 1:
                self.build_platform(x, y)
            x += 1
            if x > layer['width'] - 1:
                x = 0
                y += 1

        self.map_factory.create()
        layer2 = self.data['layers'][1]
        x = 0
        y = 3
        for item in layer2['data']:
            self.build_backround(x, y, item)
            x += 1
            if x > layer['width'] - 1:
                x = 0
                y += 1
        # dots
        layer3 = self.data['layers'][2]
        x = 0
        y = 3
        for item in layer3['data']:
            self.build_dots(x, y, item)
            x += 1
            if x > layer['width'] - 1:
                x = 0
                y += 1
        # big dots
        layer4 = self.data['layers'][3]
        x = 0
        y = 3
        for item in layer4['data']:
            self.build_big_dots(x, y, item)
            x += 1
            if x > layer['width'] - 1:
                x = 0
                y += 1

    def build_platform(self, x, y):
        Tile(x * 8, y * 8, self.__platforms)

    def build_backround(self, x, y, item):
        if item == 0:
            return
        image = self.map_factory.get_image(item)
        self.backround.blit(image, (x * 8, y * 8))

    def build_dots(self, x, y, item):
        if item == 0:
            return
        tile = Dot(x * 8, y * 8, self.__dots)
        image = self.map_factory.get_image(item)
        tile.set_image(image)

    def build_big_dots(self, x, y, item):
        if item == 0:
            return
        tile = Energizer(x * 8, y * 8, self.__dots)
        image = self.map_factory.get_image(item)
        tile.set_image(image)

    def get_platforms(self):
        return self.__platforms

    def get_background(self):
        return self.backround

    def get_dots(self):
        return self.__dots

    def get_world_size(self):
        return self.world_size
