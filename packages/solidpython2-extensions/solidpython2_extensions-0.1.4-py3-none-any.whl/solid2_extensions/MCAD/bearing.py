from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/bearing.scad'}", use_not_include=False)

BEARING_INNER_DIAMETER = OpenSCADConstant('BEARING_INNER_DIAMETER')
BEARING_OUTER_DIAMETER = OpenSCADConstant('BEARING_OUTER_DIAMETER')
BEARING_WIDTH = OpenSCADConstant('BEARING_WIDTH')
SkateBearing = OpenSCADConstant('SkateBearing')
class test_bearing(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_bearing", {**kwargs})

class test_bearing_hole(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_bearing_hole", {**kwargs})

class bearing(OpenSCADObject):
    def __init__(self, pos=None, angle=None, model=None, outline=None, material=None, sideMaterial=None, center=None, **kwargs):
       super().__init__("bearing", {"pos" : pos, "angle" : angle, "model" : model, "outline" : outline, "material" : material, "sideMaterial" : sideMaterial, "center" : center, **kwargs})

class bearingDimensions(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("bearingDimensions", {"model" : model, **kwargs})

class bearingWidth(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("bearingWidth", {"model" : model, **kwargs})

class bearingInnerDiameter(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("bearingInnerDiameter", {"model" : model, **kwargs})

class bearingOuterDiameter(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("bearingOuterDiameter", {"model" : model, **kwargs})

