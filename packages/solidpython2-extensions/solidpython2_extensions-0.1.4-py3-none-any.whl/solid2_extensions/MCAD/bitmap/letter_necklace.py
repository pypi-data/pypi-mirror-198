from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*2) / 'scad/MCAD/bitmap/letter_necklace.scad'}", use_not_include=False)

chars = OpenSCADConstant('chars')
char_count = OpenSCADConstant('char_count')
block_size = OpenSCADConstant('block_size')
height = OpenSCADConstant('height')
hole_diameter = OpenSCADConstant('hole_diameter')
matrix = OpenSCADConstant('matrix')
class _8bit_str(OpenSCADObject):
    def __init__(self, chars=None, char_count=None, block_size=None, height=None, **kwargs):
       super().__init__("_8bit_str", {"chars" : chars, "char_count" : char_count, "block_size" : block_size, "height" : height, **kwargs})

class letter(OpenSCADObject):
    def __init__(self, char=None, block_size=None, height=None, hole_diameter=None, **kwargs):
       super().__init__("letter", {"char" : char, "block_size" : block_size, "height" : height, "hole_diameter" : hole_diameter, **kwargs})

