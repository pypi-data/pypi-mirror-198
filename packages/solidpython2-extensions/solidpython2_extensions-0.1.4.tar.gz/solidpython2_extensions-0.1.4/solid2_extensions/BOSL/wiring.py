from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/wiring.scad'}", use_not_include=True)

class wiring(OpenSCADObject):
    def __init__(self, path=None, wires=None, wirediam=None, fillet=None, wirenum=None, bezsteps=None, **kwargs):
       super().__init__("wiring", {"path" : path, "wires" : wires, "wirediam" : wirediam, "fillet" : fillet, "wirenum" : wirenum, "bezsteps" : bezsteps, **kwargs})

class hex_offset_ring(OpenSCADObject):
    def __init__(self, d=None, lev=None, **kwargs):
       super().__init__("hex_offset_ring", {"d" : d, "lev" : lev, **kwargs})

class hex_offsets(OpenSCADObject):
    def __init__(self, n=None, d=None, lev=None, arr=None, **kwargs):
       super().__init__("hex_offsets", {"n" : n, "d" : d, "lev" : lev, "arr" : arr, **kwargs})

