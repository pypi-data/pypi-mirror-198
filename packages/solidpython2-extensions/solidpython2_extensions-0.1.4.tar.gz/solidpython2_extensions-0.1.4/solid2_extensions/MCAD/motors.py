from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/motors.scad'}", use_not_include=False)

class stepper_motor_mount(OpenSCADObject):
    def __init__(self, nema_standard=None, slide_distance=None, mochup=None, tolerance=None, **kwargs):
       super().__init__("stepper_motor_mount", {"nema_standard" : nema_standard, "slide_distance" : slide_distance, "mochup" : mochup, "tolerance" : tolerance, **kwargs})

class _stepper_motor_mount(OpenSCADObject):
    def __init__(self, motor_shaft_diameter=None, motor_shaft_length=None, pilot_diameter=None, pilot_length=None, mounting_bolt_circle=None, bolt_hole_size=None, bolt_hole_distance=None, slide_distance=None, motor_length=None, mochup=None, tolerance=None, **kwargs):
       super().__init__("_stepper_motor_mount", {"motor_shaft_diameter" : motor_shaft_diameter, "motor_shaft_length" : motor_shaft_length, "pilot_diameter" : pilot_diameter, "pilot_length" : pilot_length, "mounting_bolt_circle" : mounting_bolt_circle, "bolt_hole_size" : bolt_hole_size, "bolt_hole_distance" : bolt_hole_distance, "slide_distance" : slide_distance, "motor_length" : motor_length, "mochup" : mochup, "tolerance" : tolerance, **kwargs})

