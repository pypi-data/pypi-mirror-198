from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/boxes.scad'}", use_not_include=False)

class roundedBox(OpenSCADObject):
    def __init__(self, size=None, radius=None, sidesonly=None, **kwargs):
       super().__init__("roundedBox", {"size" : size, "radius" : radius, "sidesonly" : sidesonly, **kwargs})

class roundedCube(OpenSCADObject):
    def __init__(self, size=None, r=None, sidesonly=None, center=None, **kwargs):
       super().__init__("roundedCube", {"size" : size, "r" : r, "sidesonly" : sidesonly, "center" : center, **kwargs})

