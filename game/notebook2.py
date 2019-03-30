import pygame
import sys
from pygame.locals import *


def main():
    (w, h) = (800, 800)
    (x, y) = (w/2, h/2)

    pygame.init()  # 初期化
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    im = pygame.image.load("character.png").convert_alpha()
    rect = im.get_rect()
    rect.center = (w/2, h/2)

    (xg, yg) = (3, 3)   # ランダム

    while True:
        pygame.display.update()     # 画面更新
        pygame.time.wait(0)
        screen.fill((0, 20, 0, 0))
        screen.blit(im, rect)

        for event in pygame.event.get():  # イベントの設定
            if event.type == QUIT:  # もし終了ボタンをおされたら
                pygame.quit()  # 終了する
                sys.exit()
            if event.type == KEYDOWN:   # キーを押したとき
                if (event.key == K_ESCAPE) or (x == xg and y == yg):  # ESCキー(仮想キーコード)が押されたら終了
                    pygame.quit()
                    sys.exit()

                if event.key == K_LEFT:
                    rect.move_ip(-1, 0)
                if event.key == K_RIGHT:
                    rect.move_ip(1, 0)
                if event.key == K_UP:
                    rect.move_ip(0, -1)
                if event.key == K_DOWN:
                    rect.move_ip(0, 1)


if __name__ == '__main__':
    main()
