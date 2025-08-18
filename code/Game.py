import pygame
from code.Menu import Menu
from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Level import Level
import sys


class Game:

  def __init__(self):
    pygame.init()
    self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

  def run(self):
    while True:
      menu = Menu(self.window)
      menu_return = menu.run()

      if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
        level = Level(self.window, 'Level1', menu_return)
        level_return = level.run()
        if level_return:
          level = Level(self.window, 'Level1', menu_return)
          level_return = level.run()
          if level_return:
            pass

      elif menu_return == MENU_OPTION[3]:
        pass
      elif menu_return == MENU_OPTION[4]:
        pygame.quit()  # Close Window
        quit()  # end pygame
      else:
        pygame.quit()
        sys.exit()
