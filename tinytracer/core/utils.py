from .hits import HitRecord
from .ray import Ray
import math
from .vec import Vec3, Color
import random


def ray_color(ray, world, depth):
    # the heart, the beating heart
    hit_record = HitRecord()

    # if we've exceeded the ray bounce limit no more light is gathered
    if depth <= 0:
        return Color(0, 0, 0)
        # btw changing this to white gives a cool light like effect

    if depth < 40:
        if random.random() > 0.9:
            return Color(0, 0, 0)

    # goto hits.py for more info
    if world.hit(ray, 0.001, float("inf"), hit_record):

        """
        Adding emissive properties now (this is an edit)
        """
        emission = hit_record.material.emitted()
        scattered, scattered_ray, attenuation = hit_record.material.scatter(
            ray, hit_record
        )

        if scattered:
            # Recursive ray tracing with material-based attenuation
            return emission + attenuation * ray_color(scattered_ray, world, depth - 1)
        else:
            # Ray was absorbed, return only emission
            return emission
        """
        Tells if this ray hits anything in the scene, and if yes, gives the details of the closest hit


        world contains all the sphere objects inside it

        that .hit() function checks and tries to find the nearest intersection of the ray with any sphere
        simple quadratic equation, solves for discriminant
        the closest intersection is chosesn
        if an intersection exists it fills hit_record with that object's point normal color etc
        if nothing, then returns false, and we do some sky color grading then

        btw, t_min helps to avoid self intersection, just in case the ray start exactly on a surface
        float('inf') weird syntax, but it means the ray can go as far as it ones

        after this if statement we can safely use hit_record's p, normal and color
        we get the point where the ray is hit, and the surface normal (pointing outward)
        for diffusive shading, we are using random unit vector (uniformly distributed)

        what it does:
        start at the hit point
        nudge in the direction ofo the surface normal
        add some randomness so the bounce is not deterministic

        HENCE! the new ray is scatter in a random direction within the hemisphere above the surface to SIMULATE DIFFUSE REFLECTION!
        """
        target = hit_record.p + hit_record.normal + random_unit_vector()
        # we create a new ray at the hit point
        # and the direction is from hit point to the random offset
        scattered_ray = Ray(hit_record.p, target - hit_record.p)

        """
        recursion!
        we recursively compute the color of the bounced ray
        depth - 1 makes sure that the recursion actually stops

        we add some "tint" color of the surface which we had hit
        so if the sphere is red, the scattered light inherits that "redness"

        0.7 is the energy loss factor per bounce
        this prevents infinite brightness buildup
        """
        return hit_record.color * 0.69 * ray_color(scattered_ray, world, depth - 1)

        """
        Summary korle darabe:
        1. ray hits and object
        2. it scatters into a new random dir
        3. then new ray MAY hit another object, bounce again or escape into the void
        4. at each bounce the color is multiplied by the surface and slightly dimmed cause energy is lost
        5. after many rays are traced the image converged and give soft lighting effect
        """

    # this does the sky gradient
    # directly copied from ray tracing in one weekend book
    if not hasattr(ray.direction, "_unit_cache"):
        ray.direction._unit_cache = ray.direction.unit_vector()
    # unit_direction = ray.direction.unit_vector()
    unit_direction = ray.direction._unit_cache
    t = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - t) * Color(0.7, 0.7, 0.7) + t * Color(0.3, 0.3, 1)


def clamp(x, min_val, max_val):
    return max(min_val, min(x, max_val))


def write_color(pixel_color, samples_per_pixel):
    # TODO: reread gamma correction's significance
    scale = 1.0 / samples_per_pixel
    r = math.sqrt(scale * pixel_color.x)
    g = math.sqrt(scale * pixel_color.y)
    b = math.sqrt(scale * pixel_color.z)

    return (
        int(256 * clamp(r, 0.0, 0.999)),
        int(256 * clamp(g, 0.0, 0.999)),
        int(256 * clamp(b, 0.0, 0.999)),
    )
    # "Human eyes aren’t linear. Without gamma correction, the render will look too dark."
    # this didnt make any sense to me
    # i need to read that section again uhh


def reflect(v, n):
    return v - 2 * v.dot(n) * n


def refract(uv, n, etai_over_etat):
    # refracts a unit vector 'uv' through a surface with normal 'n' based on the ratio of refractive indices 'etai_over_etat'
    cos_theta = min(-uv.dot(n), 1.0)

    # perpendicular component of the refracted ray
    r_out_perp = etai_over_etat * (uv + cos_theta * n)
    # parallel component
    r_out_parallel = -math.sqrt(abs(1.0 - r_out_perp.length_squared())) * n

    return r_out_perp + r_out_parallel
