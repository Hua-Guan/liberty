# coding=utf-8
import pygame

import sprite.kirisame.kirisame
import sprite.background.background
from init import initMainPlayer


def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 600])

    background = sprite.background.background.Background()
    backgroundGroup = pygame.sprite.Group()
    backgroundGroup.add(background)

    main_player = sprite.kirisame.kirisame.Kirisame()
    group = pygame.sprite.Group()
    group.add(main_player)

    clock = pygame.time.Clock()
    while True:
        # 设置帧率
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        # initMainPlayer.init(main_player)


        # group.update()
        # group.draw(screen)

        backgroundGroup.update()
        backgroundGroup.draw(screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
