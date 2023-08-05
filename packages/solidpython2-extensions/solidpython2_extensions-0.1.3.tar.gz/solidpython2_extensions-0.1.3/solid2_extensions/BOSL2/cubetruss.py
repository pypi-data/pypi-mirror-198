from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/cubetruss.scad'}", use_not_include=False)

_cubetruss_size = OpenSCADConstant('_cubetruss_size')
_cubetruss_strut_size = OpenSCADConstant('_cubetruss_strut_size')
_cubetruss_bracing = OpenSCADConstant('_cubetruss_bracing')
_cubetruss_clip_thickness = OpenSCADConstant('_cubetruss_clip_thickness')
class cubetruss_segment(OpenSCADObject):
    def __init__(self, size=None, strut=None, bracing=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cubetruss_segment", {"size" : size, "strut" : strut, "bracing" : bracing, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cubetruss_support(OpenSCADObject):
    def __init__(self, size=None, strut=None, extents=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cubetruss_support", {"size" : size, "strut" : strut, "extents" : extents, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cubetruss_clip(OpenSCADObject):
    def __init__(self, extents=None, size=None, strut=None, clipthick=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cubetruss_clip", {"extents" : extents, "size" : size, "strut" : strut, "clipthick" : clipthick, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cubetruss_foot(OpenSCADObject):
    def __init__(self, w=None, size=None, strut=None, clipthick=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cubetruss_foot", {"w" : w, "size" : size, "strut" : strut, "clipthick" : clipthick, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cubetruss_joiner(OpenSCADObject):
    def __init__(self, w=None, vert=None, size=None, strut=None, clipthick=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cubetruss_joiner", {"w" : w, "vert" : vert, "size" : size, "strut" : strut, "clipthick" : clipthick, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cubetruss_uclip(OpenSCADObject):
    def __init__(self, dual=None, size=None, strut=None, clipthick=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cubetruss_uclip", {"dual" : dual, "size" : size, "strut" : strut, "clipthick" : clipthick, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cubetruss(OpenSCADObject):
    def __init__(self, extents=None, clips=None, bracing=None, size=None, strut=None, clipthick=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cubetruss", {"extents" : extents, "clips" : clips, "bracing" : bracing, "size" : size, "strut" : strut, "clipthick" : clipthick, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cubetruss_corner(OpenSCADObject):
    def __init__(self, h=None, extents=None, bracing=None, size=None, strut=None, clipthick=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cubetruss_corner", {"h" : h, "extents" : extents, "bracing" : bracing, "size" : size, "strut" : strut, "clipthick" : clipthick, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cubetruss_dist(OpenSCADObject):
    def __init__(self, cubes=None, gaps=None, size=None, strut=None, **kwargs):
       super().__init__("cubetruss_dist", {"cubes" : cubes, "gaps" : gaps, "size" : size, "strut" : strut, **kwargs})

