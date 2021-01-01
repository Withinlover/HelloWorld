import pygame, random

from ..components import info
from ..components import snack
from ..components import food
from .. import tools, sound
from .. import constants as C

class AI:
    def __init__(self):
        self.finished = False
        self.next = None
        self.player = snack.Snack([(300, 0), (280, 0), (260, 0)], 'right', 0)
        # self.basePath = os.getcwd() + '/source/images'
        self.basePath = C.bathPath

        C.addScore(-C.score)
        self.info = info.Info('Single')
        self.food = food.Food()
        self.setbackground()
        self.new = True
        self.timer = pygame.time.get_ticks()
        self.Unkeys = [0 for i in range(323)]

        self.sound = sound.Sound()


    def init(self):
        self.player = snack.Snack([(300, 0), (280, 0), (260, 0)], 'right', 0)
        C.addScore(-C.score)
        self.timer = pygame.time.get_ticks()


    def setbackground(self):
        self.Background = pygame.image.load(self.basePath + 'source/images/background.png')

    def gameover(self):
        pygame.time.delay(750)
        self.new = True

    def update(self, surface, keys):
        # 判断是否需要重置
        if self.new:
            self.new = False
            self.init()

        # 玩家移动
        if self.player.canMove:
            tools.getPreButton(self.player, self.food)
            # print(self.player.preButton)
        self.player.move(self.Unkeys)
        self.player.update()

        # 吃东西 / 判断死亡
        if self.player.canCheck:
            if tools.foodCheck(self.player, self.food.position):
                if (len(self.player.segment) < 900):
                    self.food.new(self.player.segment)
                C.addScore(self.player.coin)
                self.sound.eat()
            else:
                self.player.delBack()
            if self.food.existGift and tools.foodCheck(self.player, self.food.gift):
                self.food.existGift = False
                self.player.gift()
                self.sound.gift()
            self.player.canCheck = False
        # AI 模式下没有道具
        if C.mode[1] == 3:
            self.food.existGift = False
        self.food.update()

        if tools.SingleCheck(self.player) or keys[pygame.K_SPACE]:
            self.player.died = True
            self.finished = True
            self.next = 'GameOver'
            self.gameover()

        # 更新分数信息
        C.updateP1(len(self.player.segment))
        C.updateTimer((pygame.time.get_ticks() - self.timer) / 1000)
        self.info.update()

        self.draw(surface)

    def draw(self, surface):
        # 背景图片
        surface.blit(self.Background, (0, 0))
        # snack
        self.player.draw(surface)

        # food
        self.food.draw(surface)

        # info
        surface.blit(pygame.image.load(self.basePath + 'source/images/gameInfo.png'), (0, 0))
        self.info.draw(surface)
