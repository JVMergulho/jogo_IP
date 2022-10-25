import pygame as pg
import random

class Item(pg.sprite.Sprite):
    def __init__(self, tipo, imagem, player, itens_lista,x,y):

        pg.sprite.Sprite.__init__(self)

        # define o tipo do item: coffee ou energy_drink
        self.type = tipo
        

        # define a sprite que vai ser usada
        self.image = imagem

        self.rect = self.image.get_rect()
        
        self.x = x
        self.y = y

        self.player = player
        self.itens_lista = itens_lista

        # configura a dimensão da imagem e do rect
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect.update(self.x, self.y, 20, 20)

        self.time=0

    def update(self):

        # Faz os itens desaparecerem depois de certo tempo
        self.time+=1

        if self.time>150:
            pg.sprite.Sprite.kill(self)

            self.itens_lista.remove(self)

        # Caso o player toque no item
        if self.rect.colliderect(self.player.rect):
            pg.sprite.Sprite.kill(self)
            
            self.itens_lista.remove(self)

            return self.type
        else:
            return None
