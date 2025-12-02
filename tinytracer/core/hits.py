from .vec import Vec3

# hitrecord holds hit details
# hittable list manages all the objects and finds the CLOSEST hit


class HitRecord:
    def __init__(self):
        self.p = Vec3()
        # the hit Point (that's why its P) (wherever the ray intersects an object)
        self.normal = Vec3()
        self.t = 0.0
        self.front_face = False
        # whether the ray hit the front or back of face of the surface
        # im a bit confused about this front_face thing, i need to study; TODO
        self.color = Vec3(0.5, 0.5, 0.5)
        # surface color at the hit point

        # TODO: ADD MORE MATERIAL TYPES , add MATERIAL class
        self.material = None

    def set_face_normal(self, ray, outward_normal):
        # check if the ray is hitting from outside or inside
        # if from outside, then keep normal as is
        # if from inside, flip the normal to point against the ray
        self.front_face = ray.direction.dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal


class HittableList:
    """
    this is a scene manager
    it holds the objects which the ray hits first

    there is an object named "world" in main.py too
    """

    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def hit(self, ray, t_min, t_max, hit_record):
        temp_record = HitRecord()
        # temp storage for each obj's hit
        hit_anything = False

        closest_so_far = t_max
        # keeps track of the nearest hit (since mult objs could be in the path)

        for obj in self.objects:
            # loops over all objects
            # check if the CLOSEST HIT SO FAR (temp_re.t < closest so far)
            # if yes, update the closest so far
            # copies the temp record into the main hit record
            if obj.hit(ray, t_min, closest_so_far, temp_record):
                hit_anything = True
                closest_so_far = temp_record.t
                hit_record.p = temp_record.p
                hit_record.normal = temp_record.normal
                hit_record.t = temp_record.t
                hit_record.front_face = temp_record.front_face
                # hit_record.color = temp_record.color
                hit_record.material = temp_record.material

        return hit_anything
