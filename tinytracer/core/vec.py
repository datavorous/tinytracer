from random import uniform
from math import sqrt


class Vec3:
    # Vector3D class
    # has dot, cross, length, hadamard product, and operator overloading
    # TODO: port to numpy
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, t):
        if isinstance(t, Vec3):
            return Vec3(self.x * t.x, self.y * t.y, self.z * t.z)
        return Vec3(self.x * t, self.y * t, self.z * t)

    def __rmul__(self, t):
        return self * t

    def __truediv__(self, t):
        return self * (1.0 / t)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length_squared(self):
        return self.dot(self)

    def length(self):
        return sqrt(self.length_squared())

    def unit_vector(self):
        return self / self.length()

    def cross(self, other):
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def near_zero(self):
        # small number approximation
        s = 1e-8
        return abs(self.x) < s and abs(self.y) < s and abs(self.z) < s


def random_unit_vector():
    while True:
        p = Vec3(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))
        if p.length_squared() < 1:
            return p.unit_vector()


def random_in_hemisphere(normal):
    in_unit_sphere = random_unit_vector()
    if in_unit_sphere.dot(normal) > 0.0:
        return in_unit_sphere
    else:
        # i dont need to keep this right now,
        # might need for mirrors and all
        return -in_unit_sphere


Color = Vec3
