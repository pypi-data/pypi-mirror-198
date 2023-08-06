from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/triangulation.scad'}", use_not_include=True)

class face_normal(OpenSCADObject):
    def __init__(self, points=None, face=None, **kwargs):
       super().__init__("face_normal", {"points" : points, "face" : face, **kwargs})

class find_convex_vertex(OpenSCADObject):
    def __init__(self, points=None, face=None, facenorm=None, i=None, **kwargs):
       super().__init__("find_convex_vertex", {"points" : points, "face" : face, "facenorm" : facenorm, "i" : i, **kwargs})

class point_in_ear(OpenSCADObject):
    def __init__(self, points=None, face=None, tests=None, i=None, **kwargs):
       super().__init__("point_in_ear", {"points" : points, "face" : face, "tests" : tests, "i" : i, **kwargs})

class _check_point_in_ear(OpenSCADObject):
    def __init__(self, point=None, tests=None, **kwargs):
       super().__init__("_check_point_in_ear", {"point" : point, "tests" : tests, **kwargs})

class normalize_vertex_perimeter(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("normalize_vertex_perimeter", {"v" : v, **kwargs})

class is_only_noncolinear_vertex(OpenSCADObject):
    def __init__(self, points=None, facelist=None, vertex=None, **kwargs):
       super().__init__("is_only_noncolinear_vertex", {"points" : points, "facelist" : facelist, "vertex" : vertex, **kwargs})

class triangulate_face(OpenSCADObject):
    def __init__(self, points=None, face=None, **kwargs):
       super().__init__("triangulate_face", {"points" : points, "face" : face, **kwargs})

class triangulate_faces(OpenSCADObject):
    def __init__(self, points=None, faces=None, **kwargs):
       super().__init__("triangulate_faces", {"points" : points, "faces" : faces, **kwargs})

