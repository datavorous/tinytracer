class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        # ray equation: P(t) = A + tB
        return self.origin + t * self.direction
