from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/units.scad'}", use_not_include=False)

mm = OpenSCADConstant('mm')
cm = OpenSCADConstant('cm')
dm = OpenSCADConstant('dm')
m = OpenSCADConstant('m')
inch = OpenSCADConstant('inch')
X = OpenSCADConstant('X')
Y = OpenSCADConstant('Y')
Z = OpenSCADConstant('Z')
M3 = OpenSCADConstant('M3')
M4 = OpenSCADConstant('M4')
M5 = OpenSCADConstant('M5')
M6 = OpenSCADConstant('M6')
M8 = OpenSCADConstant('M8')
epsilon = OpenSCADConstant('epsilon')
