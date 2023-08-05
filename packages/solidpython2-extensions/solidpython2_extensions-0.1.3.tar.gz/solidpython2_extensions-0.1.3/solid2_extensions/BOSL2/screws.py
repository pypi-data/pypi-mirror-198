from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/screws.scad'}", use_not_include=False)

class screw(OpenSCADObject):
    def __init__(self, name=None, head=None, drive=None, thread=None, drive_size=None, oversize=None, spec=None, length=None, l=None, shank=None, tolerance=None, details=None, anchor=None, anchor_head=None, spin=None, orient=None, **kwargs):
       super().__init__("screw", {"name" : name, "head" : head, "drive" : drive, "thread" : thread, "drive_size" : drive_size, "oversize" : oversize, "spec" : spec, "length" : length, "l" : l, "shank" : shank, "tolerance" : tolerance, "details" : details, "anchor" : anchor, "anchor_head" : anchor_head, "spin" : spin, "orient" : orient, **kwargs})

class _driver(OpenSCADObject):
    def __init__(self, spec=None, **kwargs):
       super().__init__("_driver", {"spec" : spec, **kwargs})

class _rod(OpenSCADObject):
    def __init__(self, spec=None, length=None, tolerance=None, orient=None, spin=None, anchor=None, **kwargs):
       super().__init__("_rod", {"spec" : spec, "length" : length, "tolerance" : tolerance, "orient" : orient, "spin" : spin, "anchor" : anchor, **kwargs})

class nut(OpenSCADObject):
    def __init__(self, name=None, diameter=None, thickness=None, thread=None, oversize=None, spec=None, tolerance=None, bevel=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nut", {"name" : name, "diameter" : diameter, "thickness" : thickness, "thread" : thread, "oversize" : oversize, "spec" : spec, "tolerance" : tolerance, "bevel" : bevel, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class screw_head(OpenSCADObject):
    def __init__(self, screw_info=None, details=None, **kwargs):
       super().__init__("screw_head", {"screw_info" : screw_info, "details" : details, **kwargs})

class screw(OpenSCADObject):
    def __init__(self, name=None, head=None, drive=None, thread=None, drive_size=None, oversize=None, spec=None, length=None, l=None, shank=None, tolerance=None, details=None, anchor=None, anchor_head=None, spin=None, orient=None, **kwargs):
       super().__init__("screw", {"name" : name, "head" : head, "drive" : drive, "thread" : thread, "drive_size" : drive_size, "oversize" : oversize, "spec" : spec, "length" : length, "l" : l, "shank" : shank, "tolerance" : tolerance, "details" : details, "anchor" : anchor, "anchor_head" : anchor_head, "spin" : spin, "orient" : orient, **kwargs})

class _ISO_thread_tolerance(OpenSCADObject):
    def __init__(self, diameter=None, pitch=None, internal=None, tolerance=None, **kwargs):
       super().__init__("_ISO_thread_tolerance", {"diameter" : diameter, "pitch" : pitch, "internal" : internal, "tolerance" : tolerance, **kwargs})

class _UTS_thread_tolerance(OpenSCADObject):
    def __init__(self, diam=None, pitch=None, internal=None, tolerance=None, **kwargs):
       super().__init__("_UTS_thread_tolerance", {"diam" : diam, "pitch" : pitch, "internal" : internal, "tolerance" : tolerance, **kwargs})

class _exact_thread_tolerance(OpenSCADObject):
    def __init__(self, d=None, P=None, **kwargs):
       super().__init__("_exact_thread_tolerance", {"d" : d, "P" : P, **kwargs})

class nut(OpenSCADObject):
    def __init__(self, name=None, diameter=None, thickness=None, thread=None, oversize=None, spec=None, tolerance=None, bevel=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("nut", {"name" : name, "diameter" : diameter, "thickness" : thickness, "thread" : thread, "oversize" : oversize, "spec" : spec, "tolerance" : tolerance, "bevel" : bevel, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _parse_screw_name(OpenSCADObject):
    def __init__(self, name=None, **kwargs):
       super().__init__("_parse_screw_name", {"name" : name, **kwargs})

class _parse_drive(OpenSCADObject):
    def __init__(self, drive=None, drive_size=None, **kwargs):
       super().__init__("_parse_drive", {"drive" : drive, "drive_size" : drive_size, **kwargs})

class screw_head(OpenSCADObject):
    def __init__(self, screw_info=None, details=None, **kwargs):
       super().__init__("screw_head", {"screw_info" : screw_info, "details" : details, **kwargs})

class screw_info(OpenSCADObject):
    def __init__(self, name=None, head=None, drive=None, thread=None, drive_size=None, oversize=None, **kwargs):
       super().__init__("screw_info", {"name" : name, "head" : head, "drive" : drive, "thread" : thread, "drive_size" : drive_size, "oversize" : oversize, **kwargs})

class _screw_info_english(OpenSCADObject):
    def __init__(self, diam=None, threadcount=None, head=None, thread=None, drive=None, **kwargs):
       super().__init__("_screw_info_english", {"diam" : diam, "threadcount" : threadcount, "head" : head, "thread" : thread, "drive" : drive, **kwargs})

class _screw_info_metric(OpenSCADObject):
    def __init__(self, diam=None, pitch=None, head=None, thread=None, drive=None, **kwargs):
       super().__init__("_screw_info_metric", {"diam" : diam, "pitch" : pitch, "head" : head, "thread" : thread, "drive" : drive, **kwargs})

class _is_positive(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("_is_positive", {"x" : x, **kwargs})

class _validate_screw_spec(OpenSCADObject):
    def __init__(self, spec=None, **kwargs):
       super().__init__("_validate_screw_spec", {"spec" : spec, **kwargs})

class thread_specification(OpenSCADObject):
    def __init__(self, screw_spec=None, tolerance=None, internal=None, **kwargs):
       super().__init__("thread_specification", {"screw_spec" : screw_spec, "tolerance" : tolerance, "internal" : internal, **kwargs})

