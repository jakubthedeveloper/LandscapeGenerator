import random
from world_object import WorldObject

class Mountain(WorldObject):
    pattern = [
          [0,0,0,0,0,2,0,0,0,0,0],
          [0,0,0,0,2,2,2,0,0,0,0],
          [0,0,0,1,1,1,1,1,0,0,0],
          [0,0,1,1,1,1,1,1,1,0,0],
          [0,1,1,1,1,1,1,1,1,1,0],
          [1,1,1,1,1,1,1,1,1,1,1]
    ]

    colors = {}

    def __init__(self, size: float = 1.0, shade: float = 1.0, offset_x: int = 0, offset_y: int = 40):
        self.size = size
        self.shade = shade
        self.offset_x = offset_x
        self.offset_y = offset_y

        mountain_color_random = random.randint(80, 140)
        mountain_color = (self.shade * mountain_color_random, self.shade * mountain_color_random, self.shade * mountain_color_random)

        self.colors = {
            1: mountain_color,
            2: (
                  min(mountain_color[0] + 10, 255),
                  min(mountain_color[1] + 10, 255),
                  min(mountain_color[0] + 10, 255)
            )
        }

    def height(self, pixel_size):
        return int(self.size * len(self.pattern) * pixel_size)
