from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/materials.scad'}", use_not_include=False)

Oak = OpenSCADConstant('Oak')
Pine = OpenSCADConstant('Pine')
Birch = OpenSCADConstant('Birch')
FiberBoard = OpenSCADConstant('FiberBoard')
BlackPaint = OpenSCADConstant('BlackPaint')
Iron = OpenSCADConstant('Iron')
Steel = OpenSCADConstant('Steel')
Stainless = OpenSCADConstant('Stainless')
Aluminum = OpenSCADConstant('Aluminum')
Brass = OpenSCADConstant('Brass')
Transparent = OpenSCADConstant('Transparent')
class color_demo(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("color_demo", {**kwargs})

class colorTest(OpenSCADObject):
    def __init__(self, col=None, row=None, c=None, **kwargs):
       super().__init__("colorTest", {"col" : col, "row" : row, "c" : c, **kwargs})

