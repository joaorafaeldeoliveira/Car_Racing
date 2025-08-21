import pygame

#Colors
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)

#Medidas
WIN_WIDTH = 512
WIN_HEIGHT = 512

#Menu
MENU_OPTION = ('NEW GAME 1P', 'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE', 'SCORE', 'EXIT')

#ENTITY STATUS

ENTITY_SPEED = {
    'Level1Bg0': 4,
    'Level1Bg1': 2,
    'Level1Bg2': 2,
    'Level2Bg0': 4,
    'Level2Bg1': 2,
    'Level2Bg2': 2,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 6,
    'Enemy2': 6
}
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 1,
    'Enemy2': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 5,
    'Enemy2': 5,
}
ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 100,
    'Enemy2': 125,
}

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190),
    5: (WIN_WIDTH / 2, 210),
    6: (WIN_WIDTH / 2, 230),
    7: (WIN_WIDTH / 2, 250),
    8: (WIN_WIDTH / 2, 270),
    9: (WIN_WIDTH / 2, 290),
}

PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

#CONFIGS
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
EVENT_SCORE = pygame.USEREVENT + 3

#TIME CONFIGS
SPAWN_TIME = 500
SCORE_TIME = 1000

TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 30000
