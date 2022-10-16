import pygame as pg
import sys
import random
from player import Player
from item import Item
from enemies import Bug
from random import choice

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
    all_bugs = pg.sprite.Group()

   

    gerar_itens(screen,all_items)

    all_sprites.add(player)
    #all_sprites.add(player2)
    #all_sprites.add(player3)

    #variavel para controlar o spaw dos bugs
    contador = 0

    while True:
        for event in pg.event.get():
            if event.type== pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((50, 80, 90))

        all_sprites.draw(screen)
        all_sprites.update()

        all_items.update(player.rect)
        all_items.draw(screen)
        
        if contador%150 == 0:
            for i in range(4):
                x_left = random.randint(-40, -10)
                x_right = random.randint(690,720)
                x = choice([x_left, x_right])
                y = random.randint(50,600)
                bug = Bug(x,y)
                all_bugs.add(bug)
        all_bugs.draw(screen)
        all_bugs.update(player)

        pg.display.flip()
        clock.tick(30)
        contador += 1


        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            gerar_itens(screen, all_items)


if __name__ == '__main__':
    main()
