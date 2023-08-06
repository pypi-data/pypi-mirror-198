from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/debug.scad'}", use_not_include=True)

class debug_vertices(OpenSCADObject):
    def __init__(self, vertices=None, size=None, disabled=None, **kwargs):
       super().__init__("debug_vertices", {"vertices" : vertices, "size" : size, "disabled" : disabled, **kwargs})

class debug_faces(OpenSCADObject):
    def __init__(self, vertices=None, faces=None, size=None, disabled=None, **kwargs):
       super().__init__("debug_faces", {"vertices" : vertices, "faces" : faces, "size" : size, "disabled" : disabled, **kwargs})

class debug_polyhedron(OpenSCADObject):
    def __init__(self, points=None, faces=None, convexity=None, txtsize=None, disabled=None, **kwargs):
       super().__init__("debug_polyhedron", {"points" : points, "faces" : faces, "convexity" : convexity, "txtsize" : txtsize, "disabled" : disabled, **kwargs})

