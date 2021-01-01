import pygame, random

from ..components import info
from ..components import snack
from ..components import food, wall
from .. import tools, sound
from .. import constants as C


class SinglePlayer:
    def __init__(self):
        self.finished = False
        self.next = None
        self.player = snack.Snack([(300, 100), (280, 100), (260, 100)], 'right', 0)
        # self.basePath = os.getcwd() + '/source/images'
        self.basePath = C.bathPath

        C.addScore(-C.score)
        self.info = info.Info('Single')
        self.food = food.Food()
        self.setbackground()
        self.new = True
        self.timer = pygame.time.get_ticks()

        self.sound = sound.Sound()

        self.wall = wall.Wall()
        self.wallStatus = self.wall.getStatus(C.level)


    def init(self):
        self.player = snack.Snack([(300, 100), (280, 100), (260, 100)], 'right', 0)
        self.timer = pygame.time.get_ticks()
        self.wallStatus = self.wall.getStatus(C.level)
        self.food.new(self.player.segment, self.wallStatus)


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
        self.player.move(keys)
        self.player.update()

        # 吃东西 / 判断死亡
        if self.player.canCheck:
            if tools.foodCheck(self.player, self.food.position):
                if (len(self.player.segment) < 900):
                    self.food.new(self.player.segment, self.wallStatus)
                C.addScore(self.player.coin)
                self.sound.eat()
            else:
                self.player.delBack()
            if self.food.existGift and tools.foodCheck(self.player, self.food.gift):
                self.food.existGift = False
                self.player.gift()
                self.sound.gift()
            self.player.canCheck = False
        self.food.update()

        if tools.SingleCheck(self.player) or tools.checkSnack(self.player.position, self.wallStatus):
            self.player.died = True
            self.finished = True
            self.next = 'GameOver'
            self.gameover()

        if C.score > C.level * 200 and C.level < 5:
            self.player.died = True
            self.finished = True
            self.next = 'LoadScreen'
            C.level += 1
            self.gameover()


        # 更新分数信息
        C.updateP1(len(self.player.segment))
        C.updateTimer((pygame.time.get_ticks() - self.timer) / 1000)
        self.info.update()

        # 结束的时候直接调用
        # TODO 这个是之前写MainMenu 遗留下来的问题，写完本项目如果还有时间的话可以试着修改/重构一下（
        self.draw(surface)

    def draw(self, surface):
        # 背景图片
        surface.blit(self.Background, (0, 0))
        # snack
        self.player.draw(surface)

        # food
        self.food.draw(surface)

        # wall
        self.wall.update(self.wallStatus)
        self.wall.draw(surface)

        # info
        surface.blit(pygame.image.load(self.basePath + 'source/images/gameInfo.png'), (0, 0))
        self.info.draw(surface)
