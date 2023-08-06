from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/gridbeam.scad'}", use_not_include=False)

mode = OpenSCADConstant('mode')
beam_width = OpenSCADConstant('beam_width')
beam_hole_diameter = OpenSCADConstant('beam_hole_diameter')
beam_hole_radius = OpenSCADConstant('beam_hole_radius')
beam_is_hollow = OpenSCADConstant('beam_is_hollow')
beam_wall_thickness = OpenSCADConstant('beam_wall_thickness')
beam_shelf_thickness = OpenSCADConstant('beam_shelf_thickness')
class zBeam(OpenSCADObject):
    def __init__(self, segments=None, **kwargs):
       super().__init__("zBeam", {"segments" : segments, **kwargs})

class xBeam(OpenSCADObject):
    def __init__(self, segments=None, **kwargs):
       super().__init__("xBeam", {"segments" : segments, **kwargs})

class yBeam(OpenSCADObject):
    def __init__(self, segments=None, **kwargs):
       super().__init__("yBeam", {"segments" : segments, **kwargs})

class zBolt(OpenSCADObject):
    def __init__(self, segments=None, **kwargs):
       super().__init__("zBolt", {"segments" : segments, **kwargs})

class xBolt(OpenSCADObject):
    def __init__(self, segments=None, **kwargs):
       super().__init__("xBolt", {"segments" : segments, **kwargs})

class yBolt(OpenSCADObject):
    def __init__(self, segments=None, **kwargs):
       super().__init__("yBolt", {"segments" : segments, **kwargs})

class translateBeam(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("translateBeam", {"v" : v, **kwargs})

class topShelf(OpenSCADObject):
    def __init__(self, width=None, depth=None, corners=None, **kwargs):
       super().__init__("topShelf", {"width" : width, "depth" : depth, "corners" : corners, **kwargs})

class bottomShelf(OpenSCADObject):
    def __init__(self, width=None, depth=None, corners=None, **kwargs):
       super().__init__("bottomShelf", {"width" : width, "depth" : depth, "corners" : corners, **kwargs})

class backBoard(OpenSCADObject):
    def __init__(self, width=None, height=None, corners=None, **kwargs):
       super().__init__("backBoard", {"width" : width, "height" : height, "corners" : corners, **kwargs})

class frontBoard(OpenSCADObject):
    def __init__(self, width=None, height=None, corners=None, **kwargs):
       super().__init__("frontBoard", {"width" : width, "height" : height, "corners" : corners, **kwargs})

