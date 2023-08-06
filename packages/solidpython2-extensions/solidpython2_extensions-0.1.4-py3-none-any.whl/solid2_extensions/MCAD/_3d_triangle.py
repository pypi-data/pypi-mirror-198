from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/3d_triangle.scad'}", use_not_include=False)

class _3dtri_draw(OpenSCADObject):
    def __init__(self, Acord=None, Bcord=None, Ccord=None, h=None, **kwargs):
       super().__init__("_3dtri_draw", {"Acord" : Acord, "Bcord" : Bcord, "Ccord" : Ccord, "h" : h, **kwargs})

class _3dtri_rnd_draw(OpenSCADObject):
    def __init__(self, Acord=None, Bcord=None, Ccord=None, h=None, r=None, **kwargs):
       super().__init__("_3dtri_rnd_draw", {"Acord" : Acord, "Bcord" : Bcord, "Ccord" : Ccord, "h" : h, "r" : r, **kwargs})

class _3dtri_sides2coord(OpenSCADObject):
    def __init__(self, a=None, b=None, c=None, **kwargs):
       super().__init__("_3dtri_sides2coord", {"a" : a, "b" : b, "c" : c, **kwargs})

class _3dtri_centerOfGravityCoord(OpenSCADObject):
    def __init__(self, Acord=None, Bcord=None, Ccord=None, **kwargs):
       super().__init__("_3dtri_centerOfGravityCoord", {"Acord" : Acord, "Bcord" : Bcord, "Ccord" : Ccord, **kwargs})

class _3dtri_centerOfcircumcircle(OpenSCADObject):
    def __init__(self, Acord=None, Bcord=None, Ccord=None, **kwargs):
       super().__init__("_3dtri_centerOfcircumcircle", {"Acord" : Acord, "Bcord" : Bcord, "Ccord" : Ccord, **kwargs})

class _3dtri_radiusOfcircumcircle(OpenSCADObject):
    def __init__(self, Vcord=None, CCcord=None, R=None, **kwargs):
       super().__init__("_3dtri_radiusOfcircumcircle", {"Vcord" : Vcord, "CCcord" : CCcord, "R" : R, **kwargs})

class _3dtri_radiusOfIn_circle(OpenSCADObject):
    def __init__(self, Acord=None, Bcord=None, Ccord=None, **kwargs):
       super().__init__("_3dtri_radiusOfIn_circle", {"Acord" : Acord, "Bcord" : Bcord, "Ccord" : Ccord, **kwargs})

class _3dtri_centerOfIn_circle(OpenSCADObject):
    def __init__(self, Acord=None, Bcord=None, Ccord=None, r=None, **kwargs):
       super().__init__("_3dtri_centerOfIn_circle", {"Acord" : Acord, "Bcord" : Bcord, "Ccord" : Ccord, "r" : r, **kwargs})

