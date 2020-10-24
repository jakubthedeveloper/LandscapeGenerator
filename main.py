import sys
sys.path.insert(0, './src')
sys.path.insert(0, './src/world_objects')

import pygame
import pygame_gui
import random
from datetime import datetime
from gui import Gui
from world_object import WorldObject
from tree_one import TreeOne

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (800, 600) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption("Landscape generator")
pixel_size = 20
tree_space = 120

background = pygame.Surface((width, height))
background.fill(pygame.Color('#000000'))

gui = Gui(screen)

trees = []

def placeObject(object: WorldObject, offset_x, offset_y):
  global board
  for y in range(len(object.pattern)):
    for x in range(len(object.pattern[y])):
      color = object.getColor(x, y)
      if color:
        pygame.draw.rect(screen, color, (x * pixel_size + offset_x, int(y * pixel_size) + offset_y, pixel_size, pixel_size))

def initTrees():
  trees.clear()

  for i in range(0, 5):
    trees.append(TreeOne())


clock = pygame.time.Clock()
is_running = True

initTrees()

while is_running:
  time_delta = clock.tick(60)/1000.0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False

    if event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == gui.button_tree_space_plus:
          tree_space = tree_space + 5
        if event.ui_element == gui.button_tree_space_minus:
          tree_space = tree_space - 5
        if event.ui_element == gui.button_init_trees:
          initTrees()

    gui.process_event(event)

  screen.blit(background, (0, 0))

  for i in range(len(trees)):
    placeObject(trees[i], 45 + (i * tree_space), 400)

  gui.set_text('tree_space', str(tree_space))
  gui.update(time_delta)

  pygame.display.update()
