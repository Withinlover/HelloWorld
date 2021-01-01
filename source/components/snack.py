import pygame
import random
from .. import constants as C

from . import food
from .. import tools

class Snack:
    def __init__(self, position, direction, mode):
        # 基本属性： 蛇的身体，蛇头的位置，朝向，是否死亡
        self.segment = position
        self.position = self.segment[0]
        self.direction = direction
        self.died = False
        self.state = []

        # 游戏属性： 游戏模式，是否可以移动，游戏速度
        self.mode = mode # mode = 0 -> 单人游玩, mode = 1 -> 1P游玩, mode = 2 -> 2P游玩
        self.canMove = True
        self.canCheck = False
        self.limit = C.Speed[C.mode[1]]
        self.speed = 300

        # 辅助属性：计时器，用于模拟帧速率，preButton记录玩家的按键
        self.timer = pygame.time.get_ticks()
        self.preButton = ''

        # 预加载
        self.loadImage()

    # 载入图片
    def loadImage(self):
        basePath = C.bathPath
        if(self.mode == 0 or self.mode == 1):
            self.image_head = pygame.image.load(basePath + 'source/images/headP1.png')
            self.image_body = pygame.image.load(basePath + 'source/images/bodyP1.png')
            self.image_bodyA = pygame.image.load(basePath + 'source/images/bodyP1A.png')
            self.image_bodyB = pygame.image.load(basePath + 'source/images/bodyP1B.png')
            self.image_tail = pygame.image.load(basePath + 'source/images/tailP1.png')
        elif(self.mode == 2):
            self.image_head = pygame.image.load(basePath + 'source/images/headP2.png')
            self.image_body = pygame.image.load(basePath + 'source/images/bodyP2.png')
            self.image_bodyA = pygame.image.load(basePath + 'source/images/bodyP2A.png')
            self.image_bodyB = pygame.image.load(basePath + 'source/images/bodyP2B.png')
            self.image_tail = pygame.image.load(basePath + 'source/images/tailP2.png')

    # 修改蛇的方向，两层判断的原因是防止180度转弯
    # example：当蛇头朝右时，不可以调整方向为向左
    def changeDirection(self, keys):
        # TODO 这里的逻辑略复杂， 可以优化
        # mode = 0，可以同时使用 WSAD 和 上下左右 控制
        # mode = 1，仅可以使用 上下左右
        # mode = 2，仅可以使用 WSAD
        # 最外层是区分游戏mode
        # 第二层是为了防止蛇的身体发生180度转弯
        # 第三层是判断玩家的按键
        if self.mode == 0:
            if self.direction == 'left' or self.direction == 'right':
                if keys[pygame.K_UP] or self.preButton == 'up' or keys[pygame.K_w]:
                    self.direction = 'up'
                elif keys[pygame.K_DOWN] or self.preButton == 'down' or keys[pygame.K_s]:
                    self.direction = 'down'
            elif self.direction == 'up' or self.direction == 'down':
                if keys[pygame.K_RIGHT] or self.preButton == 'right' or keys[pygame.K_d]:
                    self.direction = 'right'
                elif keys[pygame.K_LEFT] or self.preButton == 'left' or keys[pygame.K_a]:
                    self.direction = 'left'

        if self.mode == 1:
            if self.direction == 'left' or self.direction == 'right':
                if keys[pygame.K_UP] or self.preButton == 'up':
                    self.direction = 'up'
                elif keys[pygame.K_DOWN] or self.preButton == 'down':
                    self.direction = 'down'
            elif self.direction == 'up' or self.direction == 'down':
                if keys[pygame.K_RIGHT] or self.preButton == 'right':
                    self.direction = 'right'
                elif keys[pygame.K_LEFT] or self.preButton == 'left':
                    self.direction = 'left'
        # TODO 和上一条 TODO 指代相同，用于区分两块代码
        if self.mode == 2:
            if self.direction == 'left' or self.direction == 'right':
                if keys[pygame.K_w] or self.preButton == 'up':
                    self.direction = 'up'
                elif keys[pygame.K_s] or self.preButton == 'down':
                    self.direction = 'down'
            elif self.direction == 'up' or self.direction == 'down':
                if keys[pygame.K_d] or self.preButton == 'right':
                    self.direction = 'right'
                elif keys[pygame.K_a] or self.preButton == 'left':
                    self.direction = 'left'

    # 向前移动一格的距离
    def moveForward(self):
        # TODO 这里的tuple使用可能不太流畅，可以优化代码结构，对性能无影响，优先度较低
        positionX, positionY = self.position
        if self.direction == 'right':
            positionX += 20
        if self.direction == 'left':
            positionX -= 20
        if self.direction == 'up':
            positionY -= 20
        if self.direction == 'down':
            positionY += 20

        # Across
        if C.mode[2] == 1:
            positionX = (((positionX - 200) + 600) % 600) + 200
            positionY = (positionY + 600) % 600

        self.position = positionX, positionY
        self.segment.insert(0, (positionX, positionY))
        self.canCheck = True

    # 删除队尾
    def delBack(self):
        self.segment.pop()

    def updateGameInfo(self):
        self.limit = C.Speed[C.mode[1]]

    def gift(self):
        base = random.randint(1, 100)
        if base <= 20:
            times = int(len(self.segment) / 3)
            for index in range(times):
                self.delBack()
        else:
            value = random.randint(4, 20) * self.coin
            if self.mode == 0:
                C.addScore(value)
            if self.mode == 1 or (C.mode[3] == 3 and self.mode == 0):
                C.addScoreP1(value)
            if self.mode == 2:
                C.addScoreP2(value)
    def move(self, keys):
        # 更新游戏速度，模式
        self.updateGameInfo()
        if self.mode == 0:
            score = C.score
        elif self.mode == 1:
            score = C.scoreP1
        elif self.mode == 2:
            score = C.scoreP2

        if self.speed > 20 and C.mode[3] > 0:
            self.speed = max(30, self.limit * max(0.01, 1 - (score ** 0.5) / 30))
        if C.mode[3] == 2:
            self.speed = 2
        if C.mode[3] == 0:
            self.speed = self.limit
        self.coin = int(((200 - self.speed) ** 3 / 389000) + 5)
        if self.died:
            return

        if self.canMove:
            self.canMove = False
            self.changeDirection(keys)
            self.moveForward()
            # self.delBack()
        elif (C.mode[3] == 3 and self.mode == 0) or C.mode[3] == 1 or C.mode[3] == 0:
            # TODO 依然是判断按键的问题，和前两个TODO可以一起解决
            # 在两次检测是否可以移动的间隔， 有可能会忽略掉用户的按键
            # 用 preButton记录一下，如果有preButton，则优先执行preButton的指令
            if self.mode == 0 or self.mode == 1:
                if keys[pygame.K_LEFT]:
                    self.preButton = 'left'
                if keys[pygame.K_RIGHT]:
                    self.preButton = 'right'
                if keys[pygame.K_UP]:
                    self.preButton = 'up'
                if keys[pygame.K_DOWN]:
                    self.preButton = 'down'
            if self.mode == 0 or self.mode == 2:
                if keys[pygame.K_a]:
                    self.preButton = 'left'
                if keys[pygame.K_d]:
                    self.preButton = 'right'
                if keys[pygame.K_w]:
                    self.preButton = 'up'
                if keys[pygame.K_s]:
                    self.preButton = 'down'

        # 防止同一时间多次按键导致蛇体180度转弯
        if pygame.time.get_ticks() - self.timer > self.speed:
            self.canMove = True
            self.timer = pygame.time.get_ticks()
    def getImage(self, pre, now, nxt):
        bodyA = pygame.transform.scale(self.image_bodyA, (20, 20))
        bodyB = pygame.transform.scale(self.image_bodyB, (20, 20))
        prex, prey = pre
        nowx, nowy = now
        nxtx, nxty = nxt
        if prex < nowx: # 1
            if nowy > nxty: # 2
                return bodyA
            if nowy < nxty: # 4
                return pygame.transform.rotate(bodyA, 90)
            if nowx < nxtx: # 3
                return bodyB
        if prey < nowy: # 2
            if nowx > nxtx: # 1
                return bodyA
            if nowx < nxtx: # 3
                return pygame.transform.rotate(bodyA, 270)
            if nowy < nxty: # 4
                return pygame.transform.rotate(bodyB, 90)
        if prex > nowx: # 3
            if nowy > nxty: # 2
                return pygame.transform.rotate(bodyA, 270)
            if nowy < nxty: # 4
                return pygame.transform.rotate(bodyA, 180)
            if nowx > nxtx: # 1
                return bodyB
        if prey > nowy: # 4
            if nowx > nxtx: # 1
                return pygame.transform.rotate(bodyA, 90)
            if nowx < nxtx: # 3
                return pygame.transform.rotate(bodyA, 180)
            if nowy > nxty: # 2
                return pygame.transform.rotate(bodyB, 90)
        return pygame.transform.scale(self.image_body, (20, 20))

    # mode = 0 for WSAD, mod = 1 for 上下左右
    def update(self):

        self.state = []
        head = pygame.transform.scale(self.image_head, (20, 20))
        tail = pygame.transform.scale(self.image_tail, (20, 20))
        if self.direction == 'right':
            head = pygame.transform.rotate(head, 90)
        elif self.direction == 'up':
            head = pygame.transform.rotate(head, 180)
        elif self.direction == 'left':
            head = pygame.transform.rotate(head, 270)
        self.state.append((head, self.position))

        limit = int(len(self.segment) - 1)

        for index in range(1, limit):
            image = self.getImage(self.segment[index - 1], self.segment[index], self.segment[index + 1])
            self.state.append((image, self.segment[index]))

        dx = self.segment[limit][0] - self.segment[limit - 1][0]
        dy = self.segment[limit][1] - self.segment[limit - 1][1]
        if dx == 20 or dx == -580:
            tail = tail
        if dx == -20 or dx == 580:
            tail = pygame.transform.rotate(tail, 180)
        if dy == 20 or dy == -580:
            tail = pygame.transform.rotate(tail, 270)
        if dy == -20 or dy == 580:
            tail = pygame.transform.rotate(tail, 90)

        self.state.append((tail, self.segment[limit]))


    def draw(self, surface):
        for label in self.state:
            surface.blit(label[0], label[1])