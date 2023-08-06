from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/involute_gears.scad'}", use_not_include=False)

pi = OpenSCADConstant('pi')
bevel_gear_flat = OpenSCADConstant('bevel_gear_flat')
bevel_gear_back_cone = OpenSCADConstant('bevel_gear_back_cone')
class test_meshing_double_helix(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_meshing_double_helix", {**kwargs})

class test_bevel_gear_pair(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_bevel_gear_pair", {**kwargs})

class test_bevel_gear(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_bevel_gear", {**kwargs})

class bevel_gear_pair(OpenSCADObject):
    def __init__(self, gear1_teeth=None, gear2_teeth=None, axis_angle=None, outside_circular_pitch=None, **kwargs):
       super().__init__("bevel_gear_pair", {"gear1_teeth" : gear1_teeth, "gear2_teeth" : gear2_teeth, "axis_angle" : axis_angle, "outside_circular_pitch" : outside_circular_pitch, **kwargs})

class bevel_gear(OpenSCADObject):
    def __init__(self, number_of_teeth=None, cone_distance=None, face_width=None, outside_circular_pitch=None, pressure_angle=None, clearance=None, bore_diameter=None, gear_thickness=None, backlash=None, involute_facets=None, finish=None, **kwargs):
       super().__init__("bevel_gear", {"number_of_teeth" : number_of_teeth, "cone_distance" : cone_distance, "face_width" : face_width, "outside_circular_pitch" : outside_circular_pitch, "pressure_angle" : pressure_angle, "clearance" : clearance, "bore_diameter" : bore_diameter, "gear_thickness" : gear_thickness, "backlash" : backlash, "involute_facets" : involute_facets, "finish" : finish, **kwargs})

class involute_bevel_gear_tooth(OpenSCADObject):
    def __init__(self, back_cone_radius=None, root_radius=None, base_radius=None, outer_radius=None, pitch_apex=None, cone_distance=None, half_thick_angle=None, involute_facets=None, **kwargs):
       super().__init__("involute_bevel_gear_tooth", {"back_cone_radius" : back_cone_radius, "root_radius" : root_radius, "base_radius" : base_radius, "outer_radius" : outer_radius, "pitch_apex" : pitch_apex, "cone_distance" : cone_distance, "half_thick_angle" : half_thick_angle, "involute_facets" : involute_facets, **kwargs})

class gear(OpenSCADObject):
    def __init__(self, number_of_teeth=None, circular_pitch=None, diametral_pitch=None, pressure_angle=None, clearance=None, gear_thickness=None, rim_thickness=None, rim_width=None, hub_thickness=None, hub_diameter=None, spokes=None, spoke_width=None, spoke_thickness=None, spoke_square=None, centered_gear=None, centered_hub=None, bore_diameter=None, circles=None, circle_diameter=None, backlash=None, twist=None, involute_facets=None, flat=None, **kwargs):
       super().__init__("gear", {"number_of_teeth" : number_of_teeth, "circular_pitch" : circular_pitch, "diametral_pitch" : diametral_pitch, "pressure_angle" : pressure_angle, "clearance" : clearance, "gear_thickness" : gear_thickness, "rim_thickness" : rim_thickness, "rim_width" : rim_width, "hub_thickness" : hub_thickness, "hub_diameter" : hub_diameter, "spokes" : spokes, "spoke_width" : spoke_width, "spoke_thickness" : spoke_thickness, "spoke_square" : spoke_square, "centered_gear" : centered_gear, "centered_hub" : centered_hub, "bore_diameter" : bore_diameter, "circles" : circles, "circle_diameter" : circle_diameter, "backlash" : backlash, "twist" : twist, "involute_facets" : involute_facets, "flat" : flat, **kwargs})

class rack(OpenSCADObject):
    def __init__(self, number_of_teeth=None, circular_pitch=None, diametral_pitch=None, pressure_angle=None, clearance=None, rim_thickness=None, rim_width=None, flat=None, **kwargs):
       super().__init__("rack", {"number_of_teeth" : number_of_teeth, "circular_pitch" : circular_pitch, "diametral_pitch" : diametral_pitch, "pressure_angle" : pressure_angle, "clearance" : clearance, "rim_thickness" : rim_thickness, "rim_width" : rim_width, "flat" : flat, **kwargs})

class linear_extrude_flat_option(OpenSCADObject):
    def __init__(self, flat=None, height=None, center=None, convexity=None, twist=None, **kwargs):
       super().__init__("linear_extrude_flat_option", {"flat" : flat, "height" : height, "center" : center, "convexity" : convexity, "twist" : twist, **kwargs})

class gear_shape(OpenSCADObject):
    def __init__(self, number_of_teeth=None, pitch_radius=None, root_radius=None, base_radius=None, outer_radius=None, half_thick_angle=None, involute_facets=None, **kwargs):
       super().__init__("gear_shape", {"number_of_teeth" : number_of_teeth, "pitch_radius" : pitch_radius, "root_radius" : root_radius, "base_radius" : base_radius, "outer_radius" : outer_radius, "half_thick_angle" : half_thick_angle, "involute_facets" : involute_facets, **kwargs})

class involute_gear_tooth(OpenSCADObject):
    def __init__(self, pitch_radius=None, root_radius=None, base_radius=None, outer_radius=None, half_thick_angle=None, involute_facets=None, **kwargs):
       super().__init__("involute_gear_tooth", {"pitch_radius" : pitch_radius, "root_radius" : root_radius, "base_radius" : base_radius, "outer_radius" : outer_radius, "half_thick_angle" : half_thick_angle, "involute_facets" : involute_facets, **kwargs})

class test_gears(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_gears", {**kwargs})

class meshing_double_helix(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("meshing_double_helix", {**kwargs})

class test_double_helix_gear(OpenSCADObject):
    def __init__(self, teeth=None, circles=None, **kwargs):
       super().__init__("test_double_helix_gear", {"teeth" : teeth, "circles" : circles, **kwargs})

class test_backlash(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_backlash", {**kwargs})

class involute_intersect_angle(OpenSCADObject):
    def __init__(self, base_radius=None, radius=None, **kwargs):
       super().__init__("involute_intersect_angle", {"base_radius" : base_radius, "radius" : radius, **kwargs})

class rotated_involute(OpenSCADObject):
    def __init__(self, rotate=None, base_radius=None, involute_angle=None, **kwargs):
       super().__init__("rotated_involute", {"rotate" : rotate, "base_radius" : base_radius, "involute_angle" : involute_angle, **kwargs})

class mirror_point(OpenSCADObject):
    def __init__(self, coord=None, **kwargs):
       super().__init__("mirror_point", {"coord" : coord, **kwargs})

class rotate_point(OpenSCADObject):
    def __init__(self, rotate=None, coord=None, **kwargs):
       super().__init__("rotate_point", {"rotate" : rotate, "coord" : coord, **kwargs})

class involute(OpenSCADObject):
    def __init__(self, base_radius=None, involute_angle=None, **kwargs):
       super().__init__("involute", {"base_radius" : base_radius, "involute_angle" : involute_angle, **kwargs})

