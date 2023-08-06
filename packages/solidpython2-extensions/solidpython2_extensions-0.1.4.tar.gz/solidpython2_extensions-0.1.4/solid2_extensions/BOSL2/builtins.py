from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/builtins.scad'}", use_not_include=False)

class _square(OpenSCADObject):
    def __init__(self, size=None, center=None, **kwargs):
       super().__init__("_square", {"size" : size, "center" : center, **kwargs})

class _circle(OpenSCADObject):
    def __init__(self, r=None, d=None, **kwargs):
       super().__init__("_circle", {"r" : r, "d" : d, **kwargs})

class _text(OpenSCADObject):
    def __init__(self, text=None, size=None, font=None, halign=None, valign=None, spacing=None, direction=None, language=None, script=None, **kwargs):
       super().__init__("_text", {"text" : text, "size" : size, "font" : font, "halign" : halign, "valign" : valign, "spacing" : spacing, "direction" : direction, "language" : language, "script" : script, **kwargs})

class _color(OpenSCADObject):
    def __init__(self, color=None, **kwargs):
       super().__init__("_color", {"color" : color, **kwargs})

class _cube(OpenSCADObject):
    def __init__(self, size=None, center=None, **kwargs):
       super().__init__("_cube", {"size" : size, "center" : center, **kwargs})

class _cylinder(OpenSCADObject):
    def __init__(self, h=None, r1=None, r2=None, center=None, r=None, d=None, d1=None, d2=None, **kwargs):
       super().__init__("_cylinder", {"h" : h, "r1" : r1, "r2" : r2, "center" : center, "r" : r, "d" : d, "d1" : d1, "d2" : d2, **kwargs})

class _sphere(OpenSCADObject):
    def __init__(self, r=None, d=None, **kwargs):
       super().__init__("_sphere", {"r" : r, "d" : d, **kwargs})

class _multmatrix(OpenSCADObject):
    def __init__(self, m=None, **kwargs):
       super().__init__("_multmatrix", {"m" : m, **kwargs})

class _translate(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_translate", {"v" : v, **kwargs})

class _rotate(OpenSCADObject):
    def __init__(self, a=None, v=None, **kwargs):
       super().__init__("_rotate", {"a" : a, "v" : v, **kwargs})

class _scale(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_scale", {"v" : v, **kwargs})

