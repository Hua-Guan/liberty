# coding=utf-8
import pygame

import sprite.kirisame.kirisame
import sprite.background.background
import level.level_1

# 定义状态量
start_bg_state = None
level_state = None
# 定义主角
main_player = None


def main():
    # 定义状态量
    global state
    state = None
    # 初始化游戏
    pygame.init()
    screen = pygame.display.set_mode([800, 600])

    init_bg_music()

    background = sprite.background.background.Background()
    background_group = pygame.sprite.Group()
    background_group.add(background)

    global main_player
    main_player = sprite.kirisame.kirisame.Kirisame()
    group = pygame.sprite.Group()
    group.add(main_player)

    level_one = level.level_1.LevelOne(screen)

    clock = pygame.time.Clock()
    while True:
        # 设置帧率
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        if state == None:
            init_mouse()
            # 绘制
            background_group.update()
            background_group.draw(screen)
        if start_bg_state == 'start_game':
            init_player()
            level_one.move()
            group.update()
            group.draw(screen)

        pygame.display.update()


def init_player():
    my_key = pygame.key.get_pressed()
    if my_key[pygame.K_d]:
        main_player.state = 'walk_forward'
        main_player.face_state = 'forward'
    elif my_key[pygame.K_a]:
        main_player.state = 'walk_back'
        main_player.face_state = 'back'
    elif my_key[pygame.K_w]:
        if main_player.state != 'jump_above':
            main_player.state = 'jump_above'
    else:
        if main_player.face_state == 'forward' and main_player.state != 'jump_above':
            main_player.state = 'idle_forward'
        elif main_player.face_state == 'back' and main_player.state != 'jump_above':
            main_player.state = 'idle_back'


def init_mouse():
    global start_bg_state
    # 获取鼠标坐标
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    # 获取鼠标点击事件
    pressed_array = pygame.mouse.get_pressed(3)
    for index in range(len(pressed_array)):
        if pressed_array[index]:
            if index == 0 and 320 < mouse_x < 420 and 420 < mouse_y < 470:
                # 按下停止音乐
                pygame.mixer.music.stop()
                start_bg_state = 'start_game'


def init_bg_music():
    pygame.mixer.music.load('resource/music/start_background.mp3')
    # 让音乐无限循环
    pygame.mixer.music.play(-1)
    # 设置音量
    pygame.mixer.music.set_volume(0.2)


if __name__ == '__main__':
    main()
