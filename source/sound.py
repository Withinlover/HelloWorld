import pygame

from . import constants as C

class Sound:
    def __init__(self):
        self.pathDefalut = C.bathPath + 'source/media/defalut.mp3'
        self.pathAdvance = C.bathPath + 'source/media/500.mp3'
        self.pathEat = C.bathPath + 'source/media/eat.wav'
        self.pathGift = C.bathPath + 'source/media/gift.wav'

        self.music = self.pathDefalut
        self.canPress = True
        self.play = True
        # 消除pygame.mixer.Sound() 的延迟
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.mixer.init()

    # 音效 - food
    def eat(self):
        if self.play:
            self.eatMusic = pygame.mixer.Sound(self.pathEat)
            self.eatMusic.play()

    # 音效 - gift
    def gift(self):
        if self.play:
            self.eatMusic = pygame.mixer.Sound(self.pathGift)
            self.eatMusic.play()

    # 更新音乐
    def update(self, keys):
        score = max(C.score, C.scoreP1 + C.scoreP2)
        if score > 1000 and self.music != self.pathAdvance:
            self.music = self.pathAdvance
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play()
        if score < 1000 and self.music != self.pathDefalut:
            self.music = self.pathDefalut
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play()

        if pygame.mixer.music.get_busy() != 1:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play()
        if keys[pygame.K_p] and self.canPress:
            self.canPress = False
            if self.play:
                pygame.mixer.music.pause()
                self.play = False
            else :
                pygame.mixer.music.unpause()
                self.play = True

        if not keys[pygame.K_p]:
            self.canPress = True


