from core.camera import Camera
from core.vec import Vec3, Color
from core.hits import HittableList
from core.utils import ray_color, write_color

# from core.ray import Ray
from shapes.sphere import Sphere

# from shapes.quad import Quad
from shapes.material import Lambertian, EmissiveMaterial, Metal, Dielectric

import random
import multiprocessing
import time


def render_pixel(args):
    i, j, image_width, image_height, samples_per_pixel, camera, world, max_depth = args
    pixel_color = Color(0, 0, 0)

    for _ in range(samples_per_pixel):
        u = (i + random.random()) / (image_width - 1)
        v = (j + random.random()) / (image_height - 1)
        ray = camera.get_ray(u, v)
        pixel_color = pixel_color + ray_color(ray, world, max_depth)

    r, g, b = write_color(pixel_color, samples_per_pixel)
    return (i, j, r, g, b)


def main():
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 5
    max_depth = 5
    world = HittableList()
    pixels = []

    world.add(Sphere(Vec3(0, -100.5, 0), 100, Lambertian(Color(0.27, 0.28, 0.26))))
    world.add(Sphere(Vec3(0, 0, -2), 0.7, Dielectric(1.5)))
    world.add(Sphere(Vec3(0, 0, -2), -0.6, Dielectric(1.5)))
    world.add(Sphere(Vec3(1.5, 0, -1.5), 0.5, Lambertian(Color(1, 0.45, 0.50))))
    world.add(Sphere(Vec3(0.5, 0, -1.7), 0.4, Lambertian(Color(0.45, 1, 0.45))))
    world.add(Sphere(Vec3(-0.75, -0.2, -0.8), 0.4, Dielectric(1.5)))
    world.add(Sphere(Vec3(-0.75, -0.2, -0.8), -0.3, Dielectric(1.5)))
    world.add(Sphere(Vec3(0, 0.5, -3.5), 0.6, Lambertian(Color(0.55, 0.65, 1))))
    world.add(Sphere(Vec3(-2, 2.5, -3), 0.8, EmissiveMaterial(Color(1, 0.9, 0.7), 4)))
    world.add(Sphere(Vec3(3, 1, -1), 0.5, EmissiveMaterial(Color(0.7, 0.85, 1), 2.5)))

    camera = Camera(
        Vec3(-1.2, 1.4, 1.6),
        Vec3(-0.1, 0.1, -1.5),
        Vec3(0, 1, 0),
        40,
        aspect_ratio,
    )

    print(
        f"Starting render: {image_width}x{image_height}, {samples_per_pixel} samples per pixel"
    )

    tasks = [
        (i, j, image_width, image_height, samples_per_pixel, camera, world, max_depth)
        for j in range(image_height - 1, -1, -1)
        for i in range(image_width)
    ]
    total_pixels = len(tasks)
    print(f"Total pixels: {total_pixels}")

    start_time = time.time()

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = []
        for idx, res in enumerate(
            pool.imap_unordered(render_pixel, tasks, chunksize=1200)
        ):
            results.append(res)
            if idx % 1000 == 0:
                elapsed = time.time() - start_time
                percent = (idx + 1) / total_pixels
                eta = (elapsed / percent - elapsed) if percent > 0 else 0

                print(
                    f"{percent * 100:.2f}% | Elapsed: {elapsed:.1f}s | ETA: {eta:.1f}s",
                    end="\r",
                    flush=True,
                )
        print()

    framebuffer = [[None] * image_width for _ in range(image_height)]

    for i, j, r, g, b in results:
        framebuffer[image_height - 1 - j][i] = (r, g, b)

    with open("tinytracer/output/image.ppm", "wb") as f:
        f.write(f"P6\n{image_width} {image_height}\n255\n".encode())
        for row in framebuffer:
            for r, g, b in row:
                f.write(bytes([r, g, b]))

    print("Saved as output/image.ppm")


start = time.time()
main()
print(f"Render time: {time.time() - start:.2f}s")


'''
    # the main work starts exactly here:
    for j in range(image_height - 1, -1, -1):
        # we go from top to bottom
        # scan each horizontal row of pixels
        # and take actions accordingly

        for i in range(image_width):
            pixel_color = Color(0, 0, 0)
            # everything is assigned a base color
            # then we shoot multiple rays from our camera
            # to perform anti aliasing

            for _ in range(samples_per_pixel):
                # u, v are discrete increments for: left-right and top-bottom
                u = (i + random.random()) / (image_width - 1)
                v = (j + random.random()) / (image_height - 1)
                # shoot some rays

                # returns a ray object, ray object has the origin, and a P(t) ray equation
                ray = camera.get_ray(u, v)
                # and we try to change the color

                """
                so important:
                ray color has a HitList in it
                first we check if there we have exceeded the depth limit or not
                depth limit here refers to the number of times the ray can bounce off from a surface
                the 'world' param (a HittableList has already provided the entities to check collisions with)

                """
                pixel_color = pixel_color + ray_color(ray, world, max_depth)
                # so after lots of magic done per ray, withing the ray_color() function
                # , we get the color we need for a given pixel
                # the ray color is techincally the heart of this path tracer
            done += 1
            if done % 1000 == 0:
                percent = done / total_pixels * 100
                print(f"{percent:.2f}% done", end="\r", flush=True)

            rgb = write_color(pixel_color, samples_per_pixel)
            pixels.append(rgb)

    with open("output/image.ppm", "wb") as f:
        f.write(f"P6\n{image_width} {image_height}\n255\n".encode())
        for r, g, b in pixels:
            f.write(bytes([r, g, b]))
    print("Saved as 'output/image.ppm'")
'''
