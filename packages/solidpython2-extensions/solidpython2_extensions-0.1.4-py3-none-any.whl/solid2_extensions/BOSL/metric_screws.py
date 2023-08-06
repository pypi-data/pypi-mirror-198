from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/metric_screws.scad'}", use_not_include=True)

class screw(OpenSCADObject):
    def __init__(self, screwsize=None, screwlen=None, headsize=None, headlen=None, pitch=None, countersunk=None, orient=None, align=None, **kwargs):
       super().__init__("screw", {"screwsize" : screwsize, "screwlen" : screwlen, "headsize" : headsize, "headlen" : headlen, "pitch" : pitch, "countersunk" : countersunk, "orient" : orient, "align" : align, **kwargs})

class metric_bolt(OpenSCADObject):
    def __init__(self, headtype=None, size=None, l=None, shank=None, pitch=None, details=None, coarse=None, phillips=None, torx=None, flange=None, orient=None, align=None, **kwargs):
       super().__init__("metric_bolt", {"headtype" : headtype, "size" : size, "l" : l, "shank" : shank, "pitch" : pitch, "details" : details, "coarse" : coarse, "phillips" : phillips, "torx" : torx, "flange" : flange, "orient" : orient, "align" : align, **kwargs})

class metric_nut(OpenSCADObject):
    def __init__(self, size=None, hole=None, pitch=None, details=None, flange=None, center=None, orient=None, align=None, **kwargs):
       super().__init__("metric_nut", {"size" : size, "hole" : hole, "pitch" : pitch, "details" : details, "flange" : flange, "center" : center, "orient" : orient, "align" : align, **kwargs})

class get_metric_bolt_head_size(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_bolt_head_size", {"size" : size, **kwargs})

class get_metric_bolt_head_height(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_bolt_head_height", {"size" : size, **kwargs})

class get_metric_socket_cap_diam(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_socket_cap_diam", {"size" : size, **kwargs})

class get_metric_socket_cap_height(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_socket_cap_height", {"size" : size, **kwargs})

class get_metric_socket_cap_socket_size(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_socket_cap_socket_size", {"size" : size, **kwargs})

class get_metric_socket_cap_socket_depth(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_socket_cap_socket_depth", {"size" : size, **kwargs})

class get_metric_iso_coarse_thread_pitch(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_iso_coarse_thread_pitch", {"size" : size, **kwargs})

class get_metric_iso_fine_thread_pitch(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_iso_fine_thread_pitch", {"size" : size, **kwargs})

class get_metric_iso_superfine_thread_pitch(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_iso_superfine_thread_pitch", {"size" : size, **kwargs})

class get_metric_jis_thread_pitch(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_jis_thread_pitch", {"size" : size, **kwargs})

class get_metric_nut_size(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_nut_size", {"size" : size, **kwargs})

class get_metric_nut_thickness(OpenSCADObject):
    def __init__(self, size=None, **kwargs):
       super().__init__("get_metric_nut_thickness", {"size" : size, **kwargs})

