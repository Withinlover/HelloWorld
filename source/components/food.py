import pygame
import random

from . import snack
from .. import constants as C
from .. import tools

class Food:
    def __init__(self):
        # 普通食物
        self.positionX = random.randint(0, 29) * 20 + 200
        self.positionY = random.randint(0, 29) * 20
        self.position = self.positionX, self.positionY

        # 特殊食物
        self.existGift = False
        self.giftX = 0
        self.giftY = 0
        self.gift = self.giftX, self.giftY

        # 食物位置
        self.status = []
        self.loadImage()


    def loadImage(self):
        self.basePath =  C.bathPath
        self.foodImage = pygame.image.load(self.basePath + 'source/images/apple.png')
        self.giftImage = pygame.image.load(self.basePath + 'source/images/gift.png')


    def new(self, P1 = [], P2 = []):
        self.position = tools.randPosition(P1, P2)
        self.positionX, self.positionY = self.position
        rand = random.randint(1, 100)
        if rand <= 10:
            self.existGift = True
            self.gift = tools.randPosition(P1, P2)
            self.giftX, self.giftY = self.gift

    def update(self):
        food = pygame.transform.scale(self.foodImage, (20, 20))
        gift = pygame.transform.scale(self.giftImage, (20, 20))

        self.status = []
        self.status.append((food, (self.positionX, self.positionY)))
        if self.existGift:
            self.status.append((gift, (self.giftX, self.giftY)))

    def draw(self, surface):
        for label in self.status:
            surface.blit(label[0], label[1])