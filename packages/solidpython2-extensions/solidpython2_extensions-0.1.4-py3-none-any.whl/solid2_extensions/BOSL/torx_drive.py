from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/torx_drive.scad'}", use_not_include=True)

class torx_drive2d(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("torx_drive2d", {"size" : size, **kwargs})

class torx_drive(OpenSCADObject):
    def __init__(self, size=None, l=None, center=None, orient=None, align=None, **kwargs):
       super().__init__("torx_drive", {"size" : size, "l" : l, "center" : center, "orient" : orient, "align" : align, **kwargs})

class torx_outer_diam(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("torx_outer_diam", {"size" : size, **kwargs})

class torx_inner_diam(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("torx_inner_diam", {"size" : size, **kwargs})

class torx_depth(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("torx_depth", {"size" : size, **kwargs})

class torx_tip_radius(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("torx_tip_radius", {"size" : size, **kwargs})

class torx_rounding_radius(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("torx_rounding_radius", {"size" : size, **kwargs})

