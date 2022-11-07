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
from lives import Lives
import menu


def gerar_itens(itens_lista, all_items, player, x, y):

    imagens_itens = {'coffee': pg.image.load(Path('assets', 'cafe.gif')),
                     'energy_drink': pg.image.load(Path('assets', 'energy_drink.png')),
                     'bit_1': pg.image.load(Path('assets', 'bit_1.png')),
                     'bit_0': pg.image.load(Path('assets', 'bit_0.png'))}

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

    # Inicializa o pygame
    pg.init()

    # carrega e inicia a música do jogo
    pg.mixer.music.load(Path('assets', 'game_music.mp3'))
    pg.mixer.music.set_volume(0.7)
    pg.mixer.music.play(-1)

    # sons do jogo
    item_sound = pg.mixer.Sound(Path('assets', 'item_sound.flac'))
    item_sound.set_volume(0.3)

    spray_sound = pg.mixer.Sound(Path('assets', 'spray_sound.wav'))
    spray_sound.set_volume(0.3)

    morte_bug_sound = pg.mixer.Sound(Path('assets', 'morte_bug.wav'))

    # define a variável que armazena o padrão RGB para a cor branca
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

    live_points = Lives(screen)

    random.seed()

    itens_lista = []

    all_sprites = pg.sprite.Group()
    all_items = pg.sprite.Group()

    itens_coletados = {'coffee': 0,
                       'energy_drink': 0,
                       'inseticide': 0,
                       'bit_0': 0,
                       'bit_1': 0,
                       'bugs': 0}
    player = Player(screen, 320, 320, pg.K_d, pg.K_a, pg.K_w, pg.K_s)

    all_sprites = pg.sprite.Group()
    all_items = pg.sprite.Group()

    #
    all_bullets = []
    #

    # Lista com todos os bugs
    all_bugs = []

    all_sprites.add(player)

    # variaveis para controlar o spaw dos bugs
    contador = 0
    gradacao = 0
    # variavel para nao permitir atirar varias vezes ao mesmo tempo
    cooldown = 0
    # Variavel para controlar se o energético está ativado
    energy = False
    # Variavel para controlar o tempo de uso do energético
    timer = 100

    # coordenada x das nuvens
    clouds_x = 0

    while True:
        cooldown -= 1  # esfriar o inseticida
        timer += 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            #
            if event.type == pg.MOUSEBUTTONDOWN and cooldown <= 0:

                bala = Projectile(player)
                all_bullets.append(bala)
                cooldown = bala.cooldown(cooldown, energy)
                if energy == True and timer >= 150:
                    energy = False

                spray_sound.play()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and itens_coletados['energy_drink'] >= 3:
                    energy = True
                    timer = 0
                    itens_coletados['energy_drink'] = 0

        for balas in all_bullets:  # movimento do gas na tela
            balas.projectile_move()

        # Faz o background aparecer
        screen.blit(pg.image.load(Path('assets', 'background.png')), (0, 0))

        # Faz a animação das nuvens
        screen.blit(pg.image.load(Path('assets', 'clouds.png')), (clouds_x, 0))
        if (clouds_x >= width):
            clouds_x = -width
        clouds_x += 3

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
        # desenha e impede a sobreposição dos bugs
        for um_bug in all_bugs:
            um_bug.trace(screen)
            um_bug.update(player, identificar_posicao_bug)
            lista_aux = all_bugs[:]
            lista_aux.remove(um_bug)
            for i in lista_aux:
                if um_bug.rect.colliderect(i.rect) is True:
                    if um_bug.x < i.x:
                        um_bug.x -= 10
                    elif um_bug.x > i.x:
                        um_bug.x += 10
                    if um_bug.y > i.y:
                        um_bug.y += 10
                    elif um_bug.y < i.y:
                        um_bug.y -= 10

            Bug.vel(um_bug, itens_coletados)
            live_points.update_vida(player, um_bug)

        # Destruindo os projéteis e os bugs quando entram em colisão

        for bala in all_bullets:
            bala.destroy = False
            # Condicional para o projétil ser A quando off-screen
            if (bala.rect.x < 0 or bala.rect.x > width) or (bala.rect.y < 0 or bala.rect.y > height):
                all_bullets.remove(bala)
            for um_bug in all_bugs:
                um_bug.destroy = False
                if bala.destroy == False and um_bug.destroy == False:
                    if bala.rect.colliderect(um_bug.rect):
                        bala.destroy = True
                        um_bug.destroy = True

                        if bala in all_bullets:

                            all_bullets.remove(bala)

                        if um_bug in all_bugs:

                            all_bugs.remove(um_bug)
                            itens_coletados['bugs'] += 1

                            morte_bug_sound.play()  # Efeito sonoro da coleta de item

                            # Tem uma chance de gerar um item no lugar onde o bug morre
                            if random.randint(0, 2) == 1:
                                gerar_itens(itens_lista, all_items,
                                            player, um_bug.x, um_bug.y)

        # Inserir os itens coletados,bugs mortos e a pontuação na tela
        text_bugs = font_game.render(
            f'X {itens_coletados["bugs"]}', 1, branco)
        # Pontuação:Um bug  vale 1 ponto e cada bit vale 5 pontos
        pontos = (
            itens_coletados["bit_0"] + itens_coletados["bit_1"])*5 + itens_coletados["bugs"]*3
        text_pontuacao = font_game.render(
            f'Pontuação: {pontos}', 1, branco)

        screen.blit(text_pontuacao, (270, 10))
        screen.blit(pg.transform.scale(pg.image.load(
            Path('assets', 'bug_simples.png')), (40, 35)), (20, 65))
        screen.blit(text_bugs, (70, 75))
        if itens_coletados['energy_drink'] == 0:
            screen.blit(pg.transform.scale(pg.image.load(
                Path('assets', 'battery-0.png')), (90, 90)), (5, 85))
        elif itens_coletados['energy_drink'] == 1:
            screen.blit(pg.transform.scale(pg.image.load(
                Path('assets', 'battery-1.png')), (90, 90)), (5, 85))
        elif itens_coletados['energy_drink'] == 2:
            screen.blit(pg.transform.scale(pg.image.load(
                Path('assets', 'battery-2.png')), (90, 90)), (5, 85))
        elif itens_coletados['energy_drink'] >= 3:
            screen.blit(pg.transform.scale(pg.image.load(
                Path('assets', 'battery-3.png')), (90, 90)), (5, 85))

        for balas in all_bullets:  # desenha o projetil gas na tela
            balas.trace(screen)

        # Atualiza o dicionário de itens coletados
        for i in itens_lista:
            coletado = i.update()
            if coletado != None:
                itens_coletados[coletado] += 1
                item_sound.play()  # Efeito sonoro da coleta de item
                if coletado == "coffee":
                    live_points.vida_adicionar(player, i)

        if Lives.parar_jogo(live_points):
            menu.error(pontos)

        # Desenha a vida na tela
        live_points.draw()
        pg.display.flip()
        clock.tick(30)
        contador += 1


if __name__ == '__main__':
    menu.menu_screen()
