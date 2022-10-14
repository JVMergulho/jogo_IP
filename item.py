import pygame as pg
import random

class Item(pg.sprite.Sprite):
    def __init__(self):

        pg.sprite.Sprite.__init__(self)

        self.rect = self.image.get_rect()
        self.image= pg.transform.scale(self.image,(30,30))

        self.x= random.randint(20,600)
        self.y = random.randint(20,600)

        self.rect.update(self.x,self.y,20,20)

    def update(self,player):

        if  self.rect.colliderect(player.rect):
            pg.sprite.Sprite.kill(self)
            print('Tocou')

class Coffee(Item):

    def __init__(self):
        Item.__init__(self)
        Item.image = pg.image.load('assets\cafe.gif')

class Energy_drink(Item):

    def __init__(self):
        Item.__init__(self)
        self.image = pg.image.load('assets\energy_drink.png')