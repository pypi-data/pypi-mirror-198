from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/teardrop.scad'}", use_not_include=False)

class teardrop(OpenSCADObject):
    def __init__(self, radius=None, length=None, angle=None, **kwargs):
       super().__init__("teardrop", {"radius" : radius, "length" : length, "angle" : angle, **kwargs})

class flat_teardrop(OpenSCADObject):
    def __init__(self, radius=None, length=None, angle=None, **kwargs):
       super().__init__("flat_teardrop", {"radius" : radius, "length" : length, "angle" : angle, **kwargs})

class test_teardrop(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_teardrop", {**kwargs})

