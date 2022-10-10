import pygame as pg
import sys
import random

class Item(pg.sprite.Sprite):
    def __init__(self, win):

        pg.sprite.Sprite.__init__(self)

        self.sprites=[]

        self.sprites.append(pg.image.load('assets\coffe.png'))
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

def gerar_itens(screen,all_items):
    num = random.randint(1, 5)

    for i in range(num):
        item = Item(screen)
        all_items.add(item)

def main():
    screen= pg.display.set_mode((672,672))
    clock= pg.time.Clock()
    pg.display.set_caption('Bug Bounty')

    random.seed()

    player= Player(screen,320,320,pg.K_d,pg.K_a,pg.K_w,pg.K_s)
    #player2=Player(screen,300,320,pg.K_RIGHT,pg.K_LEFT,pg.K_UP,pg.K_DOWN)
    #player3 = Player(screen, 250, 320, pg.K_k, pg.K_h, pg.K_u, pg.K_j)

    all_sprites= pg.sprite.Group()
    all_items = pg.sprite.Group()

    gerar_itens(screen,all_items)

    all_sprites.add(player)
    #all_sprites.add(player2)
    #all_sprites.add(player3)

    while True:
        for event in pg.event.get():
            if event.type== pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((50, 65, 90))

        all_sprites.draw(screen)
        all_sprites.update()

        all_items.update(player.rect)
        all_items.draw(screen)

        pg.display.flip()
        clock.tick(30)

        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            gerar_itens(screen, all_items)


if __name__ == '__main__':
    main()
