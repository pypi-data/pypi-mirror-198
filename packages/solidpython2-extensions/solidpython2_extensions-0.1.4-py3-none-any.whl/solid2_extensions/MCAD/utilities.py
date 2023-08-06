from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/utilities.scad'}", use_not_include=False)

CENTER = OpenSCADConstant('CENTER')
LEFT = OpenSCADConstant('LEFT')
RIGHT = OpenSCADConstant('RIGHT')
TOP = OpenSCADConstant('TOP')
BOTTOM = OpenSCADConstant('BOTTOM')
FlatCap = OpenSCADConstant('FlatCap')
ExtendedCap = OpenSCADConstant('ExtendedCap')
CutCap = OpenSCADConstant('CutCap')
class fromTo(OpenSCADObject):
    def __init__(self, _from=None, to=None, size=None, align=None, material=None, name=None, endExtras=None, endCaps=None, rotation=None, printString=None, **kwargs):
       super().__init__("fromTo", {"_from" : _from, "to" : to, "size" : size, "align" : align, "material" : material, "name" : name, "endExtras" : endExtras, "endCaps" : endCaps, "rotation" : rotation, "printString" : printString, **kwargs})

class part(OpenSCADObject):
    def __init__(self, name=None, **kwargs):
       super().__init__("part", {"name" : name, **kwargs})

class distance(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("distance", {"a" : a, "b" : b, **kwargs})

class length2(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("length2", {"a" : a, **kwargs})

class normalized(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("normalized", {"a" : a, **kwargs})

class normalized_axis(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("normalized_axis", {"a" : a, **kwargs})

class angleOfNormalizedVector(OpenSCADObject):
    def __init__(self, n=None, **kwargs):
       super().__init__("angleOfNormalizedVector", {"n" : n, **kwargs})

class angle(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("angle", {"v" : v, **kwargs})

class angleBetweenTwoPoints(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("angleBetweenTwoPoints", {"a" : a, "b" : b, **kwargs})

