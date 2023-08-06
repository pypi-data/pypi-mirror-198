from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/array.scad'}", use_not_include=False)

class Cubic_and_Radial_Array_Test(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("Cubic_and_Radial_Array_Test", {**kwargs})

class Cubic_Array(OpenSCADObject):
    def __init__(self, sx=None, sy=None, sz=None, nx=None, ny=None, nz=None, center=None, **kwargs):
       super().__init__("Cubic_Array", {"sx" : sx, "sy" : sy, "sz" : sz, "nx" : nx, "ny" : ny, "nz" : nz, "center" : center, **kwargs})

class Radial_Array(OpenSCADObject):
    def __init__(self, a=None, n=None, r=None, **kwargs):
       super().__init__("Radial_Array", {"a" : a, "n" : n, "r" : r, **kwargs})

