from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/lego_compatibility.scad'}", use_not_include=False)

knob_diameter = OpenSCADConstant('knob_diameter')
knob_height = OpenSCADConstant('knob_height')
knob_spacing = OpenSCADConstant('knob_spacing')
wall_thickness = OpenSCADConstant('wall_thickness')
roof_thickness = OpenSCADConstant('roof_thickness')
block_height = OpenSCADConstant('block_height')
pin_diameter = OpenSCADConstant('pin_diameter')
post_diameter = OpenSCADConstant('post_diameter')
reinforcing_width = OpenSCADConstant('reinforcing_width')
axle_spline_width = OpenSCADConstant('axle_spline_width')
axle_diameter = OpenSCADConstant('axle_diameter')
cylinder_precision = OpenSCADConstant('cylinder_precision')
class block(OpenSCADObject):
    def __init__(self, width=None, length=None, height=None, axle_hole=None, reinforcement=None, hollow_knob=None, flat_top=None, circular_hole=None, solid_bottom=None, center=None, **kwargs):
       super().__init__("block", {"width" : width, "length" : length, "height" : height, "axle_hole" : axle_hole, "reinforcement" : reinforcement, "hollow_knob" : hollow_knob, "flat_top" : flat_top, "circular_hole" : circular_hole, "solid_bottom" : solid_bottom, "center" : center, **kwargs})

class post(OpenSCADObject):
    def __init__(self, height=None, **kwargs):
       super().__init__("post", {"height" : height, **kwargs})

class reinforcement(OpenSCADObject):
    def __init__(self, height=None, **kwargs):
       super().__init__("reinforcement", {"height" : height, **kwargs})

class axle(OpenSCADObject):
    def __init__(self, height=None, **kwargs):
       super().__init__("axle", {"height" : height, **kwargs})

