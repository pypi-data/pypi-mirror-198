from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/affine.scad'}", use_not_include=False)

class affine2d_identity(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("affine2d_identity", {**kwargs})

class affine2d_translate(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("affine2d_translate", {"v" : v, **kwargs})

class affine2d_scale(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("affine2d_scale", {"v" : v, **kwargs})

class affine2d_zrot(OpenSCADObject):
    def __init__(self, ang=None, **kwargs):
       super().__init__("affine2d_zrot", {"ang" : ang, **kwargs})

class affine2d_mirror(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("affine2d_mirror", {"v" : v, **kwargs})

class affine2d_skew(OpenSCADObject):
    def __init__(self, xa=None, ya=None, **kwargs):
       super().__init__("affine2d_skew", {"xa" : xa, "ya" : ya, **kwargs})

class affine3d_identity(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("affine3d_identity", {**kwargs})

class affine3d_translate(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("affine3d_translate", {"v" : v, **kwargs})

class affine3d_scale(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("affine3d_scale", {"v" : v, **kwargs})

class affine3d_xrot(OpenSCADObject):
    def __init__(self, ang=None, **kwargs):
       super().__init__("affine3d_xrot", {"ang" : ang, **kwargs})

class affine3d_yrot(OpenSCADObject):
    def __init__(self, ang=None, **kwargs):
       super().__init__("affine3d_yrot", {"ang" : ang, **kwargs})

class affine3d_zrot(OpenSCADObject):
    def __init__(self, ang=None, **kwargs):
       super().__init__("affine3d_zrot", {"ang" : ang, **kwargs})

class affine3d_rot_by_axis(OpenSCADObject):
    def __init__(self, u=None, ang=None, **kwargs):
       super().__init__("affine3d_rot_by_axis", {"u" : u, "ang" : ang, **kwargs})

class affine3d_rot_from_to(OpenSCADObject):
    def __init__(self, _from=None, to=None, **kwargs):
       super().__init__("affine3d_rot_from_to", {"_from" : _from, "to" : to, **kwargs})

class affine3d_mirror(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("affine3d_mirror", {"v" : v, **kwargs})

class affine3d_skew(OpenSCADObject):
    def __init__(self, sxy=None, sxz=None, syx=None, syz=None, szx=None, szy=None, **kwargs):
       super().__init__("affine3d_skew", {"sxy" : sxy, "sxz" : sxz, "syx" : syx, "syz" : syz, "szx" : szx, "szy" : szy, **kwargs})

class affine3d_skew_xy(OpenSCADObject):
    def __init__(self, xa=None, ya=None, **kwargs):
       super().__init__("affine3d_skew_xy", {"xa" : xa, "ya" : ya, **kwargs})

class affine3d_skew_xz(OpenSCADObject):
    def __init__(self, xa=None, za=None, **kwargs):
       super().__init__("affine3d_skew_xz", {"xa" : xa, "za" : za, **kwargs})

class affine3d_skew_yz(OpenSCADObject):
    def __init__(self, ya=None, za=None, **kwargs):
       super().__init__("affine3d_skew_yz", {"ya" : ya, "za" : za, **kwargs})

