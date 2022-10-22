import pygame as pg
from pathlib import Path
import sys

class Player(pg.sprite.Sprite):
    def __init__(self, win, x, y, right, left, up, down):
        pg.sprite.Sprite.__init__(self)

        # lista de sprites usadas para a animação
        self.sprites = []

        self.sprites.append(pg.image.load(Path('assets','personagem_com_inseticida-1.png')))
        self.sprites.append(pg.image.load(Path('assets','personagem_com_inseticida-2.png')))
        self.sprites.append(pg.image.load(Path('assets','personagem_com_inseticida-3.png')))
        self.sprites.append(pg.image.load(Path('assets','personagem_com_inseticida-2.png')))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pg.transform.scale(self.image, (70, 70))

        self.rect= self.image.get_rect()
        self.rect.center= x,y

        self.win = win
        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        
        self.right = right
        self.left = left
        self.up = up
        self.down = down

        self.vel = 5

    # modifica a sprite atual
    def muda_sprite(self):
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        print(int(self.atual))
        self.image = pg.transform.scale(self.image, (70, 70))

    def update(self):
        self.move()

    def move(self):
        walk = False

        # Identifica as teclas que estão sendo pressionadas pelo usuário
        # e checa as teclas de movimentação
        keys = pg.key.get_pressed()
        if keys[self.right]:
            walk = True
            self.x += self.vel
        if keys[self.left]:
            self.x -= self.vel
            walk = True
        if keys[self.up]:
            self.y -= self.vel
            walk = True
        if keys[self.down]:
            self.y += self.vel
            walk = True

        if walk:
            self.muda_sprite()
        else:
            self.image = self.sprites[1]
            self.image = pg.transform.scale(self.image, (70, 70))
        #Cria uma borda,a qual transporta o player de um lado pro outro,no eixo x
        if self.x <= -10:
            self.x=678
        elif self.x>=678:
            self.x=-10
        self.rect.center = self.x, self.y 
        #Cria uma borda no eixo y
        if self.y <= 215:
            self.y=215
        if self.y >= 645:
            self.y = 645