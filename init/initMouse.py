import pygame


def init_mouse():
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
                return 'start_game'
