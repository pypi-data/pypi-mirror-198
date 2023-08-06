from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/profiles.scad'}", use_not_include=False)

_fn = OpenSCADConstant('_fn')
class profile_angle_equal(OpenSCADObject):
    def __init__(self, side=None, wall=None, **kwargs):
       super().__init__("profile_angle_equal", {"side" : side, "wall" : wall, **kwargs})

class profile_angle_unequal(OpenSCADObject):
    def __init__(self, side_x=None, side_y=None, wall=None, **kwargs):
       super().__init__("profile_angle_unequal", {"side_x" : side_x, "side_y" : side_y, "wall" : wall, **kwargs})

class profile_square_tube(OpenSCADObject):
    def __init__(self, side=None, wall=None, **kwargs):
       super().__init__("profile_square_tube", {"side" : side, "wall" : wall, **kwargs})

class profile_rect_tube(OpenSCADObject):
    def __init__(self, side_x=None, side_y=None, wall=None, **kwargs):
       super().__init__("profile_rect_tube", {"side_x" : side_x, "side_y" : side_y, "wall" : wall, **kwargs})

class profile_channel(OpenSCADObject):
    def __init__(self, base=None, side=None, wall=None, **kwargs):
       super().__init__("profile_channel", {"base" : base, "side" : side, "wall" : wall, **kwargs})

class profile_tslot_generic(OpenSCADObject):
    def __init__(self, pitch=None, slot=None, lip=None, web=None, core=None, hole=None, **kwargs):
       super().__init__("profile_tslot_generic", {"pitch" : pitch, "slot" : slot, "lip" : lip, "web" : web, "core" : core, "hole" : hole, **kwargs})

class profile_8020_fractional_1010(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("profile_8020_fractional_1010", {**kwargs})

class profile_misumi_metric_2020(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("profile_misumi_metric_2020", {**kwargs})

class profile_makerbeam(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("profile_makerbeam", {**kwargs})

