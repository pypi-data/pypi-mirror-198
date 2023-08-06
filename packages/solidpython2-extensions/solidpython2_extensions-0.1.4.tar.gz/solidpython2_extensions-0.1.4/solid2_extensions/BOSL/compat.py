from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/compat.scad'}", use_not_include=True)

class assert_in_list(OpenSCADObject):
    def __init__(self, argname=None, val=None, l=None, idx=None, **kwargs):
       super().__init__("assert_in_list", {"argname" : argname, "val" : val, "l" : l, "idx" : idx, **kwargs})

class assertion(OpenSCADObject):
    def __init__(self, succ=None, msg=None, **kwargs):
       super().__init__("assertion", {"succ" : succ, "msg" : msg, **kwargs})

class echo_error(OpenSCADObject):
    def __init__(self, msg=None, pfx=None, **kwargs):
       super().__init__("echo_error", {"msg" : msg, "pfx" : pfx, **kwargs})

class echo_warning(OpenSCADObject):
    def __init__(self, msg=None, pfx=None, **kwargs):
       super().__init__("echo_warning", {"msg" : msg, "pfx" : pfx, **kwargs})

class deprecate(OpenSCADObject):
    def __init__(self, name=None, suggest=None, **kwargs):
       super().__init__("deprecate", {"name" : name, "suggest" : suggest, **kwargs})

class deprecate_argument(OpenSCADObject):
    def __init__(self, name=None, arg=None, suggest=None, **kwargs):
       super().__init__("deprecate_argument", {"name" : name, "arg" : arg, "suggest" : suggest, **kwargs})

class default(OpenSCADObject):
    def __init__(self, v=None, dflt=None, **kwargs):
       super().__init__("default", {"v" : v, "dflt" : dflt, **kwargs})

class is_def(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("is_def", {"v" : v, **kwargs})

class is_str(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("is_str", {"v" : v, **kwargs})

class is_boolean(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("is_boolean", {"v" : v, **kwargs})

class is_scalar(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("is_scalar", {"v" : v, **kwargs})

class is_array(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("is_array", {"v" : v, **kwargs})

class get_radius(OpenSCADObject):
    def __init__(self, r1=None, r=None, d1=None, d=None, dflt=None, **kwargs):
       super().__init__("get_radius", {"r1" : r1, "r" : r, "d1" : d1, "d" : d, "dflt" : dflt, **kwargs})

class Len(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("Len", {"v" : v, **kwargs})

class remove_undefs(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("remove_undefs", {"v" : v, **kwargs})

class first_defined(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("first_defined", {"v" : v, **kwargs})

class any_defined(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("any_defined", {"v" : v, **kwargs})

class scalar_vec3(OpenSCADObject):
    def __init__(self, v=None, dflt=None, **kwargs):
       super().__init__("scalar_vec3", {"v" : v, "dflt" : dflt, **kwargs})

class f_echo(OpenSCADObject):
    def __init__(self, msg=None, **kwargs):
       super().__init__("f_echo", {"msg" : msg, **kwargs})

class assert_in_list(OpenSCADObject):
    def __init__(self, argname=None, val=None, l=None, idx=None, **kwargs):
       super().__init__("assert_in_list", {"argname" : argname, "val" : val, "l" : l, "idx" : idx, **kwargs})

class assertion(OpenSCADObject):
    def __init__(self, succ=None, msg=None, **kwargs):
       super().__init__("assertion", {"succ" : succ, "msg" : msg, **kwargs})

class echo_error(OpenSCADObject):
    def __init__(self, msg=None, pfx=None, **kwargs):
       super().__init__("echo_error", {"msg" : msg, "pfx" : pfx, **kwargs})

class echo_warning(OpenSCADObject):
    def __init__(self, msg=None, pfx=None, **kwargs):
       super().__init__("echo_warning", {"msg" : msg, "pfx" : pfx, **kwargs})

class deprecate(OpenSCADObject):
    def __init__(self, name=None, suggest=None, **kwargs):
       super().__init__("deprecate", {"name" : name, "suggest" : suggest, **kwargs})

class deprecate_argument(OpenSCADObject):
    def __init__(self, name=None, arg=None, suggest=None, **kwargs):
       super().__init__("deprecate_argument", {"name" : name, "arg" : arg, "suggest" : suggest, **kwargs})

