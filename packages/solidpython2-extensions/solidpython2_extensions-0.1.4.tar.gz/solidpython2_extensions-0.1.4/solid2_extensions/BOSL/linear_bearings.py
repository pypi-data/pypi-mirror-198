from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/linear_bearings.scad'}", use_not_include=True)

class linear_bearing_housing(OpenSCADObject):
    def __init__(self, d=None, l=None, tab=None, gap=None, wall=None, tabwall=None, screwsize=None, orient=None, align=None, **kwargs):
       super().__init__("linear_bearing_housing", {"d" : d, "l" : l, "tab" : tab, "gap" : gap, "wall" : wall, "tabwall" : tabwall, "screwsize" : screwsize, "orient" : orient, "align" : align, **kwargs})

class lmXuu_housing(OpenSCADObject):
    def __init__(self, size=None, tab=None, gap=None, wall=None, tabwall=None, screwsize=None, orient=None, align=None, **kwargs):
       super().__init__("lmXuu_housing", {"size" : size, "tab" : tab, "gap" : gap, "wall" : wall, "tabwall" : tabwall, "screwsize" : screwsize, "orient" : orient, "align" : align, **kwargs})

class get_lmXuu_bearing_diam(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_lmXuu_bearing_diam", {"size" : size, **kwargs})

class get_lmXuu_bearing_length(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_lmXuu_bearing_length", {"size" : size, **kwargs})

