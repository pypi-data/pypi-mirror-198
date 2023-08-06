from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/phillips_drive.scad'}", use_not_include=True)

class phillips_drive(OpenSCADObject):
    def __init__(self, size=None, shaft=None, l=None, orient=None, align=None, **kwargs):
       super().__init__("phillips_drive", {"size" : size, "shaft" : shaft, "l" : l, "orient" : orient, "align" : align, **kwargs})

