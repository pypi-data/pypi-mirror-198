from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/color.scad'}", use_not_include=False)

class recolor(OpenSCADObject):
    def __init__(self, c=None, **kwargs):
       super().__init__("recolor", {"c" : c, **kwargs})

class color_this(OpenSCADObject):
    def __init__(self, c=None, **kwargs):
       super().__init__("color_this", {"c" : c, **kwargs})

class rainbow(OpenSCADObject):
    def __init__(self, list=None, stride=None, maxhues=None, shuffle=None, seed=None, **kwargs):
       super().__init__("rainbow", {"list" : list, "stride" : stride, "maxhues" : maxhues, "shuffle" : shuffle, "seed" : seed, **kwargs})

class hsl(OpenSCADObject):
    def __init__(self, h=None, s=None, l=None, a=None, **kwargs):
       super().__init__("hsl", {"h" : h, "s" : s, "l" : l, "a" : a, **kwargs})

class hsv(OpenSCADObject):
    def __init__(self, h=None, s=None, v=None, a=None, **kwargs):
       super().__init__("hsv", {"h" : h, "s" : s, "v" : v, "a" : a, **kwargs})

class hsl(OpenSCADObject):
    def __init__(self, h=None, s=None, l=None, a=None, **kwargs):
       super().__init__("hsl", {"h" : h, "s" : s, "l" : l, "a" : a, **kwargs})

class hsv(OpenSCADObject):
    def __init__(self, h=None, s=None, v=None, a=None, **kwargs):
       super().__init__("hsv", {"h" : h, "s" : s, "v" : v, "a" : a, **kwargs})

