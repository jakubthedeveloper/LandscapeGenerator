import random
import pygame
from world_object import WorldObject

class Tree(WorldObject):
    pattern = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,2,2,2,0,0,0],
      [0,0,0,2,2,2,2,2,0,0],
      [0,0,0,2,2,2,2,2,0,0],
      [0,0,0,2,2,2,2,2,0,0],
      [0,0,0,0,2,1,2,0,0,0],
      [0,0,0,0,0,1,0,0,0,0],
      [0,0,0,0,0,1,0,0,0,0],
      [0,0,0,0,0,1,0,0,0,0],
    ]

    colors = {}

    def __init__(self, size: float = 1.0, shade: float = 1.0):
        self.size = size
        self.shade = shade
        #self.image = pygame.image.load('./images/tree.png')
        self.colors = {
            1: (self.shade * 200, self.shade * 119, 0),
            2: (0, self.shade * 180, 0)
        }
