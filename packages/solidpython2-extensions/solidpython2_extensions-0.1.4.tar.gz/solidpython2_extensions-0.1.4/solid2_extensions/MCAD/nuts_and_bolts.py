from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/nuts_and_bolts.scad'}", use_not_include=False)

MM = OpenSCADConstant('MM')
INCH = OpenSCADConstant('INCH')
METRIC_NUT_AC_WIDTHS = OpenSCADConstant('METRIC_NUT_AC_WIDTHS')
METRIC_NUT_THICKNESS = OpenSCADConstant('METRIC_NUT_THICKNESS')
COARSE_THREAD_METRIC_BOLT_MAJOR_DIAMETERS = OpenSCADConstant('COARSE_THREAD_METRIC_BOLT_MAJOR_DIAMETERS')
COURSE_METRIC_BOLT_MAJOR_THREAD_DIAMETERS = OpenSCADConstant('COURSE_METRIC_BOLT_MAJOR_THREAD_DIAMETERS')
METRIC_BOLT_CAP_DIAMETERS = OpenSCADConstant('METRIC_BOLT_CAP_DIAMETERS')
class SKIPtestNutsAndBolts(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("SKIPtestNutsAndBolts", {**kwargs})

class nutHole(OpenSCADObject):
    def __init__(self, size=None, units=None, tolerance=None, proj=None, **kwargs):
       super().__init__("nutHole", {"size" : size, "units" : units, "tolerance" : tolerance, "proj" : proj, **kwargs})

class boltHole(OpenSCADObject):
    def __init__(self, size=None, units=None, length=None, tolerance=None, proj=None, **kwargs):
       super().__init__("boltHole", {"size" : size, "units" : units, "length" : length, "tolerance" : tolerance, "proj" : proj, **kwargs})

