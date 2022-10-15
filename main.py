import pygame as pg
import sys
import random
from player import Player
from item import *


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
    clock = pg.time.Clock()
    pg.display.set_caption('Bug Bounty')

    random.seed()

    itens_lista = []

    itens_coletados = {'coffee': 0,
                       'energy_drink': 0,
                       'inseticide': 0}

    player = Player(screen, 320, 320, pg.K_d, pg.K_a, pg.K_w, pg.K_s)
    # player2=Player(screen,300,320,pg.K_RIGHT,pg.K_LEFT,pg.K_UP,pg.K_DOWN)

    all_sprites = pg.sprite.Group()
    all_items = pg.sprite.Group()

    all_sprites.add(player)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # Faz o background aparecer
        screen.blit(pg.image.load('assets\\background.png'), (0, 0))

        all_items.draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()

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

        for i in itens_lista:
            coletado = i.update()
            if coletado != None:
                itens_coletados[coletado] += 1
                print(itens_coletados)

        pg.display.flip()
        clock.tick(30)

        # Testando a coleta de itens
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            gerar_itens(itens_lista, all_items, player)


if __name__ == '__main__':
    main()
