import pygame


def init_bg_music():
    pygame.mixer.music.load('resource/music/start_background.mp3')
    # 让音乐无限循环
    pygame.mixer.music.play(-1)
    # 设置音量
    pygame.mixer.music.set_volume(0.2)
