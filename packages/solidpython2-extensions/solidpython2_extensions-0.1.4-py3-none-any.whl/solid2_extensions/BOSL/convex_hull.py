from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/convex_hull.scad'}", use_not_include=True)

class convex_hull(OpenSCADObject):
    def __init__(self, points=None, **kwargs):
       super().__init__("convex_hull", {"points" : points, **kwargs})

class convex_hull2d(OpenSCADObject):
    def __init__(self, points=None, **kwargs):
       super().__init__("convex_hull2d", {"points" : points, **kwargs})

class _convex_hull_iterative_2d(OpenSCADObject):
    def __init__(self, points=None, polygon=None, remaining=None, _i=None, **kwargs):
       super().__init__("_convex_hull_iterative_2d", {"points" : points, "polygon" : polygon, "remaining" : remaining, "_i" : _i, **kwargs})

class _find_first_noncollinear(OpenSCADObject):
    def __init__(self, line=None, points=None, i=None, **kwargs):
       super().__init__("_find_first_noncollinear", {"line" : line, "points" : points, "i" : i, **kwargs})

class _find_conflicting_segments(OpenSCADObject):
    def __init__(self, points=None, polygon=None, point=None, **kwargs):
       super().__init__("_find_conflicting_segments", {"points" : points, "polygon" : polygon, "point" : point, **kwargs})

class _remove_conflicts_and_insert_point(OpenSCADObject):
    def __init__(self, polygon=None, conflicts=None, point=None, **kwargs):
       super().__init__("_remove_conflicts_and_insert_point", {"polygon" : polygon, "conflicts" : conflicts, "point" : point, **kwargs})

class convex_hull3d(OpenSCADObject):
    def __init__(self, points=None, **kwargs):
       super().__init__("convex_hull3d", {"points" : points, **kwargs})

class _convex_hull_iterative(OpenSCADObject):
    def __init__(self, points=None, triangles=None, planes=None, remaining=None, _i=None, **kwargs):
       super().__init__("_convex_hull_iterative", {"points" : points, "triangles" : triangles, "planes" : planes, "remaining" : remaining, "_i" : _i, **kwargs})

class _convex_hull_collinear(OpenSCADObject):
    def __init__(self, points=None, **kwargs):
       super().__init__("_convex_hull_collinear", {"points" : points, **kwargs})

class _remove_internal_edges(OpenSCADObject):
    def __init__(self, halfedges=None, **kwargs):
       super().__init__("_remove_internal_edges", {"halfedges" : halfedges, **kwargs})

class _find_conflicts(OpenSCADObject):
    def __init__(self, point=None, planes=None, **kwargs):
       super().__init__("_find_conflicts", {"point" : point, "planes" : planes, **kwargs})

class _find_first_noncoplanar(OpenSCADObject):
    def __init__(self, plane=None, points=None, i=None, **kwargs):
       super().__init__("_find_first_noncoplanar", {"plane" : plane, "points" : points, "i" : i, **kwargs})

