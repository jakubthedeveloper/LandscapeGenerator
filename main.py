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
from tree import Tree
from cloud import Cloud
from display import Display

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
(width, height) = (800, 600) # Dimension of the window
screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption("Landscape generator")
tree_space = 150
test_text = "test"
clouds_offset = 0

background = pygame.Surface((width, height))
background.fill(pygame.Color('#79B2EC'))

gui = Gui(screen)
display = Display(screen)

trees = []
clouds = []

def initTrees():
  trees.clear()

  for i in range(0, 5):
    size = random.randint(60, 100) / 100
    shade = size # achieve depth by relating shade and size

    trees.append(Tree(size, shade))

def initClouds():
  clouds.clear()

  for i in range(0, 3):
    size = random.randint(80, 100) / 100
    shade = size # achieve depth by relating shade and size

    clouds.append(Cloud(
                    i % 2,
                    size,
                    shade, i * 350,
                    random.randint(30, 50),
                    random.randint(20, 80)
                  )
    )

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
        if event.ui_element == gui.button_init_clouds:
          initClouds()
        if event.ui_element == gui.button_init_trees:
          initTrees()

    gui.process_event(event)

  screen.blit(background, (0, 0))

  display.drawGrass()

  for i in range(len(trees)):
    display.placeObject(trees[i], 45 + (i * tree_space), 400)

  clouds_offset += time_delta * 80
  clouds_offset = clouds_offset % width

  for i in range(len(clouds)):
    clouds[i].offset_x = clouds[i].offset_x + (time_delta * clouds[i].speed)

    if clouds[i].offset_x > width:
        clouds[i].offset_x = -100

    display.placeObject(clouds[i], clouds[i].offset_x, clouds[i].offset_y)

  gui.set_text('test', str(test_text))
  gui.update(time_delta)

  pygame.display.update()
