from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/libtriangles.scad'}", use_not_include=False)

class rightpyramid(OpenSCADObject):
    def __init__(self, rightpyramidx=None, rightpyramidy=None, rightpyramidz=None, **kwargs):
       super().__init__("rightpyramid", {"rightpyramidx" : rightpyramidx, "rightpyramidy" : rightpyramidy, "rightpyramidz" : rightpyramidz, **kwargs})

class cornerpyramid(OpenSCADObject):
    def __init__(self, cornerpyramidx=None, cornerpyramidy=None, cornerpyramidz=None, **kwargs):
       super().__init__("cornerpyramid", {"cornerpyramidx" : cornerpyramidx, "cornerpyramidy" : cornerpyramidy, "cornerpyramidz" : cornerpyramidz, **kwargs})

class eqlpyramid(OpenSCADObject):
    def __init__(self, eqlpyramidx=None, eqlpyramidy=None, eqlpyramidz=None, **kwargs):
       super().__init__("eqlpyramid", {"eqlpyramidx" : eqlpyramidx, "eqlpyramidy" : eqlpyramidy, "eqlpyramidz" : eqlpyramidz, **kwargs})

class rightprism(OpenSCADObject):
    def __init__(self, rightprismx=None, rightprismy=None, rightprismz=None, **kwargs):
       super().__init__("rightprism", {"rightprismx" : rightprismx, "rightprismy" : rightprismy, "rightprismz" : rightprismz, **kwargs})

class eqlprism(OpenSCADObject):
    def __init__(self, rightprismx=None, rightprismy=None, rightprismz=None, **kwargs):
       super().__init__("eqlprism", {"rightprismx" : rightprismx, "rightprismy" : rightprismy, "rightprismz" : rightprismz, **kwargs})

