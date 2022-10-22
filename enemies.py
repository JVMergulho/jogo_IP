from asyncio import FastChildWatcher
import pygame as pg
from pathlib import Path
from player import Player

# Essa é classe dos inimigos

class Bug():
    # Inicializa o inimigo
    def __init__(self, x, y):
        
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(Path('assets','bug_simples.png'))
        
        self.image = pg.transform.scale(self.image, (45,45))

        self.x = x
        self.y = y

        self.rect = pg.Rect(self.x, self.y, 35, 38)

        self.vel = 3

        self.destroy = False

    # Faz o inimigo se mover em direção ao player e, se o inimigo atacá-lo, faz o player se mover para a direção contrária da direção que o inimigo atacou
    # a condição do abs previne que o bug tente sincronizar infinitamente com o player
    def update(self, player, identificar_posicao_bug):

        # Checa se o inimigo está colidindo com o player ou não
        if self.rect.colliderect(player.rect) is False:    
            if player.x < self.x and abs(player.x - self.x) > 5:
                self.x -= self.vel
                identificar_posicao_bug['esquerda'] = True
                identificar_posicao_bug['direita'] = False
            elif player.x > self.x and abs(player.x - self.x) > 5:
                self.x += self.vel
                identificar_posicao_bug['esquerda'] = False
                identificar_posicao_bug['direita'] = True
            else:
                self.x -= 0
                identificar_posicao_bug['esquerda'] = False
                identificar_posicao_bug['direita'] = False
            if player.y > self.y and abs(player.y - self.y) > 5:
                self.y += self.vel
                identificar_posicao_bug['em cima'] = True
                identificar_posicao_bug['embaixo'] = False
            elif player.y < self.y and abs(player.y - self.y) > 5:
                self.y -= self.vel
                identificar_posicao_bug['em cima'] = False
                identificar_posicao_bug['embaixo'] = True
            else:
                self.y -= 0
                identificar_posicao_bug['em cima'] = False
                identificar_posicao_bug['embaixo'] = False
        
        else: 
            if identificar_posicao_bug['esquerda']:
                player.x -= 40
            elif identificar_posicao_bug['direita']:
                player.x += 40
            if identificar_posicao_bug['embaixo']:
                player.y -= 40
            elif identificar_posicao_bug['em cima']:
                player.y += 40

        self.rect.center = self.x, self.y

        return identificar_posicao_bug


    def trace(self, screen): #desenho do bug
        screen.blit(self.image, self.rect)