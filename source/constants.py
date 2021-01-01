from . import tools
import os, sys

# 窗口大小
ScreenWidth, ScreenHeight = 800, 600
ScreenSize = ScreenWidth, ScreenHeight

# 绝对目录
# bathPath = 'D:/Code/Python/WorkSpace/Snack_1.0.1/'
# 相对目录
bathPath = ''
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# 字体
# FONT ='SimHei'
FONT = '隶书,dengxian,SimHei'
# FONT = 'script' 花体，仅英文
# FONT = 'dengxian'
#

# 颜色 - 挑选自： https://wenku.baidu.com/view/823dca44b307e87101f6961b.html
whiltColor = (255, 255, 255)
blackColor = (0, 0, 0)
pinkColor = (255, 192, 203)
purpleColor = (96, 135, 176)
blueColor = (0, 191, 255)
greenColor = (0, 250, 154)
greenColorDark = (107, 142, 35)
yelloColor = (255, 255, 0)
goldColor = (255, 215, 0)
brownColor = (184, 134, 11)
orangeColor = (255, 165, 0)
redColor = (255, 0, 0)
redColorDark = (178, 34, 34)

# 游戏速度，Normal == 10
Speed = [300, 200, 100, 50]

# 光标
CursorSize = 30, 30
CursorPosition = [[170, 200], [170, 300], [170, 400], [170, 500]]

# info
MainInfo = ['开始游戏', '难度选择', '边界判定', '游戏模式']
MainInfoPosition = [(220, 190),(220, 290),(220, 390),(220, 490)]
ModeInfo = [[''], ['Easy', 'Normal', 'Hard', 'Impossible'], ['Die', 'Cross'], ['Single', 'Double', 'Auto', 'Man Vs AI']]
ModeInfoPosition = [(520, 205),(520, 305),(520, 405),(520, 505)]

# 模式的选择信息
mode = [0, 1, 0, 0]
def updateMode(newMode):
    global mode
    mode = newMode
level = 1

# 游戏得分
score = 0
def addScore(value):
    global score
    score += value

scoreP1 = 0
def addScoreP1(value):
    global scoreP1
    scoreP1 += value

scoreP2 = 0
def addScoreP2(value):
    global scoreP2
    scoreP2 += value

# 蛇的长度
lenthP1 = 3
def updateP1(lenth):
    global lenthP1
    lenthP1 = lenth

lenthP2 = 3
def updateP2(lenth):
    global lenthP2
    lenthP2 = lenth

# 运行时间

timer = 0
def updateTimer(value):
    global timer
    timer = value
