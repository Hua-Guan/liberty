# coding=utf-8
import pygame

import sprite.kirisame.kirisame
import sprite.background.background
from init import initMainPlayer
from init import initMusic
from init import initMouse
# 定义状态量
state = None

def main():
    # 定义状态量
    global state
    state = None
    ##############
    pygame.init()
    screen = pygame.display.set_mode([800, 600])

    initMusic.init_bg_music()

    background = sprite.background.background.Background()
    background_group = pygame.sprite.Group()
    background_group.add(background)

    main_player = sprite.kirisame.kirisame.Kirisame()
    group = pygame.sprite.Group()
    group.add(main_player)

    bg_1 = pygame.image.load('resource/background/bg_1.png')
    bg_1_sc = pygame.transform.scale(bg_1, (800, 600))

    clock = pygame.time.Clock()
    while True:
        # 设置帧率
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        if state == None:
            state = initMouse.init_mouse()
            # 绘制
            background_group.update()
            background_group.draw(screen)
        if state == 'start_game':
            initMainPlayer.init(main_player)
            screen.blit(bg_1_sc, (0, 0))
            group.update()
            group.draw(screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
