import pygame as pg
import sys
import random
from player import Player
from item import *


def gerar_itens(itens_lista,all_items,player):
    num = random.randint(1,5)

    if random.randint(0,1)==0:
        tipo='coffee'
    else:
        tipo='energy_drink'

    imagens_itens={'coffee':pg.image.load('assets\cafe.gif'),
                   'energy_drink':pg.image.load('assets\energy_drink.png')}

    for i in range(num):
        item = Item(tipo,imagens_itens[tipo],player,itens_lista)
        itens_lista.append(item)
        all_items.add(item)

def main():

    screen = pg.display.set_mode((672, 672))
    clock = pg.time.Clock()
    pg.display.set_caption('Bug Bounty')

    random.seed()

    itens_lista = []

    itens_coletados = {'coffee': 0,
                       'energy_drink': 0,
                       'inseticide': 0}

    player = Player(screen, 320, 320, pg.K_d, pg.K_a, pg.K_w, pg.K_s)
    #player2=Player(screen,300,320,pg.K_RIGHT,pg.K_LEFT,pg.K_UP,pg.K_DOWN)

    all_sprites = pg.sprite.Group()
    all_items = pg.sprite.Group()

    all_sprites.add(player)


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((50, 65, 90))

        all_items.draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()

        for i in itens_lista:
            coletado= i.update()
            if coletado!= None:
                itens_coletados[coletado]+=1
                print(itens_coletados)

        pg.display.flip()
        clock.tick(30)

        #Testando a coleta de itens
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            gerar_itens(itens_lista,all_items,player)

if __name__ == '__main__':
    main()


