from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*2) / 'scad/BOSL/examples/bezier_patches.scad'}", use_not_include=True)

class CR_cube(OpenSCADObject):
    def __init__(self, size=None, r=None, splinesteps=None, cheat=None, **kwargs):
       super().__init__("CR_cube", {"size" : size, "r" : r, "splinesteps" : splinesteps, "cheat" : cheat, **kwargs})

class CR_corner(OpenSCADObject):
    def __init__(self, size=None, orient=None, trans=None, **kwargs):
       super().__init__("CR_corner", {"size" : size, "orient" : orient, "trans" : trans, **kwargs})

class CR_edge(OpenSCADObject):
    def __init__(self, size=None, orient=None, trans=None, **kwargs):
       super().__init__("CR_edge", {"size" : size, "orient" : orient, "trans" : trans, **kwargs})

