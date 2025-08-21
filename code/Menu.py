import pygame
from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, C_WHITE, C_YELLOW, C_ORANGE, C_RED, C_BLACK
from pygame import Surface, Rect
from pygame.font import Font


class Menu:

  def __init__(self, window):
    self.window = window
    self.surf = pygame.image.load('./asset/Bg.png').convert()
    self.rect = self.surf.get_rect(topleft=(0, 0))

  def run(self):
    menu_option = 0
    clock = pygame.time.Clock()
    while True:
      self.window.blit(self.surf, self.rect)

      self.menu_text(60, "CAR", C_RED, (WIN_WIDTH // 2, 100))
      self.menu_text(40, "RACING", C_RED, (WIN_WIDTH // 2, 160))

      for i, option in enumerate(MENU_OPTION):
        color = C_ORANGE if i == menu_option else C_WHITE
        self.menu_text(18, option, color, (WIN_WIDTH // 2, 220 + 35 * i))

      pygame.display.flip()
      clock.tick(30)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:
            menu_option = (menu_option + 1) % len(MENU_OPTION)

          elif event.key == pygame.K_UP:
            menu_option = (menu_option - 1) % len(MENU_OPTION)

          elif event.key == pygame.K_RETURN:
            return MENU_OPTION[menu_option]

  def menu_text(self, text_size: int, text: str, text_color: tuple,
                text_center_pos: tuple):
    try:
      text_font: Font = pygame.font.Font("./asset/PressStart2P.ttf", text_size)
    except:
      text_font: Font = pygame.font.SysFont("Arial", text_size)

    text_surf: Surface = text_font.render(text, True,
                                          text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    self.window.blit(text_surf, text_rect)
