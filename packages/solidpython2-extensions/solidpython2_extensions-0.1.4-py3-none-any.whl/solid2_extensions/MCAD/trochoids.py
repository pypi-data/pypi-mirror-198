from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/trochoids.scad'}", use_not_include=False)

_fn = OpenSCADConstant('_fn')
thickness = OpenSCADConstant('thickness')
R = OpenSCADConstant('R')
r = OpenSCADConstant('r')
d = OpenSCADConstant('d')
n = OpenSCADConstant('n')
alpha = OpenSCADConstant('alpha')
class epitrochoid(OpenSCADObject):
    def __init__(self, R=None, r=None, d=None, n=None, thickness=None, **kwargs):
       super().__init__("epitrochoid", {"R" : R, "r" : r, "d" : d, "n" : n, "thickness" : thickness, **kwargs})

class hypotrochoid(OpenSCADObject):
    def __init__(self, R=None, r=None, d=None, n=None, thickness=None, **kwargs):
       super().__init__("hypotrochoid", {"R" : R, "r" : r, "d" : d, "n" : n, "thickness" : thickness, **kwargs})

class epitrochoidWBore(OpenSCADObject):
    def __init__(self, R=None, r=None, d=None, n=None, p=None, thickness=None, rb=None, **kwargs):
       super().__init__("epitrochoidWBore", {"R" : R, "r" : r, "d" : d, "n" : n, "p" : p, "thickness" : thickness, "rb" : rb, **kwargs})

class epitrochoidWBoreLinear(OpenSCADObject):
    def __init__(self, R=None, r=None, d=None, n=None, p=None, thickness=None, rb=None, twist=None, **kwargs):
       super().__init__("epitrochoidWBoreLinear", {"R" : R, "r" : r, "d" : d, "n" : n, "p" : p, "thickness" : thickness, "rb" : rb, "twist" : twist, **kwargs})

class epitrochoidLinear(OpenSCADObject):
    def __init__(self, R=None, r=None, d=None, n=None, p=None, thickness=None, twist=None, **kwargs):
       super().__init__("epitrochoidLinear", {"R" : R, "r" : r, "d" : d, "n" : n, "p" : p, "thickness" : thickness, "twist" : twist, **kwargs})

class hypotrochoidWBore(OpenSCADObject):
    def __init__(self, R=None, r=None, d=None, n=None, p=None, thickness=None, rb=None, **kwargs):
       super().__init__("hypotrochoidWBore", {"R" : R, "r" : r, "d" : d, "n" : n, "p" : p, "thickness" : thickness, "rb" : rb, **kwargs})

class hypotrochoidWBoreLinear(OpenSCADObject):
    def __init__(self, R=None, r=None, d=None, n=None, p=None, thickness=None, rb=None, twist=None, **kwargs):
       super().__init__("hypotrochoidWBoreLinear", {"R" : R, "r" : r, "d" : d, "n" : n, "p" : p, "thickness" : thickness, "rb" : rb, "twist" : twist, **kwargs})

class hypotrochoidLinear(OpenSCADObject):
    def __init__(self, R=None, r=None, d=None, n=None, p=None, thickness=None, twist=None, **kwargs):
       super().__init__("hypotrochoidLinear", {"R" : R, "r" : r, "d" : d, "n" : n, "p" : p, "thickness" : thickness, "twist" : twist, **kwargs})

