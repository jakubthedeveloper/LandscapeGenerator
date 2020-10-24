import random
from world_object import WorldObject

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

    colors = {}

    def __init__(self):
        shade = random.randint(0, 80)
        self.colors = {
            1: (255 - shade, 119 - shade, 0),
            2: (0, 255 - shade, 0)
        }
