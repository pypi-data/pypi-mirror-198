from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/transformations.scad'}", use_not_include=False)

class local_scale(OpenSCADObject):
    def __init__(self, v=None, reference=None, **kwargs):
       super().__init__("local_scale", {"v" : v, "reference" : reference, **kwargs})

