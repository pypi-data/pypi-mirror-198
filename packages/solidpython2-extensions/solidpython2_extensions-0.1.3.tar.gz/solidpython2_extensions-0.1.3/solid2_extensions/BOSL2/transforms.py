from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/transforms.scad'}", use_not_include=False)

_NO_ARG = OpenSCADConstant('_NO_ARG')
class move(OpenSCADObject):
    def __init__(self, v=None, p=None, **kwargs):
       super().__init__("move", {"v" : v, "p" : p, **kwargs})

class left(OpenSCADObject):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("left", {"x" : x, "p" : p, **kwargs})

class right(OpenSCADObject):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("right", {"x" : x, "p" : p, **kwargs})

class xmove(OpenSCADObject):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("xmove", {"x" : x, "p" : p, **kwargs})

class fwd(OpenSCADObject):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("fwd", {"y" : y, "p" : p, **kwargs})

class back(OpenSCADObject):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("back", {"y" : y, "p" : p, **kwargs})

class ymove(OpenSCADObject):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("ymove", {"y" : y, "p" : p, **kwargs})

class down(OpenSCADObject):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("down", {"z" : z, "p" : p, **kwargs})

class up(OpenSCADObject):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("up", {"z" : z, "p" : p, **kwargs})

class zmove(OpenSCADObject):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("zmove", {"z" : z, "p" : p, **kwargs})

class rot(OpenSCADObject):
    def __init__(self, a=None, v=None, cp=None, _from=None, to=None, reverse=None, **kwargs):
       super().__init__("rot", {"a" : a, "v" : v, "cp" : cp, "_from" : _from, "to" : to, "reverse" : reverse, **kwargs})

class xrot(OpenSCADObject):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("xrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class yrot(OpenSCADObject):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("yrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class zrot(OpenSCADObject):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("zrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class xscale(OpenSCADObject):
    def __init__(self, x=None, p=None, cp=None, **kwargs):
       super().__init__("xscale", {"x" : x, "p" : p, "cp" : cp, **kwargs})

class yscale(OpenSCADObject):
    def __init__(self, y=None, p=None, cp=None, **kwargs):
       super().__init__("yscale", {"y" : y, "p" : p, "cp" : cp, **kwargs})

class zscale(OpenSCADObject):
    def __init__(self, z=None, p=None, cp=None, **kwargs):
       super().__init__("zscale", {"z" : z, "p" : p, "cp" : cp, **kwargs})

class xflip(OpenSCADObject):
    def __init__(self, p=None, x=None, **kwargs):
       super().__init__("xflip", {"p" : p, "x" : x, **kwargs})

class yflip(OpenSCADObject):
    def __init__(self, p=None, y=None, **kwargs):
       super().__init__("yflip", {"p" : p, "y" : y, **kwargs})

class zflip(OpenSCADObject):
    def __init__(self, p=None, z=None, **kwargs):
       super().__init__("zflip", {"p" : p, "z" : z, **kwargs})

class frame_map(OpenSCADObject):
    def __init__(self, x=None, y=None, z=None, p=None, reverse=None, **kwargs):
       super().__init__("frame_map", {"x" : x, "y" : y, "z" : z, "p" : p, "reverse" : reverse, **kwargs})

class skew(OpenSCADObject):
    def __init__(self, p=None, sxy=None, sxz=None, syx=None, syz=None, szx=None, szy=None, **kwargs):
       super().__init__("skew", {"p" : p, "sxy" : sxy, "sxz" : sxz, "syx" : syx, "syz" : syz, "szx" : szx, "szy" : szy, **kwargs})

class move(OpenSCADObject):
    def __init__(self, v=None, p=None, **kwargs):
       super().__init__("move", {"v" : v, "p" : p, **kwargs})

class translate(OpenSCADObject):
    def __init__(self, v=None, p=None, **kwargs):
       super().__init__("translate", {"v" : v, "p" : p, **kwargs})

class left(OpenSCADObject):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("left", {"x" : x, "p" : p, **kwargs})

class right(OpenSCADObject):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("right", {"x" : x, "p" : p, **kwargs})

class xmove(OpenSCADObject):
    def __init__(self, x=None, p=None, **kwargs):
       super().__init__("xmove", {"x" : x, "p" : p, **kwargs})

class fwd(OpenSCADObject):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("fwd", {"y" : y, "p" : p, **kwargs})

class back(OpenSCADObject):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("back", {"y" : y, "p" : p, **kwargs})

class ymove(OpenSCADObject):
    def __init__(self, y=None, p=None, **kwargs):
       super().__init__("ymove", {"y" : y, "p" : p, **kwargs})

class down(OpenSCADObject):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("down", {"z" : z, "p" : p, **kwargs})

class up(OpenSCADObject):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("up", {"z" : z, "p" : p, **kwargs})

class zmove(OpenSCADObject):
    def __init__(self, z=None, p=None, **kwargs):
       super().__init__("zmove", {"z" : z, "p" : p, **kwargs})

class rot(OpenSCADObject):
    def __init__(self, a=None, v=None, cp=None, _from=None, to=None, reverse=None, p=None, _m=None, **kwargs):
       super().__init__("rot", {"a" : a, "v" : v, "cp" : cp, "_from" : _from, "to" : to, "reverse" : reverse, "p" : p, "_m" : _m, **kwargs})

class xrot(OpenSCADObject):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("xrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class yrot(OpenSCADObject):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("yrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class zrot(OpenSCADObject):
    def __init__(self, a=None, p=None, cp=None, **kwargs):
       super().__init__("zrot", {"a" : a, "p" : p, "cp" : cp, **kwargs})

class scale(OpenSCADObject):
    def __init__(self, v=None, p=None, cp=None, **kwargs):
       super().__init__("scale", {"v" : v, "p" : p, "cp" : cp, **kwargs})

class xscale(OpenSCADObject):
    def __init__(self, x=None, p=None, cp=None, **kwargs):
       super().__init__("xscale", {"x" : x, "p" : p, "cp" : cp, **kwargs})

class yscale(OpenSCADObject):
    def __init__(self, y=None, p=None, cp=None, **kwargs):
       super().__init__("yscale", {"y" : y, "p" : p, "cp" : cp, **kwargs})

class zscale(OpenSCADObject):
    def __init__(self, z=None, p=None, cp=None, **kwargs):
       super().__init__("zscale", {"z" : z, "p" : p, "cp" : cp, **kwargs})

class mirror(OpenSCADObject):
    def __init__(self, v=None, p=None, **kwargs):
       super().__init__("mirror", {"v" : v, "p" : p, **kwargs})

class xflip(OpenSCADObject):
    def __init__(self, p=None, x=None, **kwargs):
       super().__init__("xflip", {"p" : p, "x" : x, **kwargs})

class yflip(OpenSCADObject):
    def __init__(self, p=None, y=None, **kwargs):
       super().__init__("yflip", {"p" : p, "y" : y, **kwargs})

class zflip(OpenSCADObject):
    def __init__(self, p=None, z=None, **kwargs):
       super().__init__("zflip", {"p" : p, "z" : z, **kwargs})

class frame_map(OpenSCADObject):
    def __init__(self, x=None, y=None, z=None, p=None, reverse=None, **kwargs):
       super().__init__("frame_map", {"x" : x, "y" : y, "z" : z, "p" : p, "reverse" : reverse, **kwargs})

class skew(OpenSCADObject):
    def __init__(self, p=None, sxy=None, sxz=None, syx=None, syz=None, szx=None, szy=None, **kwargs):
       super().__init__("skew", {"p" : p, "sxy" : sxy, "sxz" : sxz, "syx" : syx, "syz" : syz, "szx" : szx, "szy" : szy, **kwargs})

class is_2d_transform(OpenSCADObject):
    def __init__(self, t=None, **kwargs):
       super().__init__("is_2d_transform", {"t" : t, **kwargs})

class apply(OpenSCADObject):
    def __init__(self, transform=None, points=None, **kwargs):
       super().__init__("apply", {"transform" : transform, "points" : points, **kwargs})

class _apply(OpenSCADObject):
    def __init__(self, transform=None, points=None, **kwargs):
       super().__init__("_apply", {"transform" : transform, "points" : points, **kwargs})

