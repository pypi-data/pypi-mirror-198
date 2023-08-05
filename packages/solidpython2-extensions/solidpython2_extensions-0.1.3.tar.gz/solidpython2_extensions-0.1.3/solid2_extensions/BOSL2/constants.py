from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/constants.scad'}", use_not_include=False)

_UNDEF = OpenSCADConstant('_UNDEF')
INCH = OpenSCADConstant('INCH')
LEFT = OpenSCADConstant('LEFT')
RIGHT = OpenSCADConstant('RIGHT')
FRONT = OpenSCADConstant('FRONT')
FWD = OpenSCADConstant('FWD')
FORWARD = OpenSCADConstant('FORWARD')
BACK = OpenSCADConstant('BACK')
BOTTOM = OpenSCADConstant('BOTTOM')
BOT = OpenSCADConstant('BOT')
DOWN = OpenSCADConstant('DOWN')
TOP = OpenSCADConstant('TOP')
UP = OpenSCADConstant('UP')
CENTER = OpenSCADConstant('CENTER')
CTR = OpenSCADConstant('CTR')
CENTRE = OpenSCADConstant('CENTRE')
SEGMENT = OpenSCADConstant('SEGMENT')
RAY = OpenSCADConstant('RAY')
LINE = OpenSCADConstant('LINE')
IDENT = OpenSCADConstant('IDENT')
class get_slop(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("get_slop", {**kwargs})

