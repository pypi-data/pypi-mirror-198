from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/partitions.scad'}", use_not_include=False)

class half_of(OpenSCADObject):
    def __init__(self, v=None, cp=None, s=None, planar=None, **kwargs):
       super().__init__("half_of", {"v" : v, "cp" : cp, "s" : s, "planar" : planar, **kwargs})

class left_half(OpenSCADObject):
    def __init__(self, s=None, x=None, planar=None, **kwargs):
       super().__init__("left_half", {"s" : s, "x" : x, "planar" : planar, **kwargs})

class right_half(OpenSCADObject):
    def __init__(self, s=None, x=None, planar=None, **kwargs):
       super().__init__("right_half", {"s" : s, "x" : x, "planar" : planar, **kwargs})

class front_half(OpenSCADObject):
    def __init__(self, s=None, y=None, planar=None, **kwargs):
       super().__init__("front_half", {"s" : s, "y" : y, "planar" : planar, **kwargs})

class back_half(OpenSCADObject):
    def __init__(self, s=None, y=None, planar=None, **kwargs):
       super().__init__("back_half", {"s" : s, "y" : y, "planar" : planar, **kwargs})

class bottom_half(OpenSCADObject):
    def __init__(self, s=None, z=None, **kwargs):
       super().__init__("bottom_half", {"s" : s, "z" : z, **kwargs})

class top_half(OpenSCADObject):
    def __init__(self, s=None, z=None, **kwargs):
       super().__init__("top_half", {"s" : s, "z" : z, **kwargs})

class partition_mask(OpenSCADObject):
    def __init__(self, l=None, w=None, h=None, cutsize=None, cutpath=None, gap=None, inverse=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("partition_mask", {"l" : l, "w" : w, "h" : h, "cutsize" : cutsize, "cutpath" : cutpath, "gap" : gap, "inverse" : inverse, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class partition_cut_mask(OpenSCADObject):
    def __init__(self, l=None, h=None, cutsize=None, cutpath=None, gap=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("partition_cut_mask", {"l" : l, "h" : h, "cutsize" : cutsize, "cutpath" : cutpath, "gap" : gap, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class partition(OpenSCADObject):
    def __init__(self, size=None, spread=None, cutsize=None, cutpath=None, gap=None, spin=None, **kwargs):
       super().__init__("partition", {"size" : size, "spread" : spread, "cutsize" : cutsize, "cutpath" : cutpath, "gap" : gap, "spin" : spin, **kwargs})

class half_of(OpenSCADObject):
    def __init__(self, p=None, v=None, cp=None, **kwargs):
       super().__init__("half_of", {"p" : p, "v" : v, "cp" : cp, **kwargs})

class left_half(OpenSCADObject):
    def __init__(self, p=None, x=None, **kwargs):
       super().__init__("left_half", {"p" : p, "x" : x, **kwargs})

class right_half(OpenSCADObject):
    def __init__(self, p=None, x=None, **kwargs):
       super().__init__("right_half", {"p" : p, "x" : x, **kwargs})

class front_half(OpenSCADObject):
    def __init__(self, p=None, y=None, **kwargs):
       super().__init__("front_half", {"p" : p, "y" : y, **kwargs})

class back_half(OpenSCADObject):
    def __init__(self, p=None, y=None, **kwargs):
       super().__init__("back_half", {"p" : p, "y" : y, **kwargs})

class bottom_half(OpenSCADObject):
    def __init__(self, p=None, z=None, **kwargs):
       super().__init__("bottom_half", {"p" : p, "z" : z, **kwargs})

class top_half(OpenSCADObject):
    def __init__(self, p=None, z=None, **kwargs):
       super().__init__("top_half", {"p" : p, "z" : z, **kwargs})

class _partition_subpath(OpenSCADObject):
    def __init__(self, type=None, **kwargs):
       super().__init__("_partition_subpath", {"type" : type, **kwargs})

class _partition_cutpath(OpenSCADObject):
    def __init__(self, l=None, h=None, cutsize=None, cutpath=None, gap=None, **kwargs):
       super().__init__("_partition_cutpath", {"l" : l, "h" : h, "cutsize" : cutsize, "cutpath" : cutpath, "gap" : gap, **kwargs})

