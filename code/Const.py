import pygame

#Colors
C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_RED = (255, 0, 0)
C_BLACK =(0, 0, 0)

#Medidas
WIN_WIDTH = 512
WIN_HEIGHT = 512

#Menu
MENU_OPTION = ('NEW GAME 1P', 'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE', 'SCORE', 'EXIT')

ENTITY_SPEED = {
    'Level1Bg0': 4,
    'Level1Bg1': 2,
    'Level1Bg2': 2,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 6,
    'Enemy2': 6
}

PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

#CONFIGS
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

SPAWN_TIME = 500

TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 30000  # 30s
