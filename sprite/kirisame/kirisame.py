import pygame

import constant.player


class Kirisame(pygame.sprite.Sprite):
    def __init__(self):
        super(Kirisame, self).__init__()
        # 定义初始数据
        self.image = pygame.Surface((70, 120))
        self.rect = None
        # 加载主角的图片
        self.image_kirisame = pygame.image.load('resource/player/kirisame.png')
        # 使背景透明
        self.image.set_colorkey((47, 95, 115))
        # 定义状态
        self.face_state = 'forward'
        self.state = None
        #################
        self.vx = 100
        self.vy = 375
        self.v = 10
        self.g = 100
        #################
        self.frame_idle = 0
        self.timer_idle = 0
        #################
        self.frame_walk = 0
        self.timer_walk = 0
        ################
        self.frame_jump = -1
        self.timer_jump = 0
        self.t = 0

    def update(self, *args):
        super().update(*args)
        # 清除上一帧
        self.image.fill((47, 95, 115))
        self.idle()
        self.walk()
        self.jump()

    def idle(self):
        if self.state == 'idle_forward':
            # 加载下一帧
            x, y, w, h = constant.player.kirisame['kirisame_idle_position'][self.frame_idle]
            self.rect = (self.vx, self.vy - h, w, h)
            self.image.blit(self.image_kirisame, (0, 0, w, h), (x, y, w, h))
            # 更新帧数
            if pygame.time.get_ticks() > self.timer_idle + 100:
                self.frame_idle += 1
                self.frame_idle %= 7
                self.timer_idle = pygame.time.get_ticks()
        elif self.state == 'idle_back':
            # 加载下一帧
            x, y, w, h = constant.player.kirisame['kirisame_idle_position'][self.frame_idle]
            self.rect = (self.vx, self.vy - h, w, h)
            idle_flip = pygame.Surface((w, h))
            idle_flip.blit(self.image_kirisame, (0, 0, w, h), (x, y, w, h))
            self.image.blit(pygame.transform.flip(idle_flip, True, False), (0, 0, w, h))
            # 更新帧数
            if pygame.time.get_ticks() > self.timer_idle + 100:
                self.frame_idle += 1
                self.frame_idle %= 7
                self.timer_idle = pygame.time.get_ticks()

    def walk(self):
        if self.state == 'walk_forward':
            # 加载下一帧
            x, y, w, h = constant.player.kirisame['kirisame_walk_forwalk'][self.frame_walk]
            self.image.blit(self.image_kirisame, (0, 0, w, h), (x, y, w, h))
            self.rect = (self.vx, self.vy - h, w, h)
            # 更新帧数和坐标
            if pygame.time.get_ticks() > self.timer_walk + 60:
                self.frame_walk += 1
                self.frame_walk %= 7
                self.timer_walk = pygame.time.get_ticks()
                self.vx += self.v

        elif self.state == 'walk_back':
            # 加载下一帧
            x, y, w, h = constant.player.kirisame['kirisame_walk_forwalk'][self.frame_walk]
            walk_flip = pygame.Surface((w, h))
            walk_flip.blit(self.image_kirisame, (0, 0, w, h), (x, y, w, h))
            self.image.blit(pygame.transform.flip(walk_flip, True, False), (0, 0, w, h))
            self.rect = (self.vx, self.vy - h, w, h)
            # 更新帧数和坐标
            if pygame.time.get_ticks() > self.timer_walk + 60:
                self.frame_walk += 1
                self.frame_walk %= 7
                self.timer_walk = pygame.time.get_ticks()
                self.vx -= self.v

    def jump(self):
        if self.state == 'jump_above':
            # 加载下一帧
            x, y, w, h = constant.player.kirisame['kirisame_jump_above'][self.frame_jump]
            self.rect = (self.vx, self.vy - h, w, h)
            self.image.blit(self.image_kirisame, (0, 0, w, h), (x, y, w, h))
            # 更新帧数和坐标
            if pygame.time.get_ticks() > self.timer_jump + 50:
                self.frame_jump += 1
                if self.frame_jump > 22:
                    self.frame_jump = 0
                    self.t = 0
                    self.state = 'idle_forward'
                self.timer_jump = pygame.time.get_ticks()
                del_y = 110 * self.t - self.g * self.t * self.t
                if 8 < self.frame_jump < 15:
                    self.vy -= del_y
                    self.t += 0.1
                elif 14 < self.frame_jump < 21:
                    self.vy += del_y
                    self.t += 0.1
