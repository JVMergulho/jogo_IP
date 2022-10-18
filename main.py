import pygame as pg
import sys
import random
from player import Player
from item import Item
from enemies import Bug
from random import choice
from item import *
from projectile import Projectile

def gerar_itens(itens_lista, all_items, player):
    num = random.randint(1, 5)

    imagens_itens = {'coffee': pg.image.load('assets\cafe.gif'),
                     'energy_drink': pg.image.load('assets\energy_drink.png')}

    for i in range(num):

        if random.randint(0, 1) == 0:
            tipo = 'coffee'
        else:
            tipo = 'energy_drink'

        item = Item(tipo, imagens_itens[tipo], player, itens_lista)
        itens_lista.append(item)
        all_items.add(item)


def main():

    # Adiciona música de fundo
    pg.init()

    game_music = pg.mixer.music.load('assets\game_music.mp3')
    pg.mixer.music.play(-1)

    # define a variárvel que armazena o padrão RGB para a cor branca
    branco = (255, 255, 255)

    # Configuração para o texto que será exibido
    pg.font.init()

    font = pg.font.get_default_font()
    font_game = pg.font.SysFont(font, 30)

    # inicia o objeto que será a tela do jogo
    screen = pg.display.set_mode((672, 672))
    width,height = 672,672
    clock = pg.time.Clock()
    pg.display.set_caption('Bug Bounty')

    random.seed()

    itens_lista = []

    all_sprites= pg.sprite.Group()
    all_items = pg.sprite.Group()
    #all_bugs = pg.sprite.Group()
    spri_bugs = pg.sprite.Group()

    itens_coletados = {'coffee': 0,
                       'energy_drink': 0,
                       'inseticide': 0}

    player = Player(screen, 320, 320, pg.K_d, pg.K_a, pg.K_w, pg.K_s)
    # player2=Player(screen,300,320,pg.K_RIGHT,pg.K_LEFT,pg.K_UP,pg.K_DOWN)

    all_sprites = pg.sprite.Group()
    all_items = pg.sprite.Group()

    #
    all_bullets = []
    #

    # Lista com todos os bugs
    all_bugs = []

    all_sprites.add(player)

    #variavel para controlar o spaw dos bugs
    contador = 0
    #variavel para nao permitir atirar varias vezes ao mesmo tempo
    cooldown = 15

    while True:
        cooldown += 1 #esfriar o inseticida
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            #
            if event.type == pg.MOUSEBUTTONDOWN and cooldown >= 15:
                bala = Projectile(player)
                all_bullets.append(bala)
                cooldown = 0

        #
        for balas in all_bullets: #movimento do gas na tela
            balas.projectile_move()
        #

        #

        # Faz o background aparecer
        screen.blit(pg.image.load('assets\\background.png'), (0, 0))

        all_items.draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()

        all_items.draw(screen)
        
        if contador%150 == 0:
            for i in range(4):
                x_left = random.randint(-40, -10)
                x_right = random.randint(690,720)
                x = choice([x_left, x_right])
                y = random.randint(50,600)
                bug = Bug(x,y)
                #all_bugs.add(bug)
                all_bugs.append(bug)
        for um_bug in all_bugs:
            um_bug.trace(screen)
            um_bug.update(player)

        #all_bugs.draw(screen)
        #all_bugs.update(player)

        #Destruindo as balas e os bugs quando entram em colisão
        remove_bullets = []
        remove_bugs = []
        for bala in all_bullets:
            bala.destroy = False
            if (bala.rect.x < 0 or bala.rect.x > width) or bala.rect.y < 0 or bala.rect.y > height:
                all_bullets.remove(bala)
            for um_bug in all_bugs:
                um_bug.destroy = False
                if bala.destroy == False and um_bug.destroy == False:
                    if bala.rect.colliderect(um_bug.rect):
                        bala.destroy = True
                        um_bug.destroy = True
                        remove_bullets.append(bala)
                        remove_bugs.append(um_bug)

        for bala in remove_bullets:
            all_bullets.remove(bala)
        for um_bug in remove_bugs:
            all_bugs.remove(um_bug)


        # Inserir os itens coletados na tela
        text_coffee = font_game.render(
            f'X {itens_coletados["coffee"]}', 1, branco)
        text_energy_drink = font_game.render(
            f'X {itens_coletados["energy_drink"]}', 1, branco)

        screen.blit(pg.transform.scale(pg.image.load(
            'assets\cafe.gif'), (40, 35)), (20, 20))
        screen.blit(text_coffee, (70, 35))

        screen.blit(pg.transform.scale(pg.image.load(
            'assets\energy_drink.png'), (35, 35)), (25, 65))
        screen.blit(text_energy_drink, (70, 75))

        for balas in all_bullets: #desenha o projetil gas na tela
            balas.trace(screen)

            #Destruindo as balas que saíram da tela
            # if (bala.rect.x > width or bala.rect.x < 0) or (bala.rect.y > height or bala.rect.y < 0):
            #     all_bullets.remove(bala)
            #     print('removi bala')


        for i in itens_lista:
            coletado = i.update()
            if coletado != None:
                itens_coletados[coletado] += 1
                print(itens_coletados)

        pg.display.flip()
        clock.tick(30)
        contador += 1


        # Testando a coleta de itens
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            gerar_itens(itens_lista, all_items, player)


if __name__ == '__main__':
    main()