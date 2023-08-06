from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/joiners.scad'}", use_not_include=True)

class half_joiner_clear(OpenSCADObject):
    def __init__(self, h=None, w=None, a=None, clearance=None, overlap=None, orient=None, align=None, **kwargs):
       super().__init__("half_joiner_clear", {"h" : h, "w" : w, "a" : a, "clearance" : clearance, "overlap" : overlap, "orient" : orient, "align" : align, **kwargs})

class half_joiner(OpenSCADObject):
    def __init__(self, h=None, w=None, l=None, a=None, screwsize=None, guides=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("half_joiner", {"h" : h, "w" : w, "l" : l, "a" : a, "screwsize" : screwsize, "guides" : guides, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class half_joiner2(OpenSCADObject):
    def __init__(self, h=None, w=None, l=None, a=None, screwsize=None, guides=None, orient=None, align=None, **kwargs):
       super().__init__("half_joiner2", {"h" : h, "w" : w, "l" : l, "a" : a, "screwsize" : screwsize, "guides" : guides, "orient" : orient, "align" : align, **kwargs})

class joiner_clear(OpenSCADObject):
    def __init__(self, h=None, w=None, a=None, clearance=None, overlap=None, orient=None, align=None, **kwargs):
       super().__init__("joiner_clear", {"h" : h, "w" : w, "a" : a, "clearance" : clearance, "overlap" : overlap, "orient" : orient, "align" : align, **kwargs})

class joiner(OpenSCADObject):
    def __init__(self, h=None, w=None, l=None, a=None, screwsize=None, guides=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("joiner", {"h" : h, "w" : w, "l" : l, "a" : a, "screwsize" : screwsize, "guides" : guides, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class joiner_pair_clear(OpenSCADObject):
    def __init__(self, spacing=None, h=None, w=None, a=None, n=None, clearance=None, overlap=None, orient=None, align=None, **kwargs):
       super().__init__("joiner_pair_clear", {"spacing" : spacing, "h" : h, "w" : w, "a" : a, "n" : n, "clearance" : clearance, "overlap" : overlap, "orient" : orient, "align" : align, **kwargs})

class joiner_pair(OpenSCADObject):
    def __init__(self, spacing=None, h=None, w=None, l=None, a=None, n=None, alternate=None, screwsize=None, guides=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("joiner_pair", {"spacing" : spacing, "h" : h, "w" : w, "l" : l, "a" : a, "n" : n, "alternate" : alternate, "screwsize" : screwsize, "guides" : guides, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class joiner_quad_clear(OpenSCADObject):
    def __init__(self, xspacing=None, yspacing=None, spacing1=None, spacing2=None, n=None, h=None, w=None, a=None, clearance=None, overlap=None, orient=None, align=None, **kwargs):
       super().__init__("joiner_quad_clear", {"xspacing" : xspacing, "yspacing" : yspacing, "spacing1" : spacing1, "spacing2" : spacing2, "n" : n, "h" : h, "w" : w, "a" : a, "clearance" : clearance, "overlap" : overlap, "orient" : orient, "align" : align, **kwargs})

class joiner_quad(OpenSCADObject):
    def __init__(self, spacing1=None, spacing2=None, xspacing=None, yspacing=None, h=None, w=None, l=None, a=None, n=None, alternate=None, screwsize=None, guides=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("joiner_quad", {"spacing1" : spacing1, "spacing2" : spacing2, "xspacing" : xspacing, "yspacing" : yspacing, "h" : h, "w" : w, "l" : l, "a" : a, "n" : n, "alternate" : alternate, "screwsize" : screwsize, "guides" : guides, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

