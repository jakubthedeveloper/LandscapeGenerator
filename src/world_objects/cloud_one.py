import random
from world_object import WorldObject

class CloudOne(WorldObject):
    pattern = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,1,1,1,1,1,0,0],
      [0,0,1,1,1,1,1,1,1,0],
      [0,0,1,1,1,1,1,1,1,1],
      [0,0,0,1,1,1,1,1,1,0],
      [0,0,0,0,0,0,0,0,0,0],
    ]

    colors = {}

    def __init__(self, size: float = 1.0, shade: float = 1.0):
        self.size = size
        self.shade = shade

        self.colors = {
            1: (self.shade * 255, self.shade * 255, self.shade * 255)
        }
