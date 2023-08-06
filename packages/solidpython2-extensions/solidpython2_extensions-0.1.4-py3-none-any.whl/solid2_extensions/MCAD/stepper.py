from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/stepper.scad'}", use_not_include=False)

NemaModel = OpenSCADConstant('NemaModel')
NemaLengthShort = OpenSCADConstant('NemaLengthShort')
NemaLengthMedium = OpenSCADConstant('NemaLengthMedium')
NemaLengthLong = OpenSCADConstant('NemaLengthLong')
NemaSideSize = OpenSCADConstant('NemaSideSize')
NemaDistanceBetweenMountingHoles = OpenSCADConstant('NemaDistanceBetweenMountingHoles')
NemaMountingHoleDiameter = OpenSCADConstant('NemaMountingHoleDiameter')
NemaMountingHoleDepth = OpenSCADConstant('NemaMountingHoleDepth')
NemaMountingHoleLip = OpenSCADConstant('NemaMountingHoleLip')
NemaMountingHoleCutoutRadius = OpenSCADConstant('NemaMountingHoleCutoutRadius')
NemaEdgeRoundingRadius = OpenSCADConstant('NemaEdgeRoundingRadius')
NemaRoundExtrusionDiameter = OpenSCADConstant('NemaRoundExtrusionDiameter')
NemaRoundExtrusionHeight = OpenSCADConstant('NemaRoundExtrusionHeight')
NemaAxleDiameter = OpenSCADConstant('NemaAxleDiameter')
NemaFrontAxleLength = OpenSCADConstant('NemaFrontAxleLength')
NemaBackAxleLength = OpenSCADConstant('NemaBackAxleLength')
NemaAxleFlatDepth = OpenSCADConstant('NemaAxleFlatDepth')
NemaAxleFlatLengthFront = OpenSCADConstant('NemaAxleFlatLengthFront')
NemaAxleFlatLengthBack = OpenSCADConstant('NemaAxleFlatLengthBack')
NemaA = OpenSCADConstant('NemaA')
NemaB = OpenSCADConstant('NemaB')
NemaC = OpenSCADConstant('NemaC')
NemaShort = OpenSCADConstant('NemaShort')
NemaMedium = OpenSCADConstant('NemaMedium')
NemaLong = OpenSCADConstant('NemaLong')
Nema08 = OpenSCADConstant('Nema08')
Nema11 = OpenSCADConstant('Nema11')
Nema14 = OpenSCADConstant('Nema14')
Nema17 = OpenSCADConstant('Nema17')
Nema23 = OpenSCADConstant('Nema23')
Nema34 = OpenSCADConstant('Nema34')
class nema_demo(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("nema_demo", {**kwargs})

class motor(OpenSCADObject):
    def __init__(self, model=None, size=None, dualAxis=None, pos=None, orientation=None, **kwargs):
       super().__init__("motor", {"model" : model, "size" : size, "dualAxis" : dualAxis, "pos" : pos, "orientation" : orientation, **kwargs})

class roundedBox(OpenSCADObject):
    def __init__(self, size=None, edgeRadius=None, **kwargs):
       super().__init__("roundedBox", {"size" : size, "edgeRadius" : edgeRadius, **kwargs})

class motorWidth(OpenSCADObject):
    def __init__(self, model=None, **kwargs):
       super().__init__("motorWidth", {"model" : model, **kwargs})

class motorLength(OpenSCADObject):
    def __init__(self, model=None, size=None, **kwargs):
       super().__init__("motorLength", {"model" : model, "size" : size, **kwargs})

