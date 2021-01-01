import pygame, random

from ..components import info
from ..components import snack
from ..components import food
from .. import tools, sound
from .. import constants as C

class ManAI:
    def __init__(self):
        self.finished = False
        self.next = 'GameOver'
        self.timer = 0  # self.timer = 0 同时表示新游戏
        self.background = pygame.image.load(C.bathPath + 'source/images/background.png')

        self.Unkeys = [0 for i in range(323)]
        self.init()
        self.info = info.Info('MultiPlayer')
        self.sound = sound.Sound()

    # 初始化 蛇 和 食物
    def init(self):
        self.P1 = snack.Snack([(300, 100), (280, 100), (260, 100)], 'right', 0)
        self.P2 = snack.Snack([(300, 0), (280, 0), (260, 0)], 'right', 2)
        self.food = food.Food()

        C.addScore(-C.score)
        C.addScoreP1(-C.scoreP1)
        C.addScoreP2(-C.scoreP2)

    def gameover(self):
        pygame.time.delay(750)
        self.timer = 0

    def addScore(self, snack):
        if snack.mode == 0:
            C.addScoreP1(snack.coin)
        elif snack.mode == 2:
            C.addScoreP2(snack.coin)

    # 单独更新一条蛇的状态
    def updateSnack(self, snack):
        if snack.canCheck and not snack.died:
            if tools.foodCheck(snack, self.food.position):
                if len(self.P1.segment) + len(self.P2.segment) < 900:
                    self.food.new(self.P1.segment, self.P2.segment)
                self.addScore(snack)
                self.sound.eat()
            else:
                snack.delBack()
            if self.food.existGift and tools.foodCheck(snack, self.food.gift):
                self.food.existGift = False
                snack.gift()
                self.sound.gift()
            snack.canCheck = False

        if tools.SingleCheck(snack):
            snack.died = True

    def update(self, surface, keys):
        # 判断是否需要重置
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
            self.init()

        # 玩家移动
        if self.P2.canMove and not self.P2.died:
            if self.P1.died:
                tools.getPreButton(self.P2, self.food)
            else:
                tools.getPreButton(self.P2, self.food, self.P1.segment)
            print(self.P2.preButton, '-')

        self.P1.move(keys)
        self.P2.move(self.Unkeys)
        self.P1.update()
        self.P2.update()

        # 吃东西 / 判断死亡
        # 玩家1 和 墙体，食物
        self.updateSnack(self.P1)
        self.updateSnack(self.P2)
        # P1 Vs P2
        if not self.P1.died and not self.P2.died:
            if tools.checkSnack(self.P1.position, self.P2.segment):
                self.P1.died = True
            if tools.checkSnack(self.P2.position, self.P1.segment):
                self.P2.died = True

        self.food.update()

        # 更新分数信息
        C.updateP1(len(self.P1.segment))
        C.updateP2(len(self.P2.segment))
        C.updateTimer((pygame.time.get_ticks() - self.timer) / 1000)
        self.info.update()

        # 结束的时候直接调用
        # TODO 这个是之前写MainMenu 遗留下来的问题，写完本项目如果还有时间的话可以试着修改/重构一下（
        self.draw(surface)

        # 判断游戏是否结束
        if self.P1.died:
            if self.P2.died or C.scoreP2 > C.scoreP1:
                self.finished = True
                self.timer = 0
                self.gameover()
            else:
                self.P2.speed = 2

    def draw(self, surface):
        # 背景图片
        surface.blit(self.background, (0, 0))
        # snack
        self.P1.draw(surface)
        self.P2.draw(surface)

        # food
        self.food.draw(surface)

        # info
        surface.blit(pygame.image.load(C.bathPath + 'source/images/gameInfo2.png'), (0, 0))
        self.info.draw(surface)