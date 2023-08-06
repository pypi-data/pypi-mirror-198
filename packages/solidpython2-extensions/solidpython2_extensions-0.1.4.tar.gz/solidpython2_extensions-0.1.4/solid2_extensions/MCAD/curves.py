from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/curves.scad'}", use_not_include=False)

class b(OpenSCADObject):
    def __init__(self, pitch=None, **kwargs):
       super().__init__("b", {"pitch" : pitch, **kwargs})

class t(OpenSCADObject):
    def __init__(self, pitch=None, z=None, **kwargs):
       super().__init__("t", {"pitch" : pitch, "z" : z, **kwargs})

class helix_curve(OpenSCADObject):
    def __init__(self, pitch=None, radius=None, z=None, **kwargs):
       super().__init__("helix_curve", {"pitch" : pitch, "radius" : radius, "z" : z, **kwargs})

