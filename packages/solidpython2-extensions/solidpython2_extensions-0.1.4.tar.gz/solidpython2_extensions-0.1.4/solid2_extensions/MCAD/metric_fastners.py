from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/metric_fastners.scad'}", use_not_include=False)

_fn = OpenSCADConstant('_fn')
apply_chamfer = OpenSCADConstant('apply_chamfer')
class cap_bolt(OpenSCADObject):
    def __init__(self, dia=None, len=None, **kwargs):
       super().__init__("cap_bolt", {"dia" : dia, "len" : len, **kwargs})

class csk_bolt(OpenSCADObject):
    def __init__(self, dia=None, len=None, **kwargs):
       super().__init__("csk_bolt", {"dia" : dia, "len" : len, **kwargs})

class washer(OpenSCADObject):
    def __init__(self, dia=None, **kwargs):
       super().__init__("washer", {"dia" : dia, **kwargs})

class flat_nut(OpenSCADObject):
    def __init__(self, dia=None, **kwargs):
       super().__init__("flat_nut", {"dia" : dia, **kwargs})

class bolt(OpenSCADObject):
    def __init__(self, dia=None, len=None, **kwargs):
       super().__init__("bolt", {"dia" : dia, "len" : len, **kwargs})

class cylinder_chamfer(OpenSCADObject):
    def __init__(self, r1=None, r2=None, **kwargs):
       super().__init__("cylinder_chamfer", {"r1" : r1, "r2" : r2, **kwargs})

class chamfer(OpenSCADObject):
    def __init__(self, len=None, r=None, **kwargs):
       super().__init__("chamfer", {"len" : len, "r" : r, **kwargs})

