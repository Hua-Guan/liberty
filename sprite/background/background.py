import pygame.sprite


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.image = pygame.Surface((800, 600))
        self.background = pygame.image.load('resource/background/start_background.jpg').convert()
        self.rect = pygame.Rect(0, 0, 800, 640)
        ###############
        self.font = pygame.font.Font('resource/font/经典平黑简.ttf', 40)
        self.text_surface = self.font.render("开始游戏", False, (255, 255, 255)) # 设置抗锯齿将没有透明度
        ###############
        self.state = True
        self.frame_font = 0
        self.timer_font = 0

    def update(self):
        # 清除上一帧
        self.image.fill((255, 255, 255))
        # 更新字体透明度
        self.text_surface.set_alpha(self.frame_font)
        # 更新背景
        self.image.blit(self.background, (0, 0, 800, 600), (0, 0, 800, 600))
        self.image.blit(self.text_surface, (320, 420))
        # 更新字体帧数
        if pygame.time.get_ticks() > self.timer_font + 60:
            if self.state:
                self.frame_font += 5
            else:
                self.frame_font -= 5
            if self.frame_font == 225:
                self.state = False
            elif self.frame_font == 0:
                self.state = True
            self.timer_font = pygame.time.get_ticks()

