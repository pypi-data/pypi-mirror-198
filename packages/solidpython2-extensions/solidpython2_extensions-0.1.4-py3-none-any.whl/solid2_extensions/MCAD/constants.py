from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/constants.scad'}", use_not_include=False)

TAU = OpenSCADConstant('TAU')
PI = OpenSCADConstant('PI')
mm_per_inch = OpenSCADConstant('mm_per_inch')
