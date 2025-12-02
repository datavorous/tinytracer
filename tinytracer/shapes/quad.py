class Quad:
    # this was easy to implement
    # p(u, v) = p0 + u*edge1 + v*edge2
    # take out the normal with cross product
    # then (ray.origin + t*ray.direction - p0)*normal = 0 for intersection
    # solve for t
    # check whether the intersection point is within the boundaries or not
    # find out how far along edge1 and edge2 the point is
    def __init__(self, p0, p1, p2, p3, material):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.material = material

        self.edge1 = self.p1 - self.p0
        self.edge2 = self.p3 - self.p0
        self.normal = self.edge1.cross(self.edge2).unit_vector()

    def hit(self, ray, t_min, t_max, hit_record):
        denom = self.normal.dot(ray.direction)
        if abs(denom) < 1e-6:  # getting used to this, earlier i would have ignored
            return False

        t = (self.p0 - ray.origin).dot(self.normal) / denom
        if t < t_min or t > t_max:
            return False

        p = ray.at(t) - self.p0
        u = p.dot(self.edge1) / self.edge1.length_squared()
        v = p.dot(self.edge2) / self.edge2.length_squared()

        if u < 0 or u > 1 or v < 0 or v > 1:
            return False

        hit_record.t = t
        hit_record.p = ray.at(t)
        hit_record.set_face_normal(ray, self.normal)
        hit_record.material = self.material

        return True
