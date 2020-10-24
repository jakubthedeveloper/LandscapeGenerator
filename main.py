import sys
sys.path.insert(0, './src')
sys.path.insert(0, './src/world_objects')

import pygame
import pygame_gui
import random
import math
from datetime import datetime
from gui import Gui
from world_object import WorldObject
from tree_one import TreeOne
from cloud_one import CloudOne

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (800, 600) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption("Landscape generator")
pixel_size = 20
tree_space = 130
test_text = "test"

background = pygame.Surface((width, height))
background.fill(pygame.Color('#79B2EC'))

gui = Gui(screen)

trees = []
clouds = []

def placeObject(object: WorldObject, offset_x, offset_y):
  global board
  for y in range(len(object.pattern)):
    for x in range(len(object.pattern[y])):
      color = object.getColor(x, y)
      if color:
        pygame.draw.rect(
          screen,
          color,
          (
            int(x * math.floor(pixel_size * object.size)) + offset_x,
            int(y * math.floor(pixel_size * object.size)) + offset_y,
            int(pixel_size * object.size),
            int(pixel_size * object.size)
          )
        )

def initTrees():
  trees.clear()

  for i in range(0, 5):
    size = random.randint(60, 100) / 100
    shade = size # achieve depth by relating shade and size

    trees.append(TreeOne(size, shade))

def initClouds():
  clouds.clear()

  for i in range(0, 2):
    size = random.randint(80, 100) / 100
    shade = size # achieve depth by relating shade and size

    clouds.append(CloudOne(size, shade))


clock = pygame.time.Clock()
is_running = True

initTrees()
initClouds()

while is_running:
  time_delta = clock.tick(60)/1000.0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False

    if event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == gui.button_test_one:
          test_text = "test 1"
        if event.ui_element == gui.button_test_two:
          test_text = "test 2"
        if event.ui_element == gui.button_init_trees:
          initTrees()

    gui.process_event(event)

  screen.blit(background, (0, 0))

  #grass
  pygame.draw.rect(
    screen,
    (0, 78, 0),
    (0, 500, width, height)
  )

  for i in range(len(trees)):
    placeObject(trees[i], 45 + (i * tree_space), 400)

  for i in range(len(clouds)):
    placeObject(clouds[i], 100 + i * 350, 40)

  gui.set_text('test', str(test_text))
  gui.update(time_delta)

  pygame.display.update()
