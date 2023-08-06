from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/2Dshapes.scad'}", use_not_include=False)

class example2DShapes(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("example2DShapes", {**kwargs})

class complexRoundSquare(OpenSCADObject):
    def __init__(self, size=None, rads1=None, rads2=None, rads3=None, rads4=None, center=None, **kwargs):
       super().__init__("complexRoundSquare", {"size" : size, "rads1" : rads1, "rads2" : rads2, "rads3" : rads3, "rads4" : rads4, "center" : center, **kwargs})

class roundedSquare(OpenSCADObject):
    def __init__(self, pos=None, r=None, **kwargs):
       super().__init__("roundedSquare", {"pos" : pos, "r" : r, **kwargs})

class ngon(OpenSCADObject):
    def __init__(self, sides=None, radius=None, center=None, **kwargs):
       super().__init__("ngon", {"sides" : sides, "radius" : radius, "center" : center, **kwargs})

class ellipsePart(OpenSCADObject):
    def __init__(self, width=None, height=None, numQuarters=None, **kwargs):
       super().__init__("ellipsePart", {"width" : width, "height" : height, "numQuarters" : numQuarters, **kwargs})

class donutSlice(OpenSCADObject):
    def __init__(self, innerSize=None, outerSize=None, start_angle=None, end_angle=None, **kwargs):
       super().__init__("donutSlice", {"innerSize" : innerSize, "outerSize" : outerSize, "start_angle" : start_angle, "end_angle" : end_angle, **kwargs})

class pieSlice(OpenSCADObject):
    def __init__(self, size=None, start_angle=None, end_angle=None, **kwargs):
       super().__init__("pieSlice", {"size" : size, "start_angle" : start_angle, "end_angle" : end_angle, **kwargs})

class ellipse(OpenSCADObject):
    def __init__(self, width=None, height=None, **kwargs):
       super().__init__("ellipse", {"width" : width, "height" : height, **kwargs})

