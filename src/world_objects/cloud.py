import random
from world_object import WorldObject

class Cloud(WorldObject):
    patterns = {
      0: [
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,1,1,1,1,1,0,0],
          [0,0,1,1,1,1,1,1,1,0],
          [0,0,1,1,1,1,1,1,1,1],
          [0,0,0,1,1,1,1,1,1,0],
          [0,0,0,0,0,0,0,0,0,0]
      ],
      1: [
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,1,1,1,1,1,1,0,0],
          [1,1,1,1,1,1,1,1,1,0],
          [1,1,1,1,1,1,1,1,1,1],
          [0,1,1,1,1,1,1,1,1,0],
          [0,0,1,1,1,1,1,0,0,0]
      ]
    }

    colors = {}

    def __init__(self, patternIndex: int = 0, size: float = 1.0, shade: float = 1.0, offset_x: int = 0, offset_y: int = 40, speed: int = 60):
        self.patternIndex = patternIndex
        self.pattern = self.patterns[self.patternIndex]
        self.size = size
        self.shade = shade
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.speed = speed

        self.colors = {
            1: (self.shade * 255, self.shade * 255, self.shade * 255)
        }
