from tinytracer.core.ray import Ray
from tinytracer.core.vec import Vec3


def vec_equal(a: Vec3, b: Vec3, tol=1e-9):
    return abs(a.x - b.x) < tol and abs(a.y - b.y) < tol and abs(a.z - b.z) < tol


def test_vec_addition():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    expected = Vec3(5, 7, 9)
    assert vec_equal(v1 + v2, expected)


def test_vec_scalar_multiplication():
    v = Vec3(1, -2, 3)
    t = 3
    expected = Vec3(3, -6, 9)
    assert vec_equal(v * t, expected)
    assert vec_equal(t * v, expected)


def test_vec_dot_cross():
    v1 = Vec3(1, 0, 0)
    v2 = Vec3(0, 1, 0)
    assert v1.dot(v2) == 0
    cross = v1.cross(v2)
    expected = Vec3(0, 0, 1)
    assert vec_equal(cross, expected)


def test_ray_at():
    origin = Vec3(0, 0, 0)
    direction = Vec3(1, 0, 0)
    ray = Ray(origin, direction)
    t = 5
    expected = origin + direction * t
    assert vec_equal(ray.at(t), expected)
