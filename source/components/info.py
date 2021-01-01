import pygame
import json
from .. import constants as C
from .. import tools

class Info:
    def __init__(self, state):
        self.state = state
        self.creatTitle()

        self.timer = pygame.time.get_ticks()
        self.blink = True

        self.basePath = C.bathPath

    def creatTitle(self):
        self.stateLables = []
        self.stateLables.append((self.creatLable('贪吃蛇', color=C.whiltColor, size=100), (50, 50)))
        self.stateLables.append((self.creatLable('Code by HZY', color=C.orangeColor ,size=30), (500, 105)))

    def creatLable(self, label, color = C.pinkColor, size = 50, widthScale = 1.25, heightScale = 1):
        font = pygame.font.SysFont(C.FONT, size)
        labelImage = font.render(label, 1, color)
        rect = labelImage.get_rect()
        labelImage = pygame.transform.scale(labelImage, (int(rect.width * widthScale), int(rect.height * heightScale)))
        return labelImage

    def update(self):
        self.stateLables = []

        position = tools.getSaveInfo()
        try:
            f = open('save.json')
            dict = json.load(f)
            try:
                bestScore = dict[position]
            except:
                bestScore = 0
            f.close()
        except:
            bestScore = 0

        if(self.state == 'MainMenu'):
            index = C.mode[0]
            stat = C.mode
            stat[0] = 0

            logo = pygame.image.load(self.basePath + 'source/images/logo.png')
            logo = pygame.transform.scale(logo, (389, 120))
            self.stateLables.append((logo, (50, 50)))
            self.stateLables.append((self.creatLable('Code by HZY',color=C.redColor ,size=30), (500, 105)))
            Colors = [C.orangeColor, C.orangeColor, C.orangeColor, C.orangeColor]
            Colors[index] = C.pinkColor
            for i in range (4):
                self.stateLables.append((self.creatLable(C.MainInfo[i], Colors[i]), C.MainInfoPosition[i]))
                self.stateLables.append((self.creatLable(C.ModeInfo[i][stat[i]], Colors[i], size=30), C.ModeInfoPosition[i]))
            self.stateLables.append((self.creatLable('Press P to control music, SPACE to make choice', color=C.brownColor, size=18), (140, 570)))

        if(self.state == 'LoadScreen'):
            self.stateLables.append((self.creatLable('1P 使用上下左右控制', color=C.whiltColor, size=30), (170, 100)))
            self.stateLables.append((self.creatLable('2P 使用W A S D控制', color=C.whiltColor, size=30), (170, 150)))
            self.stateLables.append((self.creatLable('单人模式两种操作均可接受', color=C.whiltColor, size=30), (170, 200)))
            self.stateLables.append((self.creatLable('按P键可以控制音乐的开关', color=C.whiltColor, size=30), (170, 300)))
            self.stateLables.append((self.creatLable('AI模式下按空格键可以提前终止游戏', color=C.whiltColor, size=30), (170, 350)))
            self.stateLables.append((self.creatLable('地图上随机出现特殊道具', color=C.whiltColor, size=30), (170, 400)))
            self.stateLables.append((self.creatLable('多种特殊效果随机出现', color=C.whiltColor, size=30), (170, 450)))

        if(self.state == 'Single'):
            self.stateLables.append((self.creatLable((str(C.score)), color=C.brownColor, size=28), (78, 138)))
            self.stateLables.append((self.creatLable((str(int(C.timer))), color=C.brownColor, size=30), (78, 292)))
            self.stateLables.append((self.creatLable((str(C.lenthP1)), color=C.brownColor, size=40), (78, 445)))
            if C.mode[3] == 0:
                self.stateLables.append((self.creatLable('Level', color=C.brownColor, size=20), (200, 0)))
                self.stateLables.append((self.creatLable(str(C.level), color=C.brownColor, size=20), (280, 0)))

        if self.state == 'MultiPlayer' :
            self.stateLables.append((self.creatLable((str(C.scoreP1)), color=C.brownColor, size=28), (78, 138)))
            self.stateLables.append((self.creatLable((str(C.scoreP2)), color=C.brownColor, size=28), (78, 448)))
            self.stateLables.append((self.creatLable((str(int(C.lenthP1))), color=C.brownColor, size=30), (78, 196)))
            self.stateLables.append((self.creatLable((str(int(C.lenthP2))), color=C.brownColor, size=30), (78, 506)))

        if(self.state == 'GameOver'):
            if pygame.time.get_ticks() - self.timer > 200 + int(self.blink) * 200:
                self.timer = pygame.time.get_ticks()
                self.blink = not self.blink
            score = max(C.score, C.scoreP2, C.scoreP1)
            if C.mode[3] == 3:
                score = C.scoreP1
            if C.mode[3] == 0 or C.mode[3] == 2:
                self.stateLables.append((self.creatLable('Game Over', color=C.brownColor, size=100), (100, 100)))
                self.stateLables.append((self.creatLable('Your score is:', color=C.brownColor, size=30), (170, 250)))
                self.stateLables.append((self.creatLable(str(score), color=C.redColor, size=30), (550, 250)))
                self.stateLables.append((self.creatLable('Your best score is:', color=C.brownColor, size=30), (170, 350)))
                self.stateLables.append((self.creatLable(str(bestScore), color=C.redColor, size=30), (550, 350)))
            if C.mode[3] == 1:
                if C.scoreP1 > C.scoreP2:
                    self.stateLables.append((self.creatLable('Player1 Wins!', color=C.brownColor, size=70), (100, 100)))
                if C.scoreP2 > C.scoreP1:
                    self.stateLables.append((self.creatLable('Player2 Wins!', color=C.brownColor, size=70), (100, 100)))
                if C.scoreP1 == C.scoreP2:
                    self.stateLables.append((self.creatLable('Draw', color=C.brownColor, size=100), (100, 100)))
                self.stateLables.append((self.creatLable('Your score is:', color=C.brownColor, size=30), (170, 250)))
                self.stateLables.append((self.creatLable(str(score), color=C.redColor, size=30), (550, 250)))
                self.stateLables.append((self.creatLable('Your best score is:', color=C.brownColor, size=30), (170, 350)))
                self.stateLables.append((self.creatLable(str(bestScore), color=C.redColor, size=30), (550, 350)))

            if C.mode[3] == 3:
                if C.scoreP1 > C.scoreP2:
                    self.stateLables.append((self.creatLable('Player Wins!', color=C.brownColor, size=70), (100, 100)))
                if C.scoreP2 > C.scoreP1:
                    self.stateLables.append((self.creatLable('Computer Wins!', color=C.brownColor, size=70), (100, 100)))
                if C.scoreP1 == C.scoreP2:
                    self.stateLables.append((self.creatLable('Draw', color=C.brownColor, size=100), (100, 100)))
                self.stateLables.append((self.creatLable('Your score is:', color=C.brownColor, size=30), (170, 250)))
                self.stateLables.append((self.creatLable(str(score), color=C.redColor, size=30), (550, 250)))
                self.stateLables.append((self.creatLable('Your best score is:', color=C.brownColor, size=30), (170, 350)))
                self.stateLables.append((self.creatLable(str(bestScore), color=C.redColor, size=30), (550, 350)))

            if self.blink:
                self.stateLables.append((self.creatLable('Press SPACE to return to the main menu', color=C.blackColor, size=20), (125, 450)))

    def draw(self, surface):
        for label in self.stateLables:
            surface.blit(label[0], label[1])