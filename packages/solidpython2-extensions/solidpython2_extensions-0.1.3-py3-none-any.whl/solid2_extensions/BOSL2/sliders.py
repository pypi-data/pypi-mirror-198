from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/sliders.scad'}", use_not_include=False)

class slider(OpenSCADObject):
    def __init__(self, l=None, w=None, h=None, base=None, wall=None, ang=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("slider", {"l" : l, "w" : w, "h" : h, "base" : base, "wall" : wall, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rail(OpenSCADObject):
    def __init__(self, l=None, w=None, h=None, chamfer=None, ang=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rail", {"l" : l, "w" : w, "h" : h, "chamfer" : chamfer, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class slider(OpenSCADObject):
    def __init__(self, l=None, w=None, h=None, base=None, wall=None, ang=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("slider", {"l" : l, "w" : w, "h" : h, "base" : base, "wall" : wall, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rail(OpenSCADObject):
    def __init__(self, l=None, w=None, h=None, chamfer=None, ang=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("rail", {"l" : l, "w" : w, "h" : h, "chamfer" : chamfer, "ang" : ang, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

