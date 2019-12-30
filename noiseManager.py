class Vec2 :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

class Pixel :
    def __init__(self, pos, brightness) :
        self.pos = pos
        self.brightness = brightness

class perlinNoise :
    def __init__(self, size, points, scale, threshold) :
        self.size = size
        self.points = points
        self.scale = scale
        self.threshold = threshold