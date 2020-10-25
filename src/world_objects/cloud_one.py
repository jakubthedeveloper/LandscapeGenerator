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

    def __init__(self, size: float = 1.0, shade: float = 1.0, offset_x: int = 0, offset_y: int = 40):
        self.size = size
        self.shade = shade
        self.offset_x = offset_x
        self.offset_y = offset_y

        self.colors = {
            1: (self.shade * 255, self.shade * 255, self.shade * 255)
        }
