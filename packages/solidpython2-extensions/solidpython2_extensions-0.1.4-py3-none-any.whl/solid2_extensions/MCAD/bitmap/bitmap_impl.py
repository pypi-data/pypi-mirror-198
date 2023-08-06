from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*2) / 'scad/MCAD/bitmap/bitmap.scad'}", use_not_include=False)

class bitmap(OpenSCADObject):
    def __init__(self, bitmap=None, block_size=None, height=None, row_size=None, **kwargs):
       super().__init__("bitmap", {"bitmap" : bitmap, "block_size" : block_size, "height" : height, "row_size" : row_size, **kwargs})

class _8bit_char(OpenSCADObject):
    def __init__(self, char=None, block_size=None, height=None, include_base=None, **kwargs):
       super().__init__("_8bit_char", {"char" : char, "block_size" : block_size, "height" : height, "include_base" : include_base, **kwargs})

class _8bit_str(OpenSCADObject):
    def __init__(self, chars=None, char_count=None, block_size=None, height=None, **kwargs):
       super().__init__("_8bit_str", {"chars" : chars, "char_count" : char_count, "block_size" : block_size, "height" : height, **kwargs})

