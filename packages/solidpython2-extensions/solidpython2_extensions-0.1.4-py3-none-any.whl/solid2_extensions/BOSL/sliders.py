from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/sliders.scad'}", use_not_include=True)

class slider(OpenSCADObject):
    def __init__(self, l=None, w=None, h=None, chamfer=None, base=None, wall=None, ang=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("slider", {"l" : l, "w" : w, "h" : h, "chamfer" : chamfer, "base" : base, "wall" : wall, "ang" : ang, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class rail(OpenSCADObject):
    def __init__(self, l=None, w=None, h=None, chamfer=None, ang=None, orient=None, align=None, **kwargs):
       super().__init__("rail", {"l" : l, "w" : w, "h" : h, "chamfer" : chamfer, "ang" : ang, "orient" : orient, "align" : align, **kwargs})

