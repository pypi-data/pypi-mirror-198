from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/version.scad'}", use_not_include=False)

BOSL_VERSION = OpenSCADConstant('BOSL_VERSION')
class bosl_required(OpenSCADObject):
    def __init__(self, version=None, **kwargs):
       super().__init__("bosl_required", {"version" : version, **kwargs})

class bosl_version(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("bosl_version", {**kwargs})

class bosl_version_num(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("bosl_version_num", {**kwargs})

class bosl_version_str(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("bosl_version_str", {**kwargs})

class _version_split_str(OpenSCADObject):
    def __init__(self, x=None, _i=None, _out=None, _num=None, **kwargs):
       super().__init__("_version_split_str", {"x" : x, "_i" : _i, "_out" : _out, "_num" : _num, **kwargs})

class version_to_list(OpenSCADObject):
    def __init__(self, version=None, **kwargs):
       super().__init__("version_to_list", {"version" : version, **kwargs})

class version_to_str(OpenSCADObject):
    def __init__(self, version=None, **kwargs):
       super().__init__("version_to_str", {"version" : version, **kwargs})

class version_to_num(OpenSCADObject):
    def __init__(self, version=None, **kwargs):
       super().__init__("version_to_num", {"version" : version, **kwargs})

class version_cmp(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("version_cmp", {"a" : a, "b" : b, **kwargs})

