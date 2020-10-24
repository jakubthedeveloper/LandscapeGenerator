import pygame
import pygame_gui
#import pygame.freetype
from datetime import datetime

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (800, 800) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption("Landscape generator")
pixel_size = 20
tree_space = 20
font = pygame.font.Font(pygame.font.get_default_font(), 18)

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

button_tree_space_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='tree space +',
                                             manager=manager)

button_tree_space_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 350), (100, 50)),
                                             text='tree space -',
                                             manager=manager)

class WorldObject:
    pattern = []
    colors = {}

    def getColor(self, x: int, y: int):
        if self.pattern[y][x] not in self.colors:
            return None

        return self.colors[self.pattern[y][x]]


class TreeOne(WorldObject):
    pattern = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,2,2,2,0,0,0],
      [0,0,0,2,2,2,2,2,0,0],
      [0,0,0,2,2,2,2,2,0,0],
      [0,0,0,0,2,1,2,0,0,0],
      [0,0,0,0,0,1,0,0,0,0],
      [0,0,0,0,0,1,0,0,0,0],
      [0,0,0,0,0,1,0,0,0,0],
    ]

    colors = {
        1: (255, 119, 0),
        2: (0, 255, 0)
    }


def placeObject(object: WorldObject, offset_x, offset_y):
  global board
  for y in range(len(object.pattern)):
    for x in range(len(object.pattern[y])):
      color = object.getColor(x, y)
      if color:
        pygame.draw.rect(screen, color, (x * pixel_size + offset_x, int(y * pixel_size) + offset_y, pixel_size, pixel_size))


clock = pygame.time.Clock()
is_running = True

while is_running:
  time_delta = clock.tick(60)/1000.0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False

    if event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == button_tree_space_plus:
          tree_space = tree_space + 5
        if event.ui_element == button_tree_space_minus:
          tree_space = tree_space - 5

    manager.process_events(event)

  manager.update(time_delta)
  screen.blit(background, (0, 0))

  for i in range(0, 5):
    placeObject(TreeOne(), 45 + (i * tree_space), 45)

  manager.draw_ui(screen)
  text_surface = font.render('tree space ' + str(tree_space), True, (255, 255, 255))
  screen.blit(text_surface, dest=(20,400))

  pygame.display.update()
