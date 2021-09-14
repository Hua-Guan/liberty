import pygame


class LevelOne:
    def __init__(self, screen):
        self.bg_1 = pygame.image.load('resource/background/bg_1.png')
        self.bg_1_sc = pygame.transform.scale(self.bg_1, (800, 600))
        self.v = 0
        self.screen = screen

    def move(self):
        self.v -= 2
        self.screen.blit(self.bg_1_sc, (0, 0))
