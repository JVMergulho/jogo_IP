import pygame as pg

class Bug(pg.sprite.Sprite):
    def __init__(self,x,y):
        
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('assets\\bug_simples.png')
        
        self.image = pg.transform.scale(self.image, (50,50))

        self.x= x
        self.y= y

        self.rect = self.image.get_rect()
        self.rect.center = self.x,self.y

       


    
