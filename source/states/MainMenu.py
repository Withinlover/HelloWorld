import pygame
from .. import constants as C
from .. import setup
from ..components import info

class MainMenu:
    def __init__(self):
        self.SetBackground()
        self.SetCursor()
        self.Info = info.Info('MainMenu')
        self.finished = False
        self.next = 'LoadScreen'
        self.state = [0, 1, 0, 0]
        C.updateMode(self.state)

    # 初始化背景图案
    def SetBackground(self):
        path = C.bathPath + 'source/images/background.png'
        self.Background = pygame.image.load(path)

    # 初始化光标
    def SetCursor(self):
        # 初始化， 继承精灵
        path = C.bathPath + 'source/images/cursor.png'
        self.Cursor = pygame.sprite.Sprite()
        self.Cursor.image = pygame.image.load(path)
        self.Cursor.image = pygame.transform.scale(self.Cursor.image, C.CursorSize)
        # 共有四行， 所以 0 <= Index <= 3
        self.CursorIndex = 0

        # 获取位置
        rect = self.Cursor.image.get_rect()
        rect.x, rect.y = C.CursorPosition[self.CursorIndex][0], C.CursorPosition[self.CursorIndex][1]
        self.Cursor.rect = rect

        # 用于存储选择信息的变量
        self.CursorCanMove = True
        self.SpaceCanPress = False
        self.ModeCanChange = True
        self.Difficulty = 1
        self.Bround = 0
        self.GameMode = 0

    # 根据按键更新光标位置
    def updateCursor(self, keys):
        # 4个位置, CursorIndex 分别对应 0-3
        # 处理光标的移动
        if(self.CursorCanMove and self.CursorIndex > 0 and keys[pygame.K_UP]):
            self.CursorIndex -= 1
            self.CursorCanMove = False
        if(self.CursorCanMove and self.CursorIndex < 3 and keys[pygame.K_DOWN]):
            self.CursorIndex += 1
            self.CursorCanMove = False
        if((not keys[pygame.K_UP]) and (not keys[pygame.K_DOWN])):
            self.CursorCanMove = True

        # 按下空格，修改对应的模式
        if(self.SpaceCanPress and keys[pygame.K_SPACE]):
            # 开始游戏
            if self.ModeCanChange and self.CursorIndex == 0:
                self.ModeCanChange = False
                self.finished = True

            # 切换难度
            if self.ModeCanChange and self.CursorIndex == 1:
                self.Difficulty = self.Difficulty + 1
                self.ModeCanChange = False
                if self.Difficulty > 3:
                    self.Difficulty = 0

            # 切换边界判定
            if self.ModeCanChange and self.CursorIndex == 2:
                self.Bround = self.Bround + 1
                self.ModeCanChange = False
                if self.Bround > 1:
                    self.Bround = 0

            # 切换游戏模式
            if self.ModeCanChange and self.CursorIndex == 3:
                self.GameMode = self.GameMode + 1
                self.ModeCanChange = False
                if self.GameMode > 3:
                    self.GameMode = 0

        self.state = [self.CursorIndex, self.Difficulty, self.Bround, self.GameMode]
        C.updateMode(self.state)

        if(not keys[pygame.K_SPACE]):
            self.ModeCanChange = True
            self.SpaceCanPress = True

        rect = self.Cursor.image.get_rect()
        rect.x, rect.y = C.CursorPosition[self.CursorIndex][0], C.CursorPosition[self.CursorIndex][1]
        self.Cursor.rect = rect

    # 更新
    def update(self, surface, keys):

        self.updateCursor(keys)

        surface.blit(self.Background, (0, 0))
        surface.blit(self.Cursor.image, self.Cursor.rect)
        # for i in range (len(C.CursorPosition)):
        #     surface.blit(self.Cursor, (C.CursorPosition[i][0], C.CursorPosition[i][1]))

        self.Info.update()
        self.Info.draw(surface)