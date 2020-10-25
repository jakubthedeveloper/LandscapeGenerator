import sys
sys.path.insert(0, './src/world_objects')
from world_object import WorldObject
import pygame
import math

class Display:
  pixel_size = 20

  def __init__(self, screen):
    self.screen = screen
    self.width, self.height = screen.get_size()

  def placeObject(self, object: WorldObject, offset_x, offset_y):
    for y in range(len(object.pattern)):
      for x in range(len(object.pattern[y])):
        color = object.getColor(x, y)
        if color:
          pygame.draw.rect(
            self.screen,
            color,
            (
              int(x * math.floor(self.pixel_size * object.size)) + offset_x,
              int(y * math.floor(self.pixel_size * object.size)) + offset_y,
              int(self.pixel_size * object.size),
              int(self.pixel_size * object.size)
            )
          )

  def drawGrass(self):
    pygame.draw.rect(
      self.screen,
      (0, 78, 0),
      (0, 500, self.width, self.height)
    )
