import pygame as pg
from player import Player

# Essa é classe dos inimigos

class Bug(pg.sprite.Sprite):
    # Inicializa o inimigo
    def __init__(self,x,y):
        
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('assets\\bug_simples.png')
        
        self.image = pg.transform.scale(self.image, (50,50))

        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.center = self.x,self.y

        self.vel = 3

    # Faz o inimigo se mover em direção ao player
    def update(self, player):
        if player.x < self.x:
            self.x -= self.vel
        elif player.x > self.x:
            self.x += self.vel
        else:
            self.x -= 0
        if player.y > self.y:
            self.y += self.vel
        elif player.y < self.y:
            self.y -= self.vel
        else:
            self.y -= 0
       

        self.rect.center = self.x, self.y




    
