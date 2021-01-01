import pygame
import json

from ..components import info
from .. import constants as C
from .. import tools

class GameOver:
    def __init__(self):
        self.finished = False
        self.next = 'MainMenu'
        self.info = info.Info('GameOver')
        path = C.bathPath + 'source/images/background.png'
        self.Background = pygame.image.load(path)

    # 更新存档
    def updateSave(self):
        try:
            f = open('save.json')
            dict = json.load(f)
            f.close()
        except:
            dict = {}

        try:
            if C.mode[3] == 3:
                dict[tools.getSaveInfo()] = max(C.score, dict[tools.getSaveInfo()])
            else:
                dict[tools.getSaveInfo()] = max(max(C.score, C.scoreP1 + C.scoreP2), dict[tools.getSaveInfo()])
        except:
            if C.mode[3] == 3:
                dict[tools.getSaveInfo()] = C.score
            else:
                dict[tools.getSaveInfo()] = max(C.score, C.scoreP1, C.scoreP2)

        data = json.dumps(dict)
        print(data)

        with open('save.json', 'w') as f:
            f.write(data)
        f.close()

    def update(self, surface, keys):
        if(keys[pygame.K_SPACE]):
            self.updateSave()
            self.finished = True
            self.next = 'MainMenu'
            C.addScore(-C.score)
            C.addScoreP2(-C.scoreP2)
            C.addScoreP1(-C.scoreP1)
            C.level = 1

        self.draw(surface)

    def draw(self, surface):
        surface.blit(self.Background, (0, 0))

        self.info.update()
        self.info.draw(surface)