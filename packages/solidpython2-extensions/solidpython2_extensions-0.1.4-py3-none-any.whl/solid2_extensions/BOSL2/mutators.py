from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/mutators.scad'}", use_not_include=False)

class bounding_box(OpenSCADObject):
    def __init__(self, excess=None, planar=None, **kwargs):
       super().__init__("bounding_box", {"excess" : excess, "planar" : planar, **kwargs})

class chain_hull(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("chain_hull", {**kwargs})

class path_extrude2d(OpenSCADObject):
    def __init__(self, path=None, caps=None, closed=None, s=None, convexity=None, **kwargs):
       super().__init__("path_extrude2d", {"path" : path, "caps" : caps, "closed" : closed, "s" : s, "convexity" : convexity, **kwargs})

class cylindrical_extrude(OpenSCADObject):
    def __init__(self, ir=None, _or=None, od=None, id=None, size=None, convexity=None, spin=None, orient=None, **kwargs):
       super().__init__("cylindrical_extrude", {"ir" : ir, "_or" : _or, "od" : od, "id" : id, "size" : size, "convexity" : convexity, "spin" : spin, "orient" : orient, **kwargs})

class extrude_from_to(OpenSCADObject):
    def __init__(self, pt1=None, pt2=None, convexity=None, twist=None, scale=None, slices=None, **kwargs):
       super().__init__("extrude_from_to", {"pt1" : pt1, "pt2" : pt2, "convexity" : convexity, "twist" : twist, "scale" : scale, "slices" : slices, **kwargs})

class path_extrude(OpenSCADObject):
    def __init__(self, path=None, convexity=None, clipsize=None, **kwargs):
       super().__init__("path_extrude", {"path" : path, "convexity" : convexity, "clipsize" : clipsize, **kwargs})

class minkowski_difference(OpenSCADObject):
    def __init__(self, planar=None, **kwargs):
       super().__init__("minkowski_difference", {"planar" : planar, **kwargs})

class offset3d(OpenSCADObject):
    def __init__(self, r=None, size=None, convexity=None, **kwargs):
       super().__init__("offset3d", {"r" : r, "size" : size, "convexity" : convexity, **kwargs})

class round3d(OpenSCADObject):
    def __init__(self, r=None, _or=None, ir=None, size=None, **kwargs):
       super().__init__("round3d", {"r" : r, "_or" : _or, "ir" : ir, "size" : size, **kwargs})

