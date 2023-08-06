from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/unregular_shapes.scad'}", use_not_include=False)

class connect_squares(OpenSCADObject):
    def __init__(self, points=None, **kwargs):
       super().__init__("connect_squares", {"points" : points, **kwargs})

