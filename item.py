import pygame as pg
import random

class Item(pg.sprite.Sprite):
    def __init__(self, win):

        pg.sprite.Sprite.__init__(self)

        self.sprites=[]

        self.sprites.append(pg.image.load('assets\coffee.png'))
        self.sprites.append(pg.image.load('assets\energy_drink.png'))
        self.atual= random.randint(0, 1)
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()

        self.image= pg.transform.scale(self.image,(30,30))

        self.x= random.randint(20,600)
        self.y = random.randint(20,600)

        self.rect.update(self.x,self.y,20,20)

    def update(self,rect_player):

        if  self.rect.colliderect(rect_player):
            pg.sprite.Sprite.kill(self)
            print('Tocou')