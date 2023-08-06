from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*2) / 'scad/MCAD/bitmap/name_tag.scad'}", use_not_include=False)

class name_tag(OpenSCADObject):
    def __init__(self, chars=None, block_size=None, height=None, key_ring_hole=None, **kwargs):
       super().__init__("name_tag", {"chars" : chars, "block_size" : block_size, "height" : height, "key_ring_hole" : key_ring_hole, **kwargs})

