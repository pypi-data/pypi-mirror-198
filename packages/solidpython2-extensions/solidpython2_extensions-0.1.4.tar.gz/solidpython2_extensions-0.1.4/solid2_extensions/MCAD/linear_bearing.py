from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/linear_bearing.scad'}", use_not_include=False)

LINEAR_BEARING_dr = OpenSCADConstant('LINEAR_BEARING_dr')
LINEAR_BEARING_D = OpenSCADConstant('LINEAR_BEARING_D')
LINEAR_BEARING_L = OpenSCADConstant('LINEAR_BEARING_L')
LINEAR_BEARING_B = OpenSCADConstant('LINEAR_BEARING_B')
LINEAR_BEARING_D1 = OpenSCADConstant('LINEAR_BEARING_D1')
LINEAR_BEARING_W = OpenSCADConstant('LINEAR_BEARING_W')
LinearBearing = OpenSCADConstant('LinearBearing')
class linearBearing(OpenSCADObject):
    def __init__(self, pos=None, angle=None, model=None, material=None, sideMaterial=None, **kwargs):
       super().__init__("linearBearing", {"pos" : pos, "angle" : angle, "model" : model, "material" : material, "sideMaterial" : sideMaterial, **kwargs})

class linearBearingDimensions(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("linearBearingDimensions", {"model" : model, **kwargs})

class linearBearing_dr(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("linearBearing_dr", {"model" : model, **kwargs})

class linearBearing_D(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("linearBearing_D", {"model" : model, **kwargs})

class linearBearing_L(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("linearBearing_L", {"model" : model, **kwargs})

class linearBearing_B(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("linearBearing_B", {"model" : model, **kwargs})

class linearBearing_D1(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("linearBearing_D1", {"model" : model, **kwargs})

class linearBearing_W(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("linearBearing_W", {"model" : model, **kwargs})

