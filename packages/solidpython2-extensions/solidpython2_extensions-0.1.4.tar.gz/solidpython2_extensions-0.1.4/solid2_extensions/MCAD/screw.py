from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/screw.scad'}", use_not_include=False)

class helix(OpenSCADObject):
    def __init__(self, pitch=None, length=None, slices=None, **kwargs):
       super().__init__("helix", {"pitch" : pitch, "length" : length, "slices" : slices, **kwargs})

class auger(OpenSCADObject):
    def __init__(self, pitch=None, length=None, outside_radius=None, inner_radius=None, taper_ratio=None, **kwargs):
       super().__init__("auger", {"pitch" : pitch, "length" : length, "outside_radius" : outside_radius, "inner_radius" : inner_radius, "taper_ratio" : taper_ratio, **kwargs})

class test_auger(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_auger", {**kwargs})

class ball_groove(OpenSCADObject):
    def __init__(self, pitch=None, length=None, diameter=None, ball_radius=None, **kwargs):
       super().__init__("ball_groove", {"pitch" : pitch, "length" : length, "diameter" : diameter, "ball_radius" : ball_radius, **kwargs})

class test_ball_groove(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_ball_groove", {**kwargs})

class ball_groove2(OpenSCADObject):
    def __init__(self, pitch=None, length=None, diameter=None, ball_radius=None, slices=None, **kwargs):
       super().__init__("ball_groove2", {"pitch" : pitch, "length" : length, "diameter" : diameter, "ball_radius" : ball_radius, "slices" : slices, **kwargs})

class test_ball_groove2(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_ball_groove2", {**kwargs})

class ball_screw(OpenSCADObject):
    def __init__(self, pitch=None, length=None, bearing_radius=None, **kwargs):
       super().__init__("ball_screw", {"pitch" : pitch, "length" : length, "bearing_radius" : bearing_radius, **kwargs})

class test_ball_screw(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_ball_screw", {**kwargs})

