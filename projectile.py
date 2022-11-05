import pygame as pg
from pathlib import Path
import math
from player import Player

#Essa é a classe responsavel pelos projéteis

class Projectile():
    def __init__(self, player):
        xcursor, ycursor = pg.mouse.get_pos() #pega as coordenadas do cursor

        angulo = math.atan2(ycursor - player.y, xcursor - player.x) #pega o angulo para o cursor

        self.dx = math.cos(angulo) * 8 #relaciona o cosseno do angulo adquirido a direção do eixo x
        self.dy = math.sin(angulo) * 8 #relaciona o seno do angulo adquirido a direção do eixo y

        self.x = player.x + 10 #adequa a saida do gas ao inseticida
        self.y = player.y - 7

        
        self.image = pg.image.load(Path('assets','gas0.png'))
        self.image = pg.transform.scale(self.image, (20,20))
        

        #self.rect = self.image.get_rect()
        self.rect = pg.Rect(player.x, player.y, 15, 15)

        # Quando a bala sumir do mapa
        self.destroy = False



    def projectile_move(self): #movimento do gas em direção ao clique

        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


    def trace(self, screen): #desenho do gas
        screen.blit(self.image, self.rect)
    def cooldown(player,cooldown,energy):
        
        if energy == False:
            cooldown=12
        elif energy == True:
            cooldown = -1 
        return cooldown