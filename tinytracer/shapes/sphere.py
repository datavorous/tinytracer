from math import sqrt


class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        # self.color = color
        self.material = material

    def hit(self, ray, t_min, t_max, hit_record):
        # the first part of the book explains this thing really well, im skipping it for now
        oc = ray.origin - self.center
        a = ray.direction.length_squared()
        half_b = oc.dot(ray.direction)
        c = oc.length_squared() - self.radius * self.radius

        # if imaginary roots, then no intersection
        discriminant = half_b * half_b - a * c
        if discriminant < 0:
            return False

        sqrtd = sqrt(discriminant)
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False

        hit_record.t = root
        hit_record.p = ray.at(hit_record.t)
        # hit_record.color = self.color
        outward_normal = (hit_record.p - self.center) / self.radius
        hit_record.set_face_normal(ray, outward_normal)

        hit_record.material = self.material

        return True
