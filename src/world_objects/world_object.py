class WorldObject:
    pattern = []
    colors = {}
    size = 1.0
    shade = 1.0

    def getColor(self, x: int, y: int):
        if self.pattern[y][x] not in self.colors:
            return None

        return self.colors[self.pattern[y][x]]
