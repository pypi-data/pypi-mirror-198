from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/masks2d.scad'}", use_not_include=False)

class mask2d_roundover(OpenSCADObject):
    def __init__(self, r=None, inset=None, excess=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_roundover", {"r" : r, "inset" : inset, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_cove(OpenSCADObject):
    def __init__(self, r=None, inset=None, excess=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_cove", {"r" : r, "inset" : inset, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_chamfer(OpenSCADObject):
    def __init__(self, edge=None, angle=None, inset=None, excess=None, x=None, y=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_chamfer", {"edge" : edge, "angle" : angle, "inset" : inset, "excess" : excess, "x" : x, "y" : y, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_rabbet(OpenSCADObject):
    def __init__(self, size=None, excess=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_rabbet", {"size" : size, "excess" : excess, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_dovetail(OpenSCADObject):
    def __init__(self, edge=None, angle=None, inset=None, shelf=None, excess=None, x=None, y=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_dovetail", {"edge" : edge, "angle" : angle, "inset" : inset, "shelf" : shelf, "excess" : excess, "x" : x, "y" : y, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_teardrop(OpenSCADObject):
    def __init__(self, r=None, angle=None, excess=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_teardrop", {"r" : r, "angle" : angle, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_ogee(OpenSCADObject):
    def __init__(self, pattern=None, excess=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_ogee", {"pattern" : pattern, "excess" : excess, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_roundover(OpenSCADObject):
    def __init__(self, r=None, inset=None, excess=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_roundover", {"r" : r, "inset" : inset, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_cove(OpenSCADObject):
    def __init__(self, r=None, inset=None, excess=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_cove", {"r" : r, "inset" : inset, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_chamfer(OpenSCADObject):
    def __init__(self, edge=None, angle=None, inset=None, excess=None, x=None, y=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_chamfer", {"edge" : edge, "angle" : angle, "inset" : inset, "excess" : excess, "x" : x, "y" : y, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_rabbet(OpenSCADObject):
    def __init__(self, size=None, excess=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_rabbet", {"size" : size, "excess" : excess, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_dovetail(OpenSCADObject):
    def __init__(self, edge=None, angle=None, inset=None, shelf=None, excess=None, x=None, y=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_dovetail", {"edge" : edge, "angle" : angle, "inset" : inset, "shelf" : shelf, "excess" : excess, "x" : x, "y" : y, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_teardrop(OpenSCADObject):
    def __init__(self, r=None, angle=None, excess=None, d=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_teardrop", {"r" : r, "angle" : angle, "excess" : excess, "d" : d, "anchor" : anchor, "spin" : spin, **kwargs})

class mask2d_ogee(OpenSCADObject):
    def __init__(self, pattern=None, excess=None, anchor=None, spin=None, **kwargs):
       super().__init__("mask2d_ogee", {"pattern" : pattern, "excess" : excess, "anchor" : anchor, "spin" : spin, **kwargs})

