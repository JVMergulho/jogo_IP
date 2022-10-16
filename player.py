import pygame as pg
import sys

class Player(pg.sprite.Sprite):
    def __init__(self, win, x, y, right, left, up, down):


class Player(pg.sprite.Sprite):
    def __init__(self, win, x, y, right, left, up, down):
        pg.sprite.Sprite.__init__(self)

        # lista de sprites usadas para a animação
        self.sprites = []

        self.sprites.append(pg.image.load(
            'assets\personagem_com_inseticida-1.png'))
        self.sprites.append(pg.image.load(
            'assets\personagem_com_inseticida-2.png'))
        self.sprites.append(pg.image.load(
            'assets\personagem_com_inseticida-3.png'))
        self.sprites.append(pg.image.load(
            'assets\personagem_com_inseticida-2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pg.transform.scale(self.image, (70, 70))

        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

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


        self.rect.topleft = self.x, self.y


def main():
    screen = pg.display.set_mode((672, 672))
    clock = pg.time.Clock()
    pg.display.set_caption('Bug Bounty')

    player = Player(screen, 350, 320, pg.K_d, pg.K_a, pg.K_w, pg.K_s)

    # Outra possibilidade de teclas de controle: pg.K_RIGHT,pg.K_LEFT,pg.K_UP,pg.K_DOWN

    all_sprites = pg.sprite.Group()

    all_sprites.add(player)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        screen.fill((60, 100, 130))

        all_sprites.draw(screen)
        all_sprites.update()

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
