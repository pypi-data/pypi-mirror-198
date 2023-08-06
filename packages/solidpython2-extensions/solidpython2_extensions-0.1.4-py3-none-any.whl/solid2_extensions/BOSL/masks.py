from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/masks.scad'}", use_not_include=True)

class angle_pie_mask(OpenSCADObject):
    def __init__(self, ang=None, l=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, orient=None, align=None, h=None, center=None, **kwargs):
       super().__init__("angle_pie_mask", {"ang" : ang, "l" : l, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "orient" : orient, "align" : align, "h" : h, "center" : center, **kwargs})

class cylinder_mask(OpenSCADObject):
    def __init__(self, l=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, fillet=None, fillet1=None, fillet2=None, circum=None, from_end=None, overage=None, ends_only=None, orient=None, align=None, **kwargs):
       super().__init__("cylinder_mask", {"l" : l, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "fillet" : fillet, "fillet1" : fillet1, "fillet2" : fillet2, "circum" : circum, "from_end" : from_end, "overage" : overage, "ends_only" : ends_only, "orient" : orient, "align" : align, **kwargs})

class chamfer_mask(OpenSCADObject):
    def __init__(self, l=None, chamfer=None, orient=None, align=None, center=None, **kwargs):
       super().__init__("chamfer_mask", {"l" : l, "chamfer" : chamfer, "orient" : orient, "align" : align, "center" : center, **kwargs})

class chamfer_mask_x(OpenSCADObject):
    def __init__(self, l=None, chamfer=None, align=None, **kwargs):
       super().__init__("chamfer_mask_x", {"l" : l, "chamfer" : chamfer, "align" : align, **kwargs})

class chamfer_mask_y(OpenSCADObject):
    def __init__(self, l=None, chamfer=None, align=None, **kwargs):
       super().__init__("chamfer_mask_y", {"l" : l, "chamfer" : chamfer, "align" : align, **kwargs})

class chamfer_mask_z(OpenSCADObject):
    def __init__(self, l=None, chamfer=None, align=None, **kwargs):
       super().__init__("chamfer_mask_z", {"l" : l, "chamfer" : chamfer, "align" : align, **kwargs})

class chamfer(OpenSCADObject):
    def __init__(self, chamfer=None, size=None, edges=None, **kwargs):
       super().__init__("chamfer", {"chamfer" : chamfer, "size" : size, "edges" : edges, **kwargs})

class chamfer_cylinder_mask(OpenSCADObject):
    def __init__(self, r=None, d=None, chamfer=None, ang=None, from_end=None, orient=None, **kwargs):
       super().__init__("chamfer_cylinder_mask", {"r" : r, "d" : d, "chamfer" : chamfer, "ang" : ang, "from_end" : from_end, "orient" : orient, **kwargs})

class chamfer_hole_mask(OpenSCADObject):
    def __init__(self, r=None, d=None, chamfer=None, ang=None, from_end=None, overage=None, **kwargs):
       super().__init__("chamfer_hole_mask", {"r" : r, "d" : d, "chamfer" : chamfer, "ang" : ang, "from_end" : from_end, "overage" : overage, **kwargs})

class fillet_mask(OpenSCADObject):
    def __init__(self, l=None, r=None, orient=None, align=None, h=None, center=None, **kwargs):
       super().__init__("fillet_mask", {"l" : l, "r" : r, "orient" : orient, "align" : align, "h" : h, "center" : center, **kwargs})

class fillet_mask_x(OpenSCADObject):
    def __init__(self, l=None, r=None, align=None, **kwargs):
       super().__init__("fillet_mask_x", {"l" : l, "r" : r, "align" : align, **kwargs})

class fillet_mask_y(OpenSCADObject):
    def __init__(self, l=None, r=None, align=None, **kwargs):
       super().__init__("fillet_mask_y", {"l" : l, "r" : r, "align" : align, **kwargs})

class fillet_mask_z(OpenSCADObject):
    def __init__(self, l=None, r=None, align=None, **kwargs):
       super().__init__("fillet_mask_z", {"l" : l, "r" : r, "align" : align, **kwargs})

class fillet(OpenSCADObject):
    def __init__(self, fillet=None, size=None, edges=None, **kwargs):
       super().__init__("fillet", {"fillet" : fillet, "size" : size, "edges" : edges, **kwargs})

class fillet_angled_edge_mask(OpenSCADObject):
    def __init__(self, h=None, r=None, ang=None, center=None, **kwargs):
       super().__init__("fillet_angled_edge_mask", {"h" : h, "r" : r, "ang" : ang, "center" : center, **kwargs})

class fillet_angled_corner_mask(OpenSCADObject):
    def __init__(self, fillet=None, ang=None, **kwargs):
       super().__init__("fillet_angled_corner_mask", {"fillet" : fillet, "ang" : ang, **kwargs})

class fillet_corner_mask(OpenSCADObject):
    def __init__(self, r=None, **kwargs):
       super().__init__("fillet_corner_mask", {"r" : r, **kwargs})

class fillet_cylinder_mask(OpenSCADObject):
    def __init__(self, r=None, fillet=None, xtilt=None, ytilt=None, **kwargs):
       super().__init__("fillet_cylinder_mask", {"r" : r, "fillet" : fillet, "xtilt" : xtilt, "ytilt" : ytilt, **kwargs})

class fillet_hole_mask(OpenSCADObject):
    def __init__(self, r=None, d=None, fillet=None, overage=None, xtilt=None, ytilt=None, **kwargs):
       super().__init__("fillet_hole_mask", {"r" : r, "d" : d, "fillet" : fillet, "overage" : overage, "xtilt" : xtilt, "ytilt" : ytilt, **kwargs})

