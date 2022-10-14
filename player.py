import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self,win,x,y,right,left,up,down):

        pg.sprite.Sprite.__init__(self)

        self.sprites = []

        self.sprites.append(pg.image.load('assets\personagem_com_inseticida-1.png'))
        self.sprites.append(pg.image.load('assets\personagem_com_inseticida-2.png'))
        self.sprites.append(pg.image.load('assets\personagem_com_inseticida-3.png'))
        self.sprites.append(pg.image.load('assets\personagem_com_inseticida-2.png'))
        self.atual= 0
        self.image= self.sprites[self.atual]

        self.image = pg.transform.scale(self.image, (64, 64))

        self.rect= self.image.get_rect()
        self.rect.topleft= x,y

        self.win= win
        self.x= x
        self.y= y

        self.rect.update(self.x, self.y, 50, 50)

        self.right= right
        self.left= left
        self.up= up
        self.down= down

        self.vel= 5

    def update(self):
        self.atual= self.atual+0.3
        if self.atual> len(self.sprites):
            self.atual=0
        self.image= self.sprites[int(self.atual)]
        self.image = pg.transform.scale(self.image, (64, 64))
        self.move()

    def move(self):
        keys= pg.key.get_pressed()
        if keys[self.right]:
            self.x+= self.vel
        if keys[self.left]:
            self.x-= self.vel
        if keys[self.up]:
            self.y-= self.vel
        if keys[self.down]:
            self.y+= self.vel
        if keys[pg.K_SPACE]:
            self.x,self.y = 320, 320

        self.image = self.sprites[int(self.atual)]

        self.rect.topleft = self.x, self.y
