import pygame as pg
import sys
import random
from player import Player
from item import *


def gerar_itens(screen,all_items):
    qtd = random.randint(1, 5)
    num_item = random.randint(0,1)

    for i in range(qtd):
        if num_item==1:
            item = Coffee()
        else:
            item =Energy_drink()
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