"""Type hints for the project.

:author: Shay Hill
:created: 2023-03-22
"""
from typing import Annotated, Iterable


# points after rounding to nearest integer
IntPoint = tuple[int, int]

# a line segment is a pair of points
IntSegment = tuple[tuple[int, int], tuple[int, int]]

# minx, miny, maxx, maxy
BBox = tuple[float, float, float, float]

# input points
Vec2 = Annotated[Iterable[float], "2D vector"]
