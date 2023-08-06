from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/servos.scad'}", use_not_include=False)

class towerprosg90(OpenSCADObject):
    def __init__(self, position=None, rotation=None, screws=None, axle_length=None, cables=None, **kwargs):
       super().__init__("towerprosg90", {"position" : position, "rotation" : rotation, "screws" : screws, "axle_length" : axle_length, "cables" : cables, **kwargs})

class alignds420(OpenSCADObject):
    def __init__(self, position=None, rotation=None, screws=None, axle_lenght=None, **kwargs):
       super().__init__("alignds420", {"position" : position, "rotation" : rotation, "screws" : screws, "axle_lenght" : axle_lenght, **kwargs})

class futabas3003(OpenSCADObject):
    def __init__(self, position=None, rotation=None, **kwargs):
       super().__init__("futabas3003", {"position" : position, "rotation" : rotation, **kwargs})

class test_alignds420(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_alignds420", {**kwargs})

