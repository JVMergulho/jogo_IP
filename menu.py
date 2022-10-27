import pygame as pg
from buttons import Button
from pathlib import Path
import sys
from main import main



def menu_screen():

    pg.init()
    
    botoes = []

    foto_botao_play = pg.image.load(Path('assets','button4.png'))
    foto_botao_play = pg.transform.scale(foto_botao_play, (250, 100))

    botao_play = Button(foto_botao_play, 336, 316, 'PLAY')
    botao_story = Button(foto_botao_play, 336, 426, 'STORY')
    botao_quit = Button(foto_botao_play, 336, 536, 'QUIT')

    botoes.append(botao_play)
    botoes.append(botao_story)
    botoes.append(botao_quit)

    while True:
        mouseX, mouseY = pg.mouse.get_pos()
        screen = pg.display.set_mode((672, 672))
        screen.blit(pg.image.load(Path('assets', 'background_menu.png')), (0, 0))
        pg.display.set_caption('Menu')


        for botao in botoes:
            Button.draw(botao, screen)
        for botao in botoes:
            Button.hoover(botao, mouseX, mouseY)



        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for botao in botoes:
                    if Button.verifica_clique(botao, mouseX, mouseY) == True:
                        if botao == botao_quit:
                            pg.quit()
                            sys.exit()
                        elif botao == botao_play:
                            preview_jogo()
                        elif botao == botao_story:
                            story_screen()


        pg.display.flip()

#função destinada a escrever um texto grande para quebrar as linhas quando passar da tela
def texto_bloco(screen, texto, posicao, fonte, cor):
    espaco = fonte.size('')[0] #retorna a largura do espaço da fonte
    inicioX = posicao[0] #posição inicial do texto em bloco
    inicioY = posicao[1]

    for palavra in texto:
        palavra_texto = fonte.render(palavra, True, cor)
        largura_palavra, altura_palavra = palavra_texto.get_size() #retorna a largura e altura da palavra
        if inicioX + largura_palavra >= 657:
            inicioX = posicao[0]
            inicioY += altura_palavra
        screen.blit(palavra_texto, (inicioX, inicioY))
        inicioX += largura_palavra + espaco
    



pg.font.init()
title_font = pg.font.SysFont('rage', 55)
names_font = pg.font.SysFont('rage', 30)
text_font = pg.font.SysFont('Arial', 25)
def story_screen():

    pg.init()

    foto_botao = pg.image.load(Path('assets','button4.png'))
    foto_botao = pg.transform.scale(foto_botao, (250, 100))

    foto_silvio = pg.image.load(Path('assets','personagem_com_inseticida-2.png'))
    foto_silvio = pg.transform.scale(foto_silvio, (90, 90))

    foto_bug = pg.image.load(Path('assets','bug_simples.png'))
    foto_bug = pg.transform.scale(foto_bug, (65, 65))

    botao_menu = Button(foto_botao, 336, 586, 'MENU')

    texto = '   Uma bela noite, um programador do CIn estava em um grad desenvolvendo um sistema de software, quando seu código começou a apresentar um comportamento inesperado. Por mais que ele tentasse, não conseguiu se livrar dos malditos bugs. Quando estava próximo de desistir, uma figura misteriosa surgiu: Silvio-sensei, mestre das artes místicas da computação. Silvio sugeriu a seguinte estratégia: Alcançar o ciberespaço (viajando através do R5) e, assim, derrotar os bugs no mano a mano, usando, para isso, um inseticida computacional.'

    while True:
        mouseX, mouseY = pg.mouse.get_pos()
        screen = pg.display.set_mode((672, 672))
        screen.blit(pg.image.load(Path('assets', 'background_story.png')), (0, 0))
        pg.display.set_caption('Story')


        Button.draw(botao_menu, screen)
        Button.hoover(botao_menu, mouseX, mouseY)

        text_title = title_font.render('A história de Silvio-sensei', True, (89, 5, 110))
        texto_bloco(screen, texto, (20, 100), text_font, (255, 255, 255))
        screen.blit(text_title, (75, 20))
        
        nome_silvio = names_font.render('Silvio-sensei', True, (255, 255, 255))
        nome_bug = names_font.render('Bug', True, (255, 255, 255))
        screen.blit(foto_silvio, (175, 385))
        screen.blit(foto_bug, (430, 394))
        screen.blit(nome_silvio, (150, 461))
        screen.blit(nome_bug, (438, 461))



        for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if Button.verifica_clique(botao_menu, mouseX, mouseY) == True:
                        menu_screen()



        pg.display.flip()

def preview_jogo():

    pg.init()
    font = pg.font.get_default_font()
    font_game = pg.font.SysFont(font, 30)
    font_game_2 = pg.font.SysFont('Onyx', 38)

    itens_coletados = {'coffee': 0,
                       'energy_drink': 0,
                       'inseticide': 0,
                       'bit_0': 0,
                       'bit_1': 0,
                       'bugs': 0}

    while True:
        screen = pg.display.set_mode((672, 672))
        screen.fill((255, 255, 255))
        screen.blit(pg.image.load(Path('assets', 'background.png')), (0, 0))

        text_coffee = font_game.render(
            f'X {itens_coletados["coffee"]}', 1, (255, 255, 255))
        text_energy_drink = font_game.render(
            f'X {itens_coletados["energy_drink"]}', 1, (255, 255, 255))
        text_bugs = font_game.render(
            f'X {itens_coletados["bugs"]}', 1, (255, 255, 255))
        text_pontuacao = font_game.render(
            f'Pontuação: {(itens_coletados["bit_0"] + itens_coletados["bit_1"])*5 + itens_coletados["bugs"]}', 1, (255, 255, 255))

        screen.blit(text_pontuacao, (270, 10))
        screen.blit(pg.transform.scale(pg.image.load(Path('assets','bug_simples.png')), (40, 35)), (20, 105))
        screen.blit(text_bugs, (70, 115))

        screen.blit(pg.transform.scale(pg.image.load(Path('assets', 'cafe.gif')), (40, 35)), (20, 20))
        screen.blit(text_coffee, (70, 35))

        screen.blit(pg.transform.scale(pg.image.load(Path('assets', 'energy_drink.png')), (35, 35)), (25, 65))
        screen.blit(text_energy_drink, (70, 75))

        mensagem = font_game_2.render('APERTE EM QUALQUER LUGAR DA TELA PARA COMEÇAR', True, (0, 0, 0))
        screen.blit(mensagem, (80, 336))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                main()

    
        pg.display.flip()