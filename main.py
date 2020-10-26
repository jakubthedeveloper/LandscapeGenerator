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
from mountain import Mountain
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
mountain_space = 220
test_text = ""
clouds_offset = 0
pixel_size = 20

background = pygame.Surface((width, height))
background.fill(pygame.Color('#79B2EC'))

gui = Gui(screen)
display = Display(screen, pixel_size)

mountains = []
trees = []
clouds = []

def initMountains():
  mountains.clear()

  for i in range(0,3):
      size = random.randint(160, 200) / 100
      shade = random.randint(80, 100) / 100

      mountains.append(Mountain(size, shade))

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

initMountains()
initTrees()
initClouds()

while is_running:
  time_delta = clock.tick(60)/1000.0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False

    if event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == gui.button_restart_mountains:
          initMountains()
        if event.ui_element == gui.button_restart_clouds:
          initClouds()
        if event.ui_element == gui.button_restart_trees:
          initTrees()

    gui.process_event(event)

  screen.blit(background, (0, 0))

  for i in range(len(mountains)):
      display.placeObject(mountains[i], 0 + (i * mountain_space), height - 92 - mountains[i].height(pixel_size))

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
