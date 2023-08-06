from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/triangles.scad'}", use_not_include=False)

class triangle(OpenSCADObject):
    def __init__(self, o_len=None, a_len=None, depth=None, center=None, **kwargs):
       super().__init__("triangle", {"o_len" : o_len, "a_len" : a_len, "depth" : depth, "center" : center, **kwargs})

class a_triangle(OpenSCADObject):
    def __init__(self, tan_angle=None, a_len=None, depth=None, center=None, **kwargs):
       super().__init__("a_triangle", {"tan_angle" : tan_angle, "a_len" : a_len, "depth" : depth, "center" : center, **kwargs})

class test_triangle(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_triangle", {**kwargs})

class test_a_triangle(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_a_triangle", {**kwargs})

class test_triangles(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_triangles", {**kwargs})

