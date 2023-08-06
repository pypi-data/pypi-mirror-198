from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/structs.scad'}", use_not_include=False)

class echo_struct(OpenSCADObject):
    def __init__(self, struct=None, name=None, **kwargs):
       super().__init__("echo_struct", {"struct" : struct, "name" : name, **kwargs})

class struct_set(OpenSCADObject):
    def __init__(self, struct=None, key=None, value=None, grow=None, **kwargs):
       super().__init__("struct_set", {"struct" : struct, "key" : key, "value" : value, "grow" : grow, **kwargs})

class _format_key(OpenSCADObject):
    def __init__(self, key=None, **kwargs):
       super().__init__("_format_key", {"key" : key, **kwargs})

class struct_remove(OpenSCADObject):
    def __init__(self, struct=None, key=None, **kwargs):
       super().__init__("struct_remove", {"struct" : struct, "key" : key, **kwargs})

class struct_val(OpenSCADObject):
    def __init__(self, struct=None, key=None, default=None, **kwargs):
       super().__init__("struct_val", {"struct" : struct, "key" : key, "default" : default, **kwargs})

class struct_keys(OpenSCADObject):
    def __init__(self, struct=None, **kwargs):
       super().__init__("struct_keys", {"struct" : struct, **kwargs})

class echo_struct(OpenSCADObject):
    def __init__(self, struct=None, name=None, **kwargs):
       super().__init__("echo_struct", {"struct" : struct, "name" : name, **kwargs})

class is_struct(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_struct", {"x" : x, **kwargs})

