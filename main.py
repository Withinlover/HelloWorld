import pygame, os, sys

from source import tools, setup
from source import constants as C
from source.states import MainMenu, LoadScreen, SinglePlayer, GameOver
from source.states import MultiPlayer, AI, ManAI

# 路径获取
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    C.bathPath = resource_path('')
    state_dict = {
        'MainMenu' : MainMenu.MainMenu(),
        'LoadScreen' : LoadScreen.LoadScreen(),
        'SinglePlayer' : SinglePlayer.SinglePlayer(),
        'GameOver': GameOver.GameOver(),
        'MultiPlayer': MultiPlayer.MultiPlayer(),
        'Auto': AI.AI(),
        'ManAI': ManAI.ManAI()
    }
    game = tools.Game(state_dict, 'MainMenu')
    game.run()

if __name__ == '__main__':
    main()

