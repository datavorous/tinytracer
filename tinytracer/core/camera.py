from math import radians, tan
from .ray import Ray
from .vec import Vec3, random_in_unit_disk


class Camera:
    def __init__(
        self,
        look_from,
        look_at,
        vup,
        vfov,
        aspect_ratio,
        defocus_angle=0.0,
        focus_dist=10.0,  # new parameter for focus distance
    ):
        """
        Initialize a thin-lens camera with depth of field support.

        The camera simulates a real lens: objects at focus_dist are sharp,
        while objects closer or farther appear blurred based on defocus_angle.
        """
        # Calculate viewport dimensions at the focus plane
        # The viewport sits at focus_dist, not at unit distance

        # TODO: extensive re reading required
        theta = radians(vfov)
        h = tan(theta / 2)
        viewport_height = 2.0 * h * focus_dist
        viewport_width = aspect_ratio * viewport_height

        w = (look_from - look_at).unit_vector()
        u = vup.cross(w).unit_vector()
        v = w.cross(u)

        self.origin = look_from
        self.horizontal = viewport_width * u
        self.vertical = viewport_height * v
        # Lower-left corner of the viewport (at focus distance)
        self.lower_left_corner = (
            self.origin - self.horizontal / 2 - self.vertical / 2 - w * focus_dist
        )  # Push viewport to focus plane

        self.defocus_angle = (
            defocus_angle  # controls aperture size and consequently blur strength
        )
        self.focus_dist = focus_dist  # distance at which objects are in perfect focus
        defocus_radius = focus_dist * tan(radians(defocus_angle / 2))
        self.defocus_disk_u = u * defocus_radius
        self.defocus_disk_v = v * defocus_radius

    def get_ray(self, s, t):
        # translated origin sort of stuff
        """
        Generate a ray for rendering with optional depth of field.

        For pinhole cameras (defocus_angle=0), all rays originate from the camera center.
        For thin-lens cameras (defocus_angle>0), rays originate from random points on
        the aperture disk, creating realistic focus blur.
        """
        pixel_sample = self.lower_left_corner + s * self.horizontal + t * self.vertical

        if self.defocus_angle <= 0.0:
            ray_origin = self.origin
        else:
            ray_origin = self.defocus_disk_sample()
        return Ray(
            ray_origin,
            pixel_sample - ray_origin,
        )

    def defocus_disk_sample(self):
        # sample a point on the defocus disk
        """
        Sample a random point on the camera's circular aperture.

        This simulates how real camera lenses work: light enters through
        different points on the lens, causing objects not at focus_dist
        to appear blurred. The disk size is controlled by defocus_angle.
        """
        p = random_in_unit_disk()
        return self.origin + (p.x * self.defocus_disk_u) + (p.y * self.defocus_disk_v)
