import pygame, random
from .. import constants as C
from .. import tools

class Wall:
    def __init__(self):
        self.wall = []
        self.image = pygame.image.load(C.bathPath + 'source/images/wall.png')
        self.image = pygame.transform.scale(self.image, (20, 20))

    def getStatus(self, level):
        status = []
        if level == 1:
            status.append(tools.reTrans((0, 9)))
            status.append(tools.reTrans((1, 9)))
            status.append(tools.reTrans((2, 9)))
            status.append(tools.reTrans((3, 9)))
            status.append(tools.reTrans((4, 9)))
            status.append(tools.reTrans((5, 9)))
            status.append(tools.reTrans((29, 9)))
            status.append(tools.reTrans((28, 9)))
            status.append(tools.reTrans((27, 9)))
            status.append(tools.reTrans((26, 9)))
            status.append(tools.reTrans((25, 9)))
            status.append(tools.reTrans((24, 9)))

            status.append(tools.reTrans((0, 20)))
            status.append(tools.reTrans((1, 20)))
            status.append(tools.reTrans((2, 20)))
            status.append(tools.reTrans((3, 20)))
            status.append(tools.reTrans((4, 20)))
            status.append(tools.reTrans((5, 20)))
            status.append(tools.reTrans((29, 20)))
            status.append(tools.reTrans((28, 20)))
            status.append(tools.reTrans((27, 20)))
            status.append(tools.reTrans((26, 20)))
            status.append(tools.reTrans((25, 20)))
            status.append(tools.reTrans((24, 20)))
        if level == 2:
            status.append(tools.reTrans((5, 9)))
            status.append(tools.reTrans((6, 9)))
            status.append(tools.reTrans((7, 9)))
            status.append(tools.reTrans((8, 9)))
            status.append(tools.reTrans((9, 9)))
            status.append(tools.reTrans((9, 8)))
            status.append(tools.reTrans((9, 7)))
            status.append(tools.reTrans((9, 6)))
            status.append(tools.reTrans((9, 5)))

            status.append(tools.reTrans((20, 5)))
            status.append(tools.reTrans((20, 6)))
            status.append(tools.reTrans((20, 7)))
            status.append(tools.reTrans((20, 8)))
            status.append(tools.reTrans((20, 9)))
            status.append(tools.reTrans((21, 9)))
            status.append(tools.reTrans((22, 9)))
            status.append(tools.reTrans((23, 9)))
            status.append(tools.reTrans((24, 9)))

            status.append(tools.reTrans((24, 20)))
            status.append(tools.reTrans((23, 20)))
            status.append(tools.reTrans((22, 20)))
            status.append(tools.reTrans((21, 20)))
            status.append(tools.reTrans((20, 20)))
            status.append(tools.reTrans((20, 21)))
            status.append(tools.reTrans((20, 22)))
            status.append(tools.reTrans((20, 23)))
            status.append(tools.reTrans((20, 24)))

            status.append(tools.reTrans((9, 20)))
            status.append(tools.reTrans((9, 21)))
            status.append(tools.reTrans((9, 22)))
            status.append(tools.reTrans((9, 23)))
            status.append(tools.reTrans((9, 24)))
            status.append(tools.reTrans((8, 20)))
            status.append(tools.reTrans((7, 20)))
            status.append(tools.reTrans((6, 20)))
            status.append(tools.reTrans((5, 20)))
        if level == 3:
            status.append(tools.reTrans((0, 14)))
            status.append(tools.reTrans((1, 14)))
            status.append(tools.reTrans((2, 14)))
            status.append(tools.reTrans((3, 14)))
            status.append(tools.reTrans((4, 14)))
            status.append(tools.reTrans((5, 14)))
            status.append(tools.reTrans((29, 16)))
            status.append(tools.reTrans((28, 16)))
            status.append(tools.reTrans((27, 16)))
            status.append(tools.reTrans((26, 16)))
            status.append(tools.reTrans((25, 16)))
            status.append(tools.reTrans((24, 16)))

            status.append(tools.reTrans((5, 9)))
            status.append(tools.reTrans((6, 9)))
            status.append(tools.reTrans((7, 9)))
            status.append(tools.reTrans((8, 9)))
            status.append(tools.reTrans((9, 9)))
            status.append(tools.reTrans((9, 8)))
            status.append(tools.reTrans((9, 7)))
            status.append(tools.reTrans((9, 6)))
            status.append(tools.reTrans((9, 5)))

            status.append(tools.reTrans((20, 5)))
            status.append(tools.reTrans((20, 6)))
            status.append(tools.reTrans((20, 7)))
            status.append(tools.reTrans((20, 8)))
            status.append(tools.reTrans((20, 9)))
            status.append(tools.reTrans((21, 9)))
            status.append(tools.reTrans((22, 9)))
            status.append(tools.reTrans((23, 9)))
            status.append(tools.reTrans((24, 9)))

            status.append(tools.reTrans((24, 20)))
            status.append(tools.reTrans((23, 20)))
            status.append(tools.reTrans((22, 20)))
            status.append(tools.reTrans((21, 20)))
            status.append(tools.reTrans((20, 20)))
            status.append(tools.reTrans((20, 21)))
            status.append(tools.reTrans((20, 22)))
            status.append(tools.reTrans((20, 23)))
            status.append(tools.reTrans((20, 24)))

            status.append(tools.reTrans((9, 20)))
            status.append(tools.reTrans((9, 21)))
            status.append(tools.reTrans((9, 22)))
            status.append(tools.reTrans((9, 23)))
            status.append(tools.reTrans((9, 24)))
            status.append(tools.reTrans((8, 20)))
            status.append(tools.reTrans((7, 20)))
            status.append(tools.reTrans((6, 20)))
            status.append(tools.reTrans((5, 20)))
        if level == 4:
            for i in range(30):
                x = random.randint(0, 29)
                y = random.randint(0, 29)
                if x == 5:
                    x = 6
                status.append(tools.reTrans((x, y)))
        if level == 5:
            # H
            status.append(tools.reTrans((4, 7)))
            status.append(tools.reTrans((4, 8)))
            status.append(tools.reTrans((4, 9)))
            status.append(tools.reTrans((4, 10)))
            status.append(tools.reTrans((4, 11)))
            status.append(tools.reTrans((5, 9)))
            status.append(tools.reTrans((6, 9)))
            status.append(tools.reTrans((7, 7)))
            status.append(tools.reTrans((7, 8)))
            status.append(tools.reTrans((7, 9)))
            status.append(tools.reTrans((7, 10)))
            status.append(tools.reTrans((7, 11)))
            # i
            status.append(tools.reTrans((9, 7)))
            status.append(tools.reTrans((9, 9)))
            status.append(tools.reTrans((9, 10)))
            status.append(tools.reTrans((9, 11)))

            # THX
            status.append(tools.reTrans((15 - 3, 20)))
            status.append(tools.reTrans((16 - 3, 20)))
            status.append(tools.reTrans((17 - 3, 20)))
            status.append(tools.reTrans((18 - 3, 20)))
            status.append(tools.reTrans((19 - 3, 20)))
            status.append(tools.reTrans((17 - 3, 21)))
            status.append(tools.reTrans((17 - 3, 22)))
            status.append(tools.reTrans((17 - 3, 23)))
            status.append(tools.reTrans((17 - 3, 24)))

            status.append(tools.reTrans((21 - 3, 20)))
            status.append(tools.reTrans((21 - 3, 21)))
            status.append(tools.reTrans((21 - 3, 22)))
            status.append(tools.reTrans((21 - 3, 23)))
            status.append(tools.reTrans((21 - 3, 24)))
            status.append(tools.reTrans((22 - 3, 22)))
            status.append(tools.reTrans((23 - 3, 22)))
            status.append(tools.reTrans((24 - 3, 20)))
            status.append(tools.reTrans((24 - 3, 21)))
            status.append(tools.reTrans((24 - 3, 22)))
            status.append(tools.reTrans((24 - 3, 23)))
            status.append(tools.reTrans((24 - 3, 24)))

            status.append(tools.reTrans((23, 20)))
            status.append(tools.reTrans((24, 20)))
            status.append(tools.reTrans((25, 21)))
            status.append(tools.reTrans((25, 22)))
            status.append(tools.reTrans((25, 23)))
            status.append(tools.reTrans((26, 24)))
            status.append(tools.reTrans((27, 24)))
            status.append(tools.reTrans((27, 20)))
            status.append(tools.reTrans((26, 21)))
            status.append(tools.reTrans((24, 23)))
            status.append(tools.reTrans((23, 24)))

        return status

    def update(self, wall):
        self.state = []
        for index in wall:
            self.state.append((self.image, index))

    def draw(self, surface):
        for label in self.state:
            surface.blit(label[0], label[1])