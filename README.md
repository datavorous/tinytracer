# TinyTracer

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

<img src="https://raw.githubusercontent.com/datavorous/datavorous/refs/heads/main/gsbuxq.png" width="400">
<img src="output/demos/demo1.png" width="400">
<img src="output/demos/demo3.png" width="400">
<img src="output/demos/demo2.png" width="400">

## Recent Changes

1. added multiprocessing to speed up rendering
2. added dielectric material type (for glass, water, etc.)
3. implemented caching for minor speed-ups

## Todo 

- [ ] BVH implementation
- [ ] `.obj` model parser (atleast render Utah teapot)
- [ ] possible C++ rewrite?

## Foreword

A path tracer is a type of rendering program or algorithm that generates images by simulating the paths of light rays as they bounce around a scene, capturing realistic lighting, shadows, reflections, and refractions.

Sphere and Quadrilateral have been implemented till now, and four material types: Lambertian Diffuse, Metal, Dielectric and LightEmissive Material.

> [!NOTE]
> Some of the demos are so noisy because I had kept `sampling = 30`, to reduce the rendering time.

Formatted with `black`.


### Installation

Have `uv` installed beforehand.

```
git clone https://github.com/datavorous/tinytracer.git
cd tinytracer
uv run main.py
```

The image generated will be of `.ppm` format.

## References

> [!NOTE]
> Read [this](https://www.reddit.com/r/GraphicsProgramming/comments/1ej5ffo/raytracing_in_one_weekend_not_understanding_the/) if you are having some trouble with understanding how the `viewport` works.

Check out [explained.md](explained.md) for some rudimentary explanation from my side.

Book that I followed: *[Ray Tracing in One Weekend](https://raytracing.github.io/)* (Part 1 and Part 2)

