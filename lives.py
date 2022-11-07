import pygame as pg
from pathlib import Path

#Classe que controla a vida do player
class Lives(pg.sprite.Sprite):

    def __init__(self, win):

        self.qtd = 4
        self.image = pg.image.load(Path('assets', 'cafe.gif'))
        self.image = pg.transform.scale(self.image, (40, 35))
        self.screen = win
        self.time = 0

    # Mostra a vida    
    def draw(self):
         for i in range(self.qtd):
            self.screen.blit(self.image, (20 + i*30, 20))

    # Procura por uma colisão entre o player com o bug e retira vida      
    def update_vida(self,player,Bug):
        colisao_vida=False
        self.time-=1
        if player.rect.colliderect(Bug.rect) is True and self.time<=0: 
            self.qtd-=1
            self.time=60
            colisao_vida=True
            return colisao_vida

    # Procura por uma colisão entre o player com o café e adiciona vida
    def vida_adicionar(self,player,item):
         if player.rect.colliderect(item.rect) is True and self.qtd<=3:
             self.qtd+=1

    # O que ocorre quando se perde todas as vidas         
    def parar_jogo(self):
        if self.qtd == 0:
            return True