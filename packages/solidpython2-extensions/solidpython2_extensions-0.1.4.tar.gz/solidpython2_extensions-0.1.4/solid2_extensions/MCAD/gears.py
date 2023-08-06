from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/gears.scad'}", use_not_include=False)

class gear(OpenSCADObject):
    def __init__(self, number_of_teeth=None, circular_pitch=None, diametral_pitch=None, pressure_angle=None, clearance=None, verbose=None, **kwargs):
       super().__init__("gear", {"number_of_teeth" : number_of_teeth, "circular_pitch" : circular_pitch, "diametral_pitch" : diametral_pitch, "pressure_angle" : pressure_angle, "clearance" : clearance, "verbose" : verbose, **kwargs})

class involute_gear_tooth(OpenSCADObject):
    def __init__(self, pitch_radius=None, root_radius=None, base_radius=None, outer_radius=None, half_thick_angle=None, **kwargs):
       super().__init__("involute_gear_tooth", {"pitch_radius" : pitch_radius, "root_radius" : root_radius, "base_radius" : base_radius, "outer_radius" : outer_radius, "half_thick_angle" : half_thick_angle, **kwargs})

class test_gears(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_gears", {**kwargs})

class demo_3d_gears(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("demo_3d_gears", {**kwargs})

class test_involute_curve(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_involute_curve", {**kwargs})

class pitch_circular2diameter(OpenSCADObject):
    def __init__(self, number_of_teeth=None, circular_pitch=None, **kwargs):
       super().__init__("pitch_circular2diameter", {"number_of_teeth" : number_of_teeth, "circular_pitch" : circular_pitch, **kwargs})

class pitch_diametral2diameter(OpenSCADObject):
    def __init__(self, number_of_teeth=None, diametral_pitch=None, **kwargs):
       super().__init__("pitch_diametral2diameter", {"number_of_teeth" : number_of_teeth, "diametral_pitch" : diametral_pitch, **kwargs})

class involute_intersect_angle(OpenSCADObject):
    def __init__(self, base_radius=None, radius=None, **kwargs):
       super().__init__("involute_intersect_angle", {"base_radius" : base_radius, "radius" : radius, **kwargs})

class polar_to_cartesian(OpenSCADObject):
    def __init__(self, polar=None, **kwargs):
       super().__init__("polar_to_cartesian", {"polar" : polar, **kwargs})

