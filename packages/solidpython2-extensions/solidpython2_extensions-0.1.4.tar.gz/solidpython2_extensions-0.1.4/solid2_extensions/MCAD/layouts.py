from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/layouts.scad'}", use_not_include=False)

class list(OpenSCADObject):
    def __init__(self, iHeight=None, **kwargs):
       super().__init__("list", {"iHeight" : iHeight, **kwargs})

class grid(OpenSCADObject):
    def __init__(self, iWidth=None, iHeight=None, inYDir=None, limit=None, **kwargs):
       super().__init__("grid", {"iWidth" : iWidth, "iHeight" : iHeight, "inYDir" : inYDir, "limit" : limit, **kwargs})

