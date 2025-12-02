from math import radians, tan
from .ray import Ray
from .vec import Vec3


class Camera:
    def __init__(self, look_from, look_at, vup, vfov, aspect_ratio):
        # TODO: extensive re reading required
        theta = radians(vfov)
        h = tan(theta / 2)
        viewport_height = 2.0 * h
        viewport_width = aspect_ratio * viewport_height

        w = (look_from - look_at).unit_vector()
        u = vup.cross(w).unit_vector()
        v = w.cross(u)

        self.origin = look_from
        self.horizontal = viewport_width * u
        self.vertical = viewport_height * v
        self.lower_left_corner = (
            self.origin - self.horizontal / 2 - self.vertical / 2 - w
        )

    def get_ray(self, s, t):
        # translated origin sort of stuff
        return Ray(
            self.origin,
            self.lower_left_corner
            + s * self.horizontal
            + t * self.vertical
            - self.origin,
        )
