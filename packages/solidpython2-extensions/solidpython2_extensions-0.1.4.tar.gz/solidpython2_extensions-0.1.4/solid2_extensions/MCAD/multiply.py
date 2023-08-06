from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/multiply.scad'}", use_not_include=False)

class spin(OpenSCADObject):
    def __init__(self, no=None, angle=None, axis=None, strict=None, **kwargs):
       super().__init__("spin", {"no" : no, "angle" : angle, "axis" : axis, "strict" : strict, **kwargs})

class duplicate(OpenSCADObject):
    def __init__(self, axis=None, **kwargs):
       super().__init__("duplicate", {"axis" : axis, **kwargs})

class linear_multiply(OpenSCADObject):
    def __init__(self, no=None, separation=None, axis=None, **kwargs):
       super().__init__("linear_multiply", {"no" : no, "separation" : separation, "axis" : axis, **kwargs})

