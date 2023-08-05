from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/bosl1compat.scad'}", use_not_include=False)

class translate_copies(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("translate_copies", {"a" : a, **kwargs})

class xmove(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("xmove", {"x" : x, **kwargs})

class ymove(OpenSCADObject):
    def __init__(self, y=None, **kwargs):
       super().__init__("ymove", {"y" : y, **kwargs})

class zmove(OpenSCADObject):
    def __init__(self, z=None, **kwargs):
       super().__init__("zmove", {"z" : z, **kwargs})

class xspread(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("xspread", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class yspread(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("yspread", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class zspread(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("zspread", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class spread(OpenSCADObject):
    def __init__(self, p1=None, p2=None, spacing=None, l=None, n=None, **kwargs):
       super().__init__("spread", {"p1" : p1, "p2" : p2, "spacing" : spacing, "l" : l, "n" : n, **kwargs})

class grid_of(OpenSCADObject):
    def __init__(self, xa=None, ya=None, za=None, count=None, spacing=None, **kwargs):
       super().__init__("grid_of", {"xa" : xa, "ya" : ya, "za" : za, "count" : count, "spacing" : spacing, **kwargs})

class xring(OpenSCADObject):
    def __init__(self, n=None, r=None, sa=None, cp=None, rot=None, **kwargs):
       super().__init__("xring", {"n" : n, "r" : r, "sa" : sa, "cp" : cp, "rot" : rot, **kwargs})

class yring(OpenSCADObject):
    def __init__(self, n=None, r=None, sa=None, cp=None, rot=None, **kwargs):
       super().__init__("yring", {"n" : n, "r" : r, "sa" : sa, "cp" : cp, "rot" : rot, **kwargs})

class zring(OpenSCADObject):
    def __init__(self, n=None, r=None, sa=None, cp=None, rot=None, **kwargs):
       super().__init__("zring", {"n" : n, "r" : r, "sa" : sa, "cp" : cp, "rot" : rot, **kwargs})

class leftcube(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("leftcube", {"size" : size, **kwargs})

class rightcube(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("rightcube", {"size" : size, **kwargs})

class fwdcube(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("fwdcube", {"size" : size, **kwargs})

class backcube(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("backcube", {"size" : size, **kwargs})

class downcube(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("downcube", {"size" : size, **kwargs})

class upcube(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("upcube", {"size" : size, **kwargs})

class cube2pt(OpenSCADObject):
    def __init__(self, p1=None, p2=None, **kwargs):
       super().__init__("cube2pt", {"p1" : p1, "p2" : p2, **kwargs})

class offsetcube(OpenSCADObject):
    def __init__(self, size=None, v=None, **kwargs):
       super().__init__("offsetcube", {"size" : size, "v" : v, **kwargs})

class rrect(OpenSCADObject):
    def __init__(self, size=None, r=None, center=None, **kwargs):
       super().__init__("rrect", {"size" : size, "r" : r, "center" : center, **kwargs})

class rcube(OpenSCADObject):
    def __init__(self, size=None, r=None, center=None, **kwargs):
       super().__init__("rcube", {"size" : size, "r" : r, "center" : center, **kwargs})

class chamfcube(OpenSCADObject):
    def __init__(self, size=None, chamfer=None, chamfaxes=None, chamfcorners=None, **kwargs):
       super().__init__("chamfcube", {"size" : size, "chamfer" : chamfer, "chamfaxes" : chamfaxes, "chamfcorners" : chamfcorners, **kwargs})

class trapezoid(OpenSCADObject):
    def __init__(self, size1=None, size2=None, h=None, shift=None, align=None, orient=None, center=None, **kwargs):
       super().__init__("trapezoid", {"size1" : size1, "size2" : size2, "h" : h, "shift" : shift, "align" : align, "orient" : orient, "center" : center, **kwargs})

class pyramid(OpenSCADObject):
    def __init__(self, n=None, h=None, l=None, r=None, d=None, circum=None, **kwargs):
       super().__init__("pyramid", {"n" : n, "h" : h, "l" : l, "r" : r, "d" : d, "circum" : circum, **kwargs})

class prism(OpenSCADObject):
    def __init__(self, n=None, h=None, l=None, r=None, d=None, circum=None, center=None, **kwargs):
       super().__init__("prism", {"n" : n, "h" : h, "l" : l, "r" : r, "d" : d, "circum" : circum, "center" : center, **kwargs})

class chamferred_cylinder(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, chamfer=None, chamfedge=None, angle=None, top=None, bottom=None, center=None, **kwargs):
       super().__init__("chamferred_cylinder", {"h" : h, "r" : r, "d" : d, "chamfer" : chamfer, "chamfedge" : chamfedge, "angle" : angle, "top" : top, "bottom" : bottom, "center" : center, **kwargs})

class chamf_cyl(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, chamfer=None, chamfedge=None, angle=None, center=None, top=None, bottom=None, **kwargs):
       super().__init__("chamf_cyl", {"h" : h, "r" : r, "d" : d, "chamfer" : chamfer, "chamfedge" : chamfedge, "angle" : angle, "center" : center, "top" : top, "bottom" : bottom, **kwargs})

class filleted_cylinder(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, fillet=None, center=None, **kwargs):
       super().__init__("filleted_cylinder", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "fillet" : fillet, "center" : center, **kwargs})

class rcylinder(OpenSCADObject):
    def __init__(self, h=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, fillet=None, center=None, **kwargs):
       super().__init__("rcylinder", {"h" : h, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "fillet" : fillet, "center" : center, **kwargs})

class thinning_brace(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, ang=None, strut=None, wall=None, center=None, **kwargs):
       super().__init__("thinning_brace", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "strut" : strut, "wall" : wall, "center" : center, **kwargs})

