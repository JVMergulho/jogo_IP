import pygame as pg
import sys

class Player(pg.sprite.Sprite):
    def __init__(self,win,x,y,right,left,up,down):
        pg.sprite.Sprite.__init__(self)

        self.sprites = []

        self.sprites.append(pg.image.load('assets\personagem_com_inseticida-2.png'))
        self.sprites.append(pg.image.load('assets\personagem_com_inseticida-1.png'))
        self.sprites.append(pg.image.load('assets\personagem_com_inseticida-2.png'))
        self.sprites.append(pg.image.load('assets\personagem_com_inseticida-3.png'))

        self.atual= 0
        self.image= self.sprites[self.atual]

        self.rect= self.image.get_rect()
        self.rect.topleft= x,y

        self.win= win
        self.x= x
        self.y= y
        self.right= right
        self.left= left
        self.up= up
        self.down= down

        self.largura= 20
        self.altura= 20
        self.vel= 10

    def update(self):
        self.atual= self.atual+0.3
        if self.atual> len(self.sprites):
            self.atual=0
        self.image= self.sprites[int(self.atual)]
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

        self.rect.topleft = self.x, self.y

def main():
    screen= pg.display.set_mode((672,672))
    clock= pg.time.Clock()
    pg.display.set_caption('Bug Bounty')

    player= Player(screen,370,320,pg.K_d,pg.K_a,pg.K_w,pg.K_s)
    player2=Player(screen,300,320, pg.K_RIGHT,pg.K_LEFT,pg.K_UP,pg.K_DOWN)

    all_sprites= pg.sprite.Group()

    all_sprites.add(player)
    all_sprites.add(player2)

    while True:
        for event in pg.event.get():
            if event.type== pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((60, 100, 130))

        all_sprites.draw(screen)
        all_sprites.update()

        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
