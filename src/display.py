import sys
sys.path.insert(0, './src/world_objects')
from world_object import WorldObject
import pygame
import math

class Display:

  def __init__(self, screen, pixel_size):
    self.screen = screen
    self.width, self.height = screen.get_size()
    self.pixel_size = pixel_size

  def placeObject(self, object: WorldObject, offset_x, offset_y):
    if object.image == None:
      return self.placePattern(object, offset_x, offset_y)

    return self.placeImage(object, offset_x, offset_y)

  def placeImage(self, object: WorldObject, offset_x, offset_y):
    self.screen.blit(
        pygame.transform.rotozoom(object.image, 0, object.size),
        (offset_x, offset_y)
    )

  def placePattern(self,  object: WorldObject, offset_x, offset_y):
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
