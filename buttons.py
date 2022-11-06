import pygame as pg
import sys
from pathlib import Path

pg.font.init()
button_font = pg.font.Font(Path('assets', 'OXSTARS.ttf'), 25)
class Button():
    def __init__(self, imagem, centrox, centroy, texto):
        self.imagem = imagem
        self.centrox = centrox
        self.centroy = centroy
        self.texto = texto
        
        self.rect = self.imagem.get_rect(center=(self.centrox, self.centroy))
        self.text = button_font.render(self.texto, True, (145, 61, 136))
        self.text_rect = self.text.get_rect(center=(self.centrox, self.centroy))

    def draw(self, screen):
        screen.blit(self.imagem, self.rect)
        screen.blit(self.text, self.text_rect)

    def verifica_clique(self, mouseX, mouseY):
        if mouseX in range(self.rect.left, self.rect.right) and mouseY in range(self.rect.top, self.rect.bottom):
            return True
    
    def hoover(self, mouseX, mouseY):
        if mouseX in range(self.rect.left, self.rect.right) and mouseY in range(self.rect.top, self.rect.bottom):
            self.text = button_font.render(self.texto, True, (89, 5, 110))
        else:
            self.text = button_font.render(self.texto, True, (145, 61, 136))
