from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/polyholes.scad'}", use_not_include=False)

class polyhole(OpenSCADObject):
    def __init__(self, h=None, d=None, r=None, center=None, **kwargs):
       super().__init__("polyhole", {"h" : h, "d" : d, "r" : r, "center" : center, **kwargs})

class test_polyhole(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_polyhole", {**kwargs})

