from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/shapes.scad'}", use_not_include=True)

class cuboid(OpenSCADObject):
    def __init__(self, size=None, p1=None, p2=None, chamfer=None, fillet=None, edges=None, trimcorners=None, align=None, center=None, **kwargs):
       super().__init__("cuboid", {"size" : size, "p1" : p1, "p2" : p2, "chamfer" : chamfer, "fillet" : fillet, "edges" : edges, "trimcorners" : trimcorners, "align" : align, "center" : center, **kwargs})

class cube2pt(OpenSCADObject):
    def __init__(self, p1=None, p2=None, **kwargs):
       super().__init__("cube2pt", {"p1" : p1, "p2" : p2, **kwargs})

class span_cube(OpenSCADObject):
    def __init__(self, xspan=None, yspan=None, zspan=None, **kwargs):
       super().__init__("span_cube", {"xspan" : xspan, "yspan" : yspan, "zspan" : zspan, **kwargs})

class offsetcube(OpenSCADObject):
    def __init__(self, size=None, v=None, **kwargs):
       super().__init__("offsetcube", {"size" : size, "v" : v, **kwargs})

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

class chamfcube(OpenSCADObject):
    def __init__(self, size=None, chamfer=None, chamfaxes=None, chamfcorners=None, **kwargs):
       super().__init__("chamfcube", {"size" : size, "chamfer" : chamfer, "chamfaxes" : chamfaxes, "chamfcorners" : chamfcorners, **kwargs})

class rrect(OpenSCADObject):
    def __init__(self, size=None, r=None, center=None, **kwargs):
       super().__init__("rrect", {"size" : size, "r" : r, "center" : center, **kwargs})

class rcube(OpenSCADObject):
    def __init__(self, size=None, r=None, center=None, **kwargs):
       super().__init__("rcube", {"size" : size, "r" : r, "center" : center, **kwargs})

class prismoid(OpenSCADObject):
    def __init__(self, size1=None, size2=None, h=None, shift=None, orient=None, align=None, center=None, **kwargs):
       super().__init__("prismoid", {"size1" : size1, "size2" : size2, "h" : h, "shift" : shift, "orient" : orient, "align" : align, "center" : center, **kwargs})

class trapezoid(OpenSCADObject):
    def __init__(self, size1=None, size2=None, h=None, center=None, **kwargs):
       super().__init__("trapezoid", {"size1" : size1, "size2" : size2, "h" : h, "center" : center, **kwargs})

class rounded_prismoid(OpenSCADObject):
    def __init__(self, size1=None, size2=None, h=None, shift=None, r=None, r1=None, r2=None, align=None, orient=None, center=None, **kwargs):
       super().__init__("rounded_prismoid", {"size1" : size1, "size2" : size2, "h" : h, "shift" : shift, "r" : r, "r1" : r1, "r2" : r2, "align" : align, "orient" : orient, "center" : center, **kwargs})

class pyramid(OpenSCADObject):
    def __init__(self, n=None, h=None, l=None, r=None, d=None, circum=None, **kwargs):
       super().__init__("pyramid", {"n" : n, "h" : h, "l" : l, "r" : r, "d" : d, "circum" : circum, **kwargs})

class prism(OpenSCADObject):
    def __init__(self, n=None, h=None, l=None, r=None, d=None, circum=None, center=None, **kwargs):
       super().__init__("prism", {"n" : n, "h" : h, "l" : l, "r" : r, "d" : d, "circum" : circum, "center" : center, **kwargs})

class right_triangle(OpenSCADObject):
    def __init__(self, size=None, orient=None, align=None, center=None, **kwargs):
       super().__init__("right_triangle", {"size" : size, "orient" : orient, "align" : align, "center" : center, **kwargs})

class cyl(OpenSCADObject):
    def __init__(self, l=None, h=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, fillet=None, fillet1=None, fillet2=None, circum=None, realign=None, from_end=None, orient=None, align=None, center=None, **kwargs):
       super().__init__("cyl", {"l" : l, "h" : h, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "fillet" : fillet, "fillet1" : fillet1, "fillet2" : fillet2, "circum" : circum, "realign" : realign, "from_end" : from_end, "orient" : orient, "align" : align, "center" : center, **kwargs})

class downcyl(OpenSCADObject):
    def __init__(self, r=None, h=None, l=None, d=None, d1=None, d2=None, r1=None, r2=None, **kwargs):
       super().__init__("downcyl", {"r" : r, "h" : h, "l" : l, "d" : d, "d1" : d1, "d2" : d2, "r1" : r1, "r2" : r2, **kwargs})

class xcyl(OpenSCADObject):
    def __init__(self, l=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, h=None, align=None, center=None, **kwargs):
       super().__init__("xcyl", {"l" : l, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "h" : h, "align" : align, "center" : center, **kwargs})

class ycyl(OpenSCADObject):
    def __init__(self, l=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, h=None, align=None, center=None, **kwargs):
       super().__init__("ycyl", {"l" : l, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "h" : h, "align" : align, "center" : center, **kwargs})

class zcyl(OpenSCADObject):
    def __init__(self, l=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, h=None, align=None, center=None, **kwargs):
       super().__init__("zcyl", {"l" : l, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "h" : h, "align" : align, "center" : center, **kwargs})

class chamferred_cylinder(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, chamfer=None, chamfedge=None, angle=None, center=None, top=None, bottom=None, **kwargs):
       super().__init__("chamferred_cylinder", {"h" : h, "r" : r, "d" : d, "chamfer" : chamfer, "chamfedge" : chamfedge, "angle" : angle, "center" : center, "top" : top, "bottom" : bottom, **kwargs})

class chamf_cyl(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, chamfer=None, chamfedge=None, angle=None, center=None, top=None, bottom=None, **kwargs):
       super().__init__("chamf_cyl", {"h" : h, "r" : r, "d" : d, "chamfer" : chamfer, "chamfedge" : chamfedge, "angle" : angle, "center" : center, "top" : top, "bottom" : bottom, **kwargs})

class filleted_cylinder(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, fillet=None, center=None, **kwargs):
       super().__init__("filleted_cylinder", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "fillet" : fillet, "center" : center, **kwargs})

class rcylinder(OpenSCADObject):
    def __init__(self, h=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, fillet=None, center=None, **kwargs):
       super().__init__("rcylinder", {"h" : h, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "fillet" : fillet, "center" : center, **kwargs})

class tube(OpenSCADObject):
    def __init__(self, h=None, wall=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, _or=None, or1=None, or2=None, od=None, od1=None, od2=None, ir=None, id=None, ir1=None, ir2=None, id1=None, id2=None, center=None, orient=None, align=None, realign=None, **kwargs):
       super().__init__("tube", {"h" : h, "wall" : wall, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "_or" : _or, "or1" : or1, "or2" : or2, "od" : od, "od1" : od1, "od2" : od2, "ir" : ir, "id" : id, "ir1" : ir1, "ir2" : ir2, "id1" : id1, "id2" : id2, "center" : center, "orient" : orient, "align" : align, "realign" : realign, **kwargs})

class torus(OpenSCADObject):
    def __init__(self, r=None, d=None, r2=None, d2=None, _or=None, od=None, ir=None, id=None, orient=None, align=None, center=None, **kwargs):
       super().__init__("torus", {"r" : r, "d" : d, "r2" : r2, "d2" : d2, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "orient" : orient, "align" : align, "center" : center, **kwargs})

class staggered_sphere(OpenSCADObject):
    def __init__(self, r=None, d=None, circum=None, align=None, **kwargs):
       super().__init__("staggered_sphere", {"r" : r, "d" : d, "circum" : circum, "align" : align, **kwargs})

class teardrop2d(OpenSCADObject):
    def __init__(self, r=None, d=None, ang=None, cap_h=None, **kwargs):
       super().__init__("teardrop2d", {"r" : r, "d" : d, "ang" : ang, "cap_h" : cap_h, **kwargs})

class teardrop(OpenSCADObject):
    def __init__(self, r=None, d=None, l=None, h=None, ang=None, cap_h=None, orient=None, align=None, **kwargs):
       super().__init__("teardrop", {"r" : r, "d" : d, "l" : l, "h" : h, "ang" : ang, "cap_h" : cap_h, "orient" : orient, "align" : align, **kwargs})

class onion(OpenSCADObject):
    def __init__(self, cap_h=None, r=None, d=None, maxang=None, h=None, orient=None, align=None, **kwargs):
       super().__init__("onion", {"cap_h" : cap_h, "r" : r, "d" : d, "maxang" : maxang, "h" : h, "orient" : orient, "align" : align, **kwargs})

class narrowing_strut(OpenSCADObject):
    def __init__(self, w=None, l=None, wall=None, ang=None, orient=None, align=None, **kwargs):
       super().__init__("narrowing_strut", {"w" : w, "l" : l, "wall" : wall, "ang" : ang, "orient" : orient, "align" : align, **kwargs})

class thinning_wall(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, ang=None, strut=None, wall=None, orient=None, align=None, **kwargs):
       super().__init__("thinning_wall", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "strut" : strut, "wall" : wall, "orient" : orient, "align" : align, **kwargs})

class braced_thinning_wall(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, ang=None, strut=None, wall=None, orient=None, align=None, **kwargs):
       super().__init__("braced_thinning_wall", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "strut" : strut, "wall" : wall, "orient" : orient, "align" : align, **kwargs})

class thinning_triangle(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, ang=None, strut=None, wall=None, diagonly=None, center=None, orient=None, align=None, **kwargs):
       super().__init__("thinning_triangle", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "strut" : strut, "wall" : wall, "diagonly" : diagonly, "center" : center, "orient" : orient, "align" : align, **kwargs})

class thinning_brace(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, ang=None, strut=None, wall=None, center=None, **kwargs):
       super().__init__("thinning_brace", {"h" : h, "l" : l, "thick" : thick, "ang" : ang, "strut" : strut, "wall" : wall, "center" : center, **kwargs})

class sparse_strut(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, maxang=None, strut=None, max_bridge=None, orient=None, align=None, **kwargs):
       super().__init__("sparse_strut", {"h" : h, "l" : l, "thick" : thick, "maxang" : maxang, "strut" : strut, "max_bridge" : max_bridge, "orient" : orient, "align" : align, **kwargs})

class sparse_strut3d(OpenSCADObject):
    def __init__(self, h=None, l=None, w=None, thick=None, maxang=None, strut=None, max_bridge=None, orient=None, align=None, **kwargs):
       super().__init__("sparse_strut3d", {"h" : h, "l" : l, "w" : w, "thick" : thick, "maxang" : maxang, "strut" : strut, "max_bridge" : max_bridge, "orient" : orient, "align" : align, **kwargs})

class corrugated_wall(OpenSCADObject):
    def __init__(self, h=None, l=None, thick=None, strut=None, wall=None, orient=None, align=None, **kwargs):
       super().__init__("corrugated_wall", {"h" : h, "l" : l, "thick" : thick, "strut" : strut, "wall" : wall, "orient" : orient, "align" : align, **kwargs})

class nil(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("nil", {**kwargs})

class noop(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("noop", {**kwargs})

class pie_slice(OpenSCADObject):
    def __init__(self, ang=None, l=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, orient=None, align=None, center=None, h=None, **kwargs):
       super().__init__("pie_slice", {"ang" : ang, "l" : l, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "orient" : orient, "align" : align, "center" : center, "h" : h, **kwargs})

class interior_fillet(OpenSCADObject):
    def __init__(self, l=None, r=None, ang=None, overlap=None, orient=None, align=None, **kwargs):
       super().__init__("interior_fillet", {"l" : l, "r" : r, "ang" : ang, "overlap" : overlap, "orient" : orient, "align" : align, **kwargs})

class slot(OpenSCADObject):
    def __init__(self, p1=None, p2=None, h=None, l=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, **kwargs):
       super().__init__("slot", {"p1" : p1, "p2" : p2, "h" : h, "l" : l, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, **kwargs})

class arced_slot(OpenSCADObject):
    def __init__(self, r=None, d=None, h=None, sr=None, sr1=None, sr2=None, sd=None, sd1=None, sd2=None, sa=None, ea=None, cp=None, orient=None, align=None, _fn2=None, **kwargs):
       super().__init__("arced_slot", {"r" : r, "d" : d, "h" : h, "sr" : sr, "sr1" : sr1, "sr2" : sr2, "sd" : sd, "sd1" : sd1, "sd2" : sd2, "sa" : sa, "ea" : ea, "cp" : cp, "orient" : orient, "align" : align, "_fn2" : _fn2, **kwargs})

