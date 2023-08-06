from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/transforms.scad'}", use_not_include=True)

class move(OpenSCADObject):
    def __init__(self, a=None, x=None, y=None, z=None, **kwargs):
       super().__init__("move", {"a" : a, "x" : x, "y" : y, "z" : z, **kwargs})

class xmove(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("xmove", {"x" : x, **kwargs})

class ymove(OpenSCADObject):
    def __init__(self, y=None, **kwargs):
       super().__init__("ymove", {"y" : y, **kwargs})

class zmove(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("zmove", {"z" : z, **kwargs})

class left(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("left", {"x" : x, **kwargs})

class right(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("right", {"x" : x, **kwargs})

class forward(OpenSCADObject):
    def __init__(self, y=None, **kwargs):
       super().__init__("forward", {"y" : y, **kwargs})

class fwd(OpenSCADObject):
    def __init__(self, y=None, **kwargs):
       super().__init__("fwd", {"y" : y, **kwargs})

class back(OpenSCADObject):
    def __init__(self, y=None, **kwargs):
       super().__init__("back", {"y" : y, **kwargs})

class down(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("down", {"z" : z, **kwargs})

class up(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("up", {"z" : z, **kwargs})

class rot(OpenSCADObject):
    def __init__(self, a=None, v=None, cp=None, _from=None, to=None, reverse=None, **kwargs):
       super().__init__("rot", {"a" : a, "v" : v, "cp" : cp, "_from" : _from, "to" : to, "reverse" : reverse, **kwargs})

class xrot(OpenSCADObject):
    def __init__(self, a=None, cp=None, **kwargs):
       super().__init__("xrot", {"a" : a, "cp" : cp, **kwargs})

class yrot(OpenSCADObject):
    def __init__(self, a=None, cp=None, **kwargs):
       super().__init__("yrot", {"a" : a, "cp" : cp, **kwargs})

class zrot(OpenSCADObject):
    def __init__(self, a=None, cp=None, **kwargs):
       super().__init__("zrot", {"a" : a, "cp" : cp, **kwargs})

class xscale(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("xscale", {"x" : x, **kwargs})

class yscale(OpenSCADObject):
    def __init__(self, y=None, **kwargs):
       super().__init__("yscale", {"y" : y, **kwargs})

class zscale(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("zscale", {"z" : z, **kwargs})

class xflip(OpenSCADObject):
    def __init__(self, cp=None, **kwargs):
       super().__init__("xflip", {"cp" : cp, **kwargs})

class yflip(OpenSCADObject):
    def __init__(self, cp=None, **kwargs):
       super().__init__("yflip", {"cp" : cp, **kwargs})

class zflip(OpenSCADObject):
    def __init__(self, cp=None, **kwargs):
       super().__init__("zflip", {"cp" : cp, **kwargs})

class skew_xy(OpenSCADObject):
    def __init__(self, xa=None, ya=None, planar=None, **kwargs):
       super().__init__("skew_xy", {"xa" : xa, "ya" : ya, "planar" : planar, **kwargs})

class zskew(OpenSCADObject):
    def __init__(self, xa=None, ya=None, planar=None, **kwargs):
       super().__init__("zskew", {"xa" : xa, "ya" : ya, "planar" : planar, **kwargs})

class skew_yz(OpenSCADObject):
    def __init__(self, ya=None, za=None, **kwargs):
       super().__init__("skew_yz", {"ya" : ya, "za" : za, **kwargs})

class xskew(OpenSCADObject):
    def __init__(self, ya=None, za=None, **kwargs):
       super().__init__("xskew", {"ya" : ya, "za" : za, **kwargs})

class skew_xz(OpenSCADObject):
    def __init__(self, xa=None, za=None, **kwargs):
       super().__init__("skew_xz", {"xa" : xa, "za" : za, **kwargs})

class yskew(OpenSCADObject):
    def __init__(self, xa=None, za=None, **kwargs):
       super().__init__("yskew", {"xa" : xa, "za" : za, **kwargs})

class place_copies(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("place_copies", {"a" : a, **kwargs})

class translate_copies(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("translate_copies", {"a" : a, **kwargs})

class line_of(OpenSCADObject):
    def __init__(self, p1=None, p2=None, n=None, **kwargs):
       super().__init__("line_of", {"p1" : p1, "p2" : p2, "n" : n, **kwargs})

class spread(OpenSCADObject):
    def __init__(self, p1=None, p2=None, spacing=None, l=None, n=None, **kwargs):
       super().__init__("spread", {"p1" : p1, "p2" : p2, "spacing" : spacing, "l" : l, "n" : n, **kwargs})

class xspread(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("xspread", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class yspread(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("yspread", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class zspread(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("zspread", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class distribute(OpenSCADObject):
    def __init__(self, spacing=None, sizes=None, dir=None, l=None, **kwargs):
       super().__init__("distribute", {"spacing" : spacing, "sizes" : sizes, "dir" : dir, "l" : l, **kwargs})

class xdistribute(OpenSCADObject):
    def __init__(self, spacing=None, sizes=None, l=None, **kwargs):
       super().__init__("xdistribute", {"spacing" : spacing, "sizes" : sizes, "l" : l, **kwargs})

class ydistribute(OpenSCADObject):
    def __init__(self, spacing=None, sizes=None, l=None, **kwargs):
       super().__init__("ydistribute", {"spacing" : spacing, "sizes" : sizes, "l" : l, **kwargs})

class zdistribute(OpenSCADObject):
    def __init__(self, spacing=None, sizes=None, l=None, **kwargs):
       super().__init__("zdistribute", {"spacing" : spacing, "sizes" : sizes, "l" : l, **kwargs})

class grid2d(OpenSCADObject):
    def __init__(self, size=None, spacing=None, cols=None, rows=None, stagger=None, scale=None, in_poly=None, orient=None, align=None, **kwargs):
       super().__init__("grid2d", {"size" : size, "spacing" : spacing, "cols" : cols, "rows" : rows, "stagger" : stagger, "scale" : scale, "in_poly" : in_poly, "orient" : orient, "align" : align, **kwargs})

class grid3d(OpenSCADObject):
    def __init__(self, xa=None, ya=None, za=None, n=None, spacing=None, **kwargs):
       super().__init__("grid3d", {"xa" : xa, "ya" : ya, "za" : za, "n" : n, "spacing" : spacing, **kwargs})

class grid_of(OpenSCADObject):
    def __init__(self, xa=None, ya=None, za=None, count=None, spacing=None, **kwargs):
       super().__init__("grid_of", {"xa" : xa, "ya" : ya, "za" : za, "count" : count, "spacing" : spacing, **kwargs})

class rot_copies(OpenSCADObject):
    def __init__(self, rots=None, v=None, cp=None, count=None, n=None, sa=None, offset=None, delta=None, subrot=None, **kwargs):
       super().__init__("rot_copies", {"rots" : rots, "v" : v, "cp" : cp, "count" : count, "n" : n, "sa" : sa, "offset" : offset, "delta" : delta, "subrot" : subrot, **kwargs})

class xrot_copies(OpenSCADObject):
    def __init__(self, rots=None, cp=None, n=None, count=None, sa=None, offset=None, r=None, subrot=None, **kwargs):
       super().__init__("xrot_copies", {"rots" : rots, "cp" : cp, "n" : n, "count" : count, "sa" : sa, "offset" : offset, "r" : r, "subrot" : subrot, **kwargs})

class yrot_copies(OpenSCADObject):
    def __init__(self, rots=None, cp=None, n=None, count=None, sa=None, offset=None, r=None, subrot=None, **kwargs):
       super().__init__("yrot_copies", {"rots" : rots, "cp" : cp, "n" : n, "count" : count, "sa" : sa, "offset" : offset, "r" : r, "subrot" : subrot, **kwargs})

class zrot_copies(OpenSCADObject):
    def __init__(self, rots=None, cp=None, n=None, count=None, sa=None, offset=None, r=None, subrot=None, **kwargs):
       super().__init__("zrot_copies", {"rots" : rots, "cp" : cp, "n" : n, "count" : count, "sa" : sa, "offset" : offset, "r" : r, "subrot" : subrot, **kwargs})

class xring(OpenSCADObject):
    def __init__(self, n=None, r=None, sa=None, cp=None, rot=None, **kwargs):
       super().__init__("xring", {"n" : n, "r" : r, "sa" : sa, "cp" : cp, "rot" : rot, **kwargs})

class yring(OpenSCADObject):
    def __init__(self, n=None, r=None, sa=None, cp=None, rot=None, **kwargs):
       super().__init__("yring", {"n" : n, "r" : r, "sa" : sa, "cp" : cp, "rot" : rot, **kwargs})

class zring(OpenSCADObject):
    def __init__(self, n=None, r=None, sa=None, cp=None, rot=None, **kwargs):
       super().__init__("zring", {"n" : n, "r" : r, "sa" : sa, "cp" : cp, "rot" : rot, **kwargs})

class arc_of(OpenSCADObject):
    def __init__(self, n=None, r=None, rx=None, ry=None, d=None, dx=None, dy=None, sa=None, ea=None, rot=None, **kwargs):
       super().__init__("arc_of", {"n" : n, "r" : r, "rx" : rx, "ry" : ry, "d" : d, "dx" : dx, "dy" : dy, "sa" : sa, "ea" : ea, "rot" : rot, **kwargs})

class ovoid_spread(OpenSCADObject):
    def __init__(self, r=None, d=None, n=None, cone_ang=None, scale=None, perp=None, **kwargs):
       super().__init__("ovoid_spread", {"r" : r, "d" : d, "n" : n, "cone_ang" : cone_ang, "scale" : scale, "perp" : perp, **kwargs})

class mirror_copy(OpenSCADObject):
    def __init__(self, v=None, offset=None, cp=None, **kwargs):
       super().__init__("mirror_copy", {"v" : v, "offset" : offset, "cp" : cp, **kwargs})

class xflip_copy(OpenSCADObject):
    def __init__(self, offset=None, cp=None, **kwargs):
       super().__init__("xflip_copy", {"offset" : offset, "cp" : cp, **kwargs})

class yflip_copy(OpenSCADObject):
    def __init__(self, offset=None, cp=None, **kwargs):
       super().__init__("yflip_copy", {"offset" : offset, "cp" : cp, **kwargs})

class zflip_copy(OpenSCADObject):
    def __init__(self, offset=None, cp=None, **kwargs):
       super().__init__("zflip_copy", {"offset" : offset, "cp" : cp, **kwargs})

class half_of(OpenSCADObject):
    def __init__(self, v=None, cp=None, s=None, planar=None, **kwargs):
       super().__init__("half_of", {"v" : v, "cp" : cp, "s" : s, "planar" : planar, **kwargs})

class top_half(OpenSCADObject):
    def __init__(self, s=None, z=None, cp=None, planar=None, **kwargs):
       super().__init__("top_half", {"s" : s, "z" : z, "cp" : cp, "planar" : planar, **kwargs})

class bottom_half(OpenSCADObject):
    def __init__(self, s=None, z=None, cp=None, planar=None, **kwargs):
       super().__init__("bottom_half", {"s" : s, "z" : z, "cp" : cp, "planar" : planar, **kwargs})

class left_half(OpenSCADObject):
    def __init__(self, s=None, x=None, cp=None, planar=None, **kwargs):
       super().__init__("left_half", {"s" : s, "x" : x, "cp" : cp, "planar" : planar, **kwargs})

class right_half(OpenSCADObject):
    def __init__(self, s=None, x=None, cp=None, planar=None, **kwargs):
       super().__init__("right_half", {"s" : s, "x" : x, "cp" : cp, "planar" : planar, **kwargs})

class front_half(OpenSCADObject):
    def __init__(self, s=None, y=None, cp=None, planar=None, **kwargs):
       super().__init__("front_half", {"s" : s, "y" : y, "cp" : cp, "planar" : planar, **kwargs})

class back_half(OpenSCADObject):
    def __init__(self, s=None, y=None, cp=None, planar=None, **kwargs):
       super().__init__("back_half", {"s" : s, "y" : y, "cp" : cp, "planar" : planar, **kwargs})

class chain_hull(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("chain_hull", {**kwargs})

class extrude_arc(OpenSCADObject):
    def __init__(self, arc=None, sa=None, r=None, d=None, orient=None, align=None, masksize=None, caps=None, convexity=None, **kwargs):
       super().__init__("extrude_arc", {"arc" : arc, "sa" : sa, "r" : r, "d" : d, "orient" : orient, "align" : align, "masksize" : masksize, "caps" : caps, "convexity" : convexity, **kwargs})

class round2d(OpenSCADObject):
    def __init__(self, r=None, _or=None, ir=None, **kwargs):
       super().__init__("round2d", {"r" : r, "_or" : _or, "ir" : ir, **kwargs})

class shell2d(OpenSCADObject):
    def __init__(self, thickness=None, _or=None, ir=None, fill=None, round=None, **kwargs):
       super().__init__("shell2d", {"thickness" : thickness, "_or" : _or, "ir" : ir, "fill" : fill, "round" : round, **kwargs})

class orient_and_align(OpenSCADObject):
    def __init__(self, size=None, orient=None, align=None, center=None, noncentered=None, orig_orient=None, orig_align=None, alignments=None, **kwargs):
       super().__init__("orient_and_align", {"size" : size, "orient" : orient, "align" : align, "center" : center, "noncentered" : noncentered, "orig_orient" : orig_orient, "orig_align" : orig_align, "alignments" : alignments, **kwargs})

