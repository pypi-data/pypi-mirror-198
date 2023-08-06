from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/involute_gears.scad'}", use_not_include=True)

class gear_tooth_profile(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, pressure_angle=None, backlash=None, bevelang=None, clearance=None, interior=None, valleys=None, **kwargs):
       super().__init__("gear_tooth_profile", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "pressure_angle" : pressure_angle, "backlash" : backlash, "bevelang" : bevelang, "clearance" : clearance, "interior" : interior, "valleys" : valleys, **kwargs})

class gear2d(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, teeth_to_hide=None, pressure_angle=None, clearance=None, backlash=None, bevelang=None, interior=None, **kwargs):
       super().__init__("gear2d", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "teeth_to_hide" : teeth_to_hide, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "bevelang" : bevelang, "interior" : interior, **kwargs})

class gear(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, thickness=None, hole_diameter=None, teeth_to_hide=None, pressure_angle=None, clearance=None, backlash=None, bevelang=None, twist=None, slices=None, interior=None, orient=None, align=None, **kwargs):
       super().__init__("gear", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "thickness" : thickness, "hole_diameter" : hole_diameter, "teeth_to_hide" : teeth_to_hide, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "bevelang" : bevelang, "twist" : twist, "slices" : slices, "interior" : interior, "orient" : orient, "align" : align, **kwargs})

class rack(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, thickness=None, height=None, pressure_angle=None, backlash=None, clearance=None, orient=None, align=None, **kwargs):
       super().__init__("rack", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "thickness" : thickness, "height" : height, "pressure_angle" : pressure_angle, "backlash" : backlash, "clearance" : clearance, "orient" : orient, "align" : align, **kwargs})

class circular_pitch(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, **kwargs):
       super().__init__("circular_pitch", {"mm_per_tooth" : mm_per_tooth, **kwargs})

class diametral_pitch(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, **kwargs):
       super().__init__("diametral_pitch", {"mm_per_tooth" : mm_per_tooth, **kwargs})

class module_value(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, **kwargs):
       super().__init__("module_value", {"mm_per_tooth" : mm_per_tooth, **kwargs})

class adendum(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, **kwargs):
       super().__init__("adendum", {"mm_per_tooth" : mm_per_tooth, **kwargs})

class dedendum(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, clearance=None, **kwargs):
       super().__init__("dedendum", {"mm_per_tooth" : mm_per_tooth, "clearance" : clearance, **kwargs})

class pitch_radius(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, **kwargs):
       super().__init__("pitch_radius", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, **kwargs})

class outer_radius(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, clearance=None, interior=None, **kwargs):
       super().__init__("outer_radius", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "clearance" : clearance, "interior" : interior, **kwargs})

class root_radius(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, clearance=None, interior=None, **kwargs):
       super().__init__("root_radius", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "clearance" : clearance, "interior" : interior, **kwargs})

class base_radius(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, pressure_angle=None, **kwargs):
       super().__init__("base_radius", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "pressure_angle" : pressure_angle, **kwargs})

class _gear_polar(OpenSCADObject):
    def __init__(self, r=None, theta=None, **kwargs):
       super().__init__("_gear_polar", {"r" : r, "theta" : theta, **kwargs})

class _gear_iang(OpenSCADObject):
    def __init__(self, r1=None, r2=None, **kwargs):
       super().__init__("_gear_iang", {"r1" : r1, "r2" : r2, **kwargs})

class _gear_q7(OpenSCADObject):
    def __init__(self, f=None, r=None, b=None, r2=None, t=None, s=None, **kwargs):
       super().__init__("_gear_q7", {"f" : f, "r" : r, "b" : b, "r2" : r2, "t" : t, "s" : s, **kwargs})

class _gear_q6(OpenSCADObject):
    def __init__(self, b=None, s=None, t=None, d=None, **kwargs):
       super().__init__("_gear_q6", {"b" : b, "s" : s, "t" : t, "d" : d, **kwargs})

class gear_tooth_profile(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, pressure_angle=None, backlash=None, bevelang=None, clearance=None, interior=None, valleys=None, **kwargs):
       super().__init__("gear_tooth_profile", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "pressure_angle" : pressure_angle, "backlash" : backlash, "bevelang" : bevelang, "clearance" : clearance, "interior" : interior, "valleys" : valleys, **kwargs})

class gear2d(OpenSCADObject):
    def __init__(self, mm_per_tooth=None, number_of_teeth=None, teeth_to_hide=None, pressure_angle=None, clearance=None, backlash=None, bevelang=None, interior=None, **kwargs):
       super().__init__("gear2d", {"mm_per_tooth" : mm_per_tooth, "number_of_teeth" : number_of_teeth, "teeth_to_hide" : teeth_to_hide, "pressure_angle" : pressure_angle, "clearance" : clearance, "backlash" : backlash, "bevelang" : bevelang, "interior" : interior, **kwargs})

