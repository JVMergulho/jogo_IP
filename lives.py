import pygame as pg
from pathlib import Path


class Lives(pg.sprite.Sprite):

    def __init__(self, win):

        self.qtd = 4
        self.image = pg.image.load(Path('assets', 'cafe.gif'))
        self.image = pg.transform.scale(self.image, (40, 35))
        self.screen = win

    def draw(self):

        for i in range(self.qtd):
            self.screen.blit(self.image, (20 + i*30, 20))
