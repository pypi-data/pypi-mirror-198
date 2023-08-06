from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*2) / 'scad/BOSL/examples/orientations.scad'}", use_not_include=True)

orientations = OpenSCADConstant('orientations')
axisdiam = OpenSCADConstant('axisdiam')
axislen = OpenSCADConstant('axislen')
axislbllen = OpenSCADConstant('axislbllen')
axiscolors = OpenSCADConstant('axiscolors')
class text3d(OpenSCADObject):
    def __init__(self, text=None, h=None, size=None, **kwargs):
       super().__init__("text3d", {"text" : text, "h" : h, "size" : size, **kwargs})

class dottedline(OpenSCADObject):
    def __init__(self, l=None, d=None, **kwargs):
       super().__init__("dottedline", {"l" : l, "d" : d, **kwargs})

class orient_cubes(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("orient_cubes", {**kwargs})

