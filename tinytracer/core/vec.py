"""Vector utilities and the :class:`Vec3` 3D vector type.

This module provides a lightweight 3D vector class used by the renderer and
some utility functions for generating random directions. The :class:`Vec3`
object is used both for geometry and as the ``Color`` alias for RGB values.
"""

from random import uniform
from math import sqrt


class Vec3:
    """A 3D vector for geometry and color computations.

    Represents a vector with float components (``x``, ``y``, ``z``) and
    provides basic vector operations used by the renderer:
    addition, subtraction, scalar and component-wise multiplication,
    dot/cross products, length/normalization, and component-wise clamping.

    Attributes:
        x (float): X component.
        y (float): Y component.
        z (float): Z component.
    """

    def __init__(self, x=0, y=0, z=0):
        """Create a new :class:`Vec3`.

        Args:
            x (float, optional): X component. Defaults to 0.
            y (float, optional): Y component. Defaults to 0.
            z (float, optional): Z component. Defaults to 0.
        """
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        """Return the vector sum ``self + other``.

        Args:
            other (Vec3): The vector to add.

        Returns:
            Vec3: Sum of the vectors.
        """
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Return the vector difference ``self - other``.

        Args:
            other (Vec3): The vector to subtract.

        Returns:
            Vec3: Difference of the vectors.
        """
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, t):
        """Multiply by a scalar or component-wise by another :class:`Vec3`.

        Args:
            t (Union[Vec3, float]): A vector for Hadamard product or a scalar
                for uniform scaling.

        Returns:
            Vec3: Result of multiplication.
        """
        if isinstance(t, Vec3):
            return Vec3(self.x * t.x, self.y * t.y, self.z * t.z)
        return Vec3(self.x * t, self.y * t, self.z * t)

    def __rmul__(self, t):
        """Support right-hand scalar multiplication (``scalar * Vec3``)."""
        return self * t

    def __truediv__(self, t):
        """Return ``self`` divided by scalar ``t``.

        Args:
            t (float): Divisor.

        Returns:
            Vec3: Scaled vector (``self * (1.0 / t)``).
        """
        return self * (1.0 / t)

    def __neg__(self):
        """Return the negation of this vector (``-self``)."""
        return Vec3(-self.x, -self.y, -self.z)

    def dot(self, other):
        """Compute the dot product with ``other``.

        Args:
            other (Vec3): Other vector.

        Returns:
            float: Dot product value.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length_squared(self):
        """Return the squared length (magnitude) of the vector."""
        return self.dot(self)

    def length(self):
        """Return the Euclidean length (magnitude) of the vector."""
        return sqrt(self.length_squared())

    def unit_vector(self):
        """Return a unit (normalized) vector in the same direction as ``self``.

        Returns:
            Vec3: Unit vector (``self / length``).
        """
        return self / self.length()

    def cross(self, other):
        """Compute the cross product with ``other``.

        Args:
            other (Vec3): Other vector.

        Returns:
            Vec3: Cross product vector.
        """
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def near_zero(self):
        """Return ``True`` if the vector is close to zero in all components.

        This tests whether each component is smaller than a small threshold
        (``1e-8``) to account for floating-point imprecision.

        Returns:
            bool: ``True`` if the vector is approximately zero.
        """
        s = 1e-8
        return abs(self.x) < s and abs(self.y) < s and abs(self.z) < s

    def clamp(self, min_val, max_val):
        """Clamp each component to the ``[min_val, max_val]`` range.

        Args:
            min_val (float): Minimum allowed component value.
            max_val (float): Maximum allowed component value.

        Returns:
            Vec3: A new vector with clamped components.
        """
        return Vec3(
            min(max(self.x, min_val), max_val),
            min(max(self.y, min_val), max_val),
            min(max(self.z, min_val), max_val),
        )


def random_unit_vector():
    """Return a random unit vector sampled uniformly inside the unit sphere.

    Uses rejection sampling to pick points inside the unit sphere and returns
    the normalized direction.
    """
    while True:
        p = Vec3(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))
        if p.length_squared() < 1:
            return p.unit_vector()


def random_in_hemisphere(normal):
    """Return a random unit vector in the hemisphere defined by ``normal``.

    Args:
        normal (Vec3): The hemisphere's outward normal vector.

    Returns:
        Vec3: Random unit vector in the same hemisphere as ``normal``.
    """
    in_unit_sphere = random_unit_vector()
    if in_unit_sphere.dot(normal) > 0.0:
        return in_unit_sphere
    else:
        # i dont need to keep this right now,
        # might need for mirrors and all
        return -in_unit_sphere


Color = Vec3
