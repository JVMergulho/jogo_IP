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
        screen.blit(pg.image.load(Path('assets', 'background_menu.jpeg')), (0, 0))
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
                            main()


        pg.display.flip()