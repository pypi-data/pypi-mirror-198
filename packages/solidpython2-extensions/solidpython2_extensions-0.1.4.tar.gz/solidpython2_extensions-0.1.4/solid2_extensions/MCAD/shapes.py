from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/shapes.scad'}", use_not_include=False)

class echo_deprecated_shapes_library(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("echo_deprecated_shapes_library", {**kwargs})

class box(OpenSCADObject):
    def __init__(self, width=None, height=None, depth=None, **kwargs):
       super().__init__("box", {"width" : width, "height" : height, "depth" : depth, **kwargs})

class roundedBox(OpenSCADObject):
    def __init__(self, width=None, height=None, depth=None, radius=None, **kwargs):
       super().__init__("roundedBox", {"width" : width, "height" : height, "depth" : depth, "radius" : radius, **kwargs})

class cone(OpenSCADObject):
    def __init__(self, height=None, radius=None, center=None, **kwargs):
       super().__init__("cone", {"height" : height, "radius" : radius, "center" : center, **kwargs})

class ellipticalCylinder(OpenSCADObject):
    def __init__(self, w=None, h=None, height=None, center=None, **kwargs):
       super().__init__("ellipticalCylinder", {"w" : w, "h" : h, "height" : height, "center" : center, **kwargs})

class ellipsoid(OpenSCADObject):
    def __init__(self, w=None, h=None, center=None, **kwargs):
       super().__init__("ellipsoid", {"w" : w, "h" : h, "center" : center, **kwargs})

class tube(OpenSCADObject):
    def __init__(self, height=None, radius=None, wall=None, center=None, **kwargs):
       super().__init__("tube", {"height" : height, "radius" : radius, "wall" : wall, "center" : center, **kwargs})

class tube2(OpenSCADObject):
    def __init__(self, height=None, ID=None, OD=None, center=None, **kwargs):
       super().__init__("tube2", {"height" : height, "ID" : ID, "OD" : OD, "center" : center, **kwargs})

class ovalTube(OpenSCADObject):
    def __init__(self, height=None, rx=None, ry=None, wall=None, center=None, **kwargs):
       super().__init__("ovalTube", {"height" : height, "rx" : rx, "ry" : ry, "wall" : wall, "center" : center, **kwargs})

class hexagon(OpenSCADObject):
    def __init__(self, size=None, height=None, **kwargs):
       super().__init__("hexagon", {"size" : size, "height" : height, **kwargs})

class octagon(OpenSCADObject):
    def __init__(self, size=None, height=None, **kwargs):
       super().__init__("octagon", {"size" : size, "height" : height, **kwargs})

class dodecagon(OpenSCADObject):
    def __init__(self, size=None, height=None, **kwargs):
       super().__init__("dodecagon", {"size" : size, "height" : height, **kwargs})

class hexagram(OpenSCADObject):
    def __init__(self, size=None, height=None, **kwargs):
       super().__init__("hexagram", {"size" : size, "height" : height, **kwargs})

class rightTriangle(OpenSCADObject):
    def __init__(self, adjacent=None, opposite=None, height=None, **kwargs):
       super().__init__("rightTriangle", {"adjacent" : adjacent, "opposite" : opposite, "height" : height, **kwargs})

class equiTriangle(OpenSCADObject):
    def __init__(self, side=None, height=None, **kwargs):
       super().__init__("equiTriangle", {"side" : side, "height" : height, **kwargs})

class _12ptStar(OpenSCADObject):
    def __init__(self, size=None, height=None, **kwargs):
       super().__init__("_12ptStar", {"size" : size, "height" : height, **kwargs})

class dislocateBox(OpenSCADObject):
    def __init__(self, w=None, h=None, d=None, **kwargs):
       super().__init__("dislocateBox", {"w" : w, "h" : h, "d" : d, **kwargs})

