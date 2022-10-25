import pygame as pg
import sys
import random
from pathlib import Path
from player import Player
from item import Item
from enemies import Bug
from random import choice
from item import *
from projectile import Projectile
import math


def gerar_itens(itens_lista, all_items, player, x, y):

    imagens_itens = {'coffee': pg.image.load('assets\cafe.gif'),
                     'energy_drink': pg.image.load('assets\energy_drink.png'),
                     'bit_1': pg.image.load('assets\\bit_1.png'),
                     'bit_0': pg.image.load('assets\\bit_0.png')}

    if random.randint(0, 3) == 0:
        tipo = 'coffee'
    elif random.randint(0, 3) == 1:
        tipo = 'bit_0'
    elif random.randint(0, 3) == 2:
        tipo = 'bit_1'
    else:
        tipo = 'energy_drink'

    item = Item(tipo, imagens_itens[tipo], player, itens_lista, x, y)
    itens_lista.append(item)
    all_items.add(item)


def main():

    # Adiciona música de fundo
    pg.init()

    pg.mixer.music.load('assets\game_music.mp3')
    pg.mixer.music.set_volume(0.7)
    pg.mixer.music.play(-1)

    # sons do jogo
    item_sound = pg.mixer.Sound(Path('assets', 'item_sound.flac'))
    item_sound.set_volume(0.3)

    spray_sound = pg.mixer.Sound(Path('assets', 'spray_sound.wav'))
    spray_sound.set_volume(0.3)

    morte_bug_sound = pg.mixer.Sound(Path('assets', 'morte_bug.wav'))

    # define a variárvel que armazena o padrão RGB para a cor branca
    branco = (255, 255, 255)

    # Configuração para o texto que será exibido
    pg.font.init()

    font = pg.font.get_default_font()
    font_game = pg.font.SysFont(font, 30)

    # inicia o objeto que será a tela do jogo
    screen = pg.display.set_mode((672, 672))
    width, height = 672, 672
    clock = pg.time.Clock()
    pg.display.set_caption('Bug Bounty')

    random.seed()

    itens_lista = []

    all_sprites = pg.sprite.Group()
    all_items = pg.sprite.Group()
    spri_bugs = pg.sprite.Group()

    itens_coletados = {'coffee': 0,
                       'energy_drink': 0,
                       'inseticide': 0,
                       'bit_0': 0,
                       'bit_1': 0,
                       'bugs': 0}
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

    # variavel para controlar o spaw dos bugs
    contador = 0
    gradacao = 0
    # variavel para nao permitir atirar varias vezes ao mesmo tempo
    cooldown = 15

    while True:
        cooldown += 1  # esfriar o inseticida]

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            #
            if event.type == pg.MOUSEBUTTONDOWN and cooldown >= 12:
                bala = Projectile(player)
                all_bullets.append(bala)
                cooldown = 0

                spray_sound.play()

        #
        for balas in all_bullets:  # movimento do gas na tela
            balas.projectile_move()

        # Faz o background aparecer
        screen.blit(pg.image.load(Path('assets', 'background.png')), (0, 0))

        all_items.draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()

        all_items.draw(screen)

        # controla o spam gradativo de bugs
        if contador % 200 == 0:
            gradacao += 1
            if gradacao > 3:
                gradacao = 3
            for i in range(gradacao):
                x_left = random.randint(-40, -10)
                x_right = random.randint(690, 720)
                x = choice([x_left, x_right])
                y = random.randint(50, 600)
                identificar_posicao_bug = {
                    'esquerda': None, 'direita': None, 'em cima': None, 'embaixo': None}
                bug = Bug(x, y)
                all_bugs.append(bug)

        for um_bug in all_bugs:
            um_bug.trace(screen)
            um_bug.update(player, identificar_posicao_bug)

        # Destruindo os projéteis e os bugs quando entram em colisão
        remove_bullets = []
        remove_bugs = []
        for bala in all_bullets:
            bala.destroy = False
            # Condicional para o projétil ser removido quando off-screen
            if (bala.rect.x < 0 or bala.rect.x > width) or (bala.rect.y < 0 or bala.rect.y > height):
                all_bullets.remove(bala)
                print('removi bala')
            for um_bug in all_bugs:
                um_bug.destroy = False
                if bala.destroy == False and um_bug.destroy == False:
                    if bala.rect.colliderect(um_bug.rect):
                        bala.destroy = True
                        um_bug.destroy = True

                        if bala not in remove_bullets:
                            remove_bullets.append(bala)
                        if um_bug not in remove_bugs:
                            remove_bugs.append(um_bug)

                        itens_coletados['bugs'] += 1

        for bala in remove_bullets:
            all_bullets.remove(bala)

        for um_bug in remove_bugs:
            all_bugs.remove(um_bug)
            morte_bug_sound.play()  # Efeito sonoro da coleta de item

            # Tem uma chance de gerar um item no lugar onde o bug morre
            if random.randint(0, 2) == 1:
                gerar_itens(itens_lista, all_items, player, um_bug.x, um_bug.y)

        # Inserir os itens coletados,bugs mortos e a pontuação na tela
        text_coffee = font_game.render(
            f'X {itens_coletados["coffee"]}', 1, branco)
        text_energy_drink = font_game.render(
            f'X {itens_coletados["energy_drink"]}', 1, branco)
        text_bugs = font_game.render(
            f'X {itens_coletados["bugs"]}', 1, branco)
        # Pontuação:Um bug  vale 1 ponto e cada bit vale 5 pontos
        text_pontuacao = font_game.render(
            f'Pontuação: {(itens_coletados["bit_0"] + itens_coletados["bit_1"])*5 + itens_coletados["bugs"]}', 1, branco)

        screen.blit(text_pontuacao, (270, 10))
        screen.blit(pg.transform.scale(pg.image.load(
            'assets\\bug_simples.png'), (40, 35)), (20, 105))
        screen.blit(text_bugs, (70, 115))

        screen.blit(pg.transform.scale(pg.image.load(
            Path('assets', 'cafe.gif')), (40, 35)), (20, 20))
        screen.blit(text_coffee, (70, 35))

        screen.blit(pg.transform.scale(pg.image.load(
            Path('assets', 'energy_drink.png')), (35, 35)), (25, 65))
        screen.blit(text_energy_drink, (70, 75))

        for balas in all_bullets:  # desenha o projetil gas na tela
            balas.trace(screen)

        # Atualiza o dicionário de itens coletados
        for i in itens_lista:
            coletado = i.update()
            if coletado != None:
                itens_coletados[coletado] += 1
                print(itens_coletados)

                item_sound.play()  # Efeito sonoro da coleta de item

        pg.display.flip()
        clock.tick(30)
        contador += 1

        # Testando a coleta de itens
        keys = pg.key.get_pressed()


if __name__ == '__main__':
    main()
