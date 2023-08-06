from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/math.scad'}", use_not_include=False)

class deg(OpenSCADObject):
    def __init__(self, angle=None, **kwargs):
       super().__init__("deg", {"angle" : angle, **kwargs})

