from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/threading.scad'}", use_not_include=True)

class trapezoidal_threaded_rod(OpenSCADObject):
    def __init__(self, d=None, l=None, pitch=None, thread_angle=None, thread_depth=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, starts=None, profile=None, internal=None, slop=None, orient=None, align=None, center=None, **kwargs):
       super().__init__("trapezoidal_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "thread_angle" : thread_angle, "thread_depth" : thread_depth, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "profile" : profile, "internal" : internal, "slop" : slop, "orient" : orient, "align" : align, "center" : center, **kwargs})

class trapezoidal_threaded_nut(OpenSCADObject):
    def __init__(self, od=None, id=None, h=None, pitch=None, thread_depth=None, thread_angle=None, profile=None, left_handed=None, starts=None, bevel=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("trapezoidal_threaded_nut", {"od" : od, "id" : id, "h" : h, "pitch" : pitch, "thread_depth" : thread_depth, "thread_angle" : thread_angle, "profile" : profile, "left_handed" : left_handed, "starts" : starts, "bevel" : bevel, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class threaded_rod(OpenSCADObject):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, internal=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "internal" : internal, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class threaded_nut(OpenSCADObject):
    def __init__(self, od=None, id=None, h=None, pitch=None, left_handed=None, bevel=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("threaded_nut", {"od" : od, "id" : id, "h" : h, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class buttress_threaded_rod(OpenSCADObject):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, internal=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("buttress_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "internal" : internal, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class buttress_threaded_nut(OpenSCADObject):
    def __init__(self, od=None, id=None, h=None, pitch=None, left_handed=None, bevel=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("buttress_threaded_nut", {"od" : od, "id" : id, "h" : h, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class metric_trapezoidal_threaded_rod(OpenSCADObject):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, starts=None, bevel=None, bevel1=None, bevel2=None, orient=None, align=None, **kwargs):
       super().__init__("metric_trapezoidal_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "starts" : starts, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "orient" : orient, "align" : align, **kwargs})

class metric_trapezoidal_threaded_nut(OpenSCADObject):
    def __init__(self, od=None, id=None, h=None, pitch=None, starts=None, left_handed=None, bevel=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("metric_trapezoidal_threaded_nut", {"od" : od, "id" : id, "h" : h, "pitch" : pitch, "starts" : starts, "left_handed" : left_handed, "bevel" : bevel, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class acme_threaded_rod(OpenSCADObject):
    def __init__(self, d=None, l=None, pitch=None, thread_angle=None, thread_depth=None, starts=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, orient=None, align=None, **kwargs):
       super().__init__("acme_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "thread_angle" : thread_angle, "thread_depth" : thread_depth, "starts" : starts, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "orient" : orient, "align" : align, **kwargs})

class acme_threaded_nut(OpenSCADObject):
    def __init__(self, od=None, id=None, h=None, pitch=None, thread_angle=None, thread_depth=None, starts=None, left_handed=None, bevel=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("acme_threaded_nut", {"od" : od, "id" : id, "h" : h, "pitch" : pitch, "thread_angle" : thread_angle, "thread_depth" : thread_depth, "starts" : starts, "left_handed" : left_handed, "bevel" : bevel, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

class square_threaded_rod(OpenSCADObject):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, starts=None, orient=None, align=None, **kwargs):
       super().__init__("square_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "orient" : orient, "align" : align, **kwargs})

class square_threaded_nut(OpenSCADObject):
    def __init__(self, od=None, id=None, h=None, pitch=None, left_handed=None, bevel=None, starts=None, slop=None, orient=None, align=None, **kwargs):
       super().__init__("square_threaded_nut", {"od" : od, "id" : id, "h" : h, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "starts" : starts, "slop" : slop, "orient" : orient, "align" : align, **kwargs})

