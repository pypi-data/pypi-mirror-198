from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*2) / 'scad/MCAD/bitmap/height_map.scad'}", use_not_include=False)

block_size = OpenSCADConstant('block_size')
height = OpenSCADConstant('height')
row_size = OpenSCADConstant('row_size')
bitmap = OpenSCADConstant('bitmap')
