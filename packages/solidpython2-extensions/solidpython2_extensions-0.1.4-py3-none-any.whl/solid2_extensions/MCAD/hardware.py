from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/hardware.scad'}", use_not_include=False)

rodsize = OpenSCADConstant('rodsize')
xaxis = OpenSCADConstant('xaxis')
yaxis = OpenSCADConstant('yaxis')
screwsize = OpenSCADConstant('screwsize')
bearingsize = OpenSCADConstant('bearingsize')
bearingwidth = OpenSCADConstant('bearingwidth')
rodpitch = OpenSCADConstant('rodpitch')
rodnutsize = OpenSCADConstant('rodnutsize')
rodnutdiameter = OpenSCADConstant('rodnutdiameter')
rodwashersize = OpenSCADConstant('rodwashersize')
rodwasherdiameter = OpenSCADConstant('rodwasherdiameter')
screwpitch = OpenSCADConstant('screwpitch')
nutsize = OpenSCADConstant('nutsize')
nutdiameter = OpenSCADConstant('nutdiameter')
washersize = OpenSCADConstant('washersize')
washerdiameter = OpenSCADConstant('washerdiameter')
partthick = OpenSCADConstant('partthick')
vertexrodspace = OpenSCADConstant('vertexrodspace')
c = OpenSCADConstant('c')
rodendoffset = OpenSCADConstant('rodendoffset')
vertexoffset = OpenSCADConstant('vertexoffset')
renderrodthreads = OpenSCADConstant('renderrodthreads')
renderscrewthreads = OpenSCADConstant('renderscrewthreads')
fn = OpenSCADConstant('fn')
class rod(OpenSCADObject):
    def __init__(self, length=None, threaded=None, **kwargs):
       super().__init__("rod", {"length" : length, "threaded" : threaded, **kwargs})

class screw(OpenSCADObject):
    def __init__(self, length=None, nutpos=None, washer=None, bearingpos=None, **kwargs):
       super().__init__("screw", {"length" : length, "nutpos" : nutpos, "washer" : washer, "bearingpos" : bearingpos, **kwargs})

class bearing(OpenSCADObject):
    def __init__(self, position=None, **kwargs):
       super().__init__("bearing", {"position" : position, **kwargs})

class nut(OpenSCADObject):
    def __init__(self, position=None, washer=None, **kwargs):
       super().__init__("nut", {"position" : position, "washer" : washer, **kwargs})

class washer(OpenSCADObject):
    def __init__(self, position=None, **kwargs):
       super().__init__("washer", {"position" : position, **kwargs})

class rodnut(OpenSCADObject):
    def __init__(self, position=None, washer=None, **kwargs):
       super().__init__("rodnut", {"position" : position, "washer" : washer, **kwargs})

class rodwasher(OpenSCADObject):
    def __init__(self, position=None, **kwargs):
       super().__init__("rodwasher", {"position" : position, **kwargs})

