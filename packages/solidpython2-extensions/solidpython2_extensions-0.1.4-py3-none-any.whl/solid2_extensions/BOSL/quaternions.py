from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/quaternions.scad'}", use_not_include=True)

class Qrot(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Qrot", {"q" : q, **kwargs})

class _Quat(OpenSCADObject):
    def __init__(self, a=None, s=None, w=None, **kwargs):
       super().__init__("_Quat", {"a" : a, "s" : s, "w" : w, **kwargs})

class Quat(OpenSCADObject):
    def __init__(self, ax=None, ang=None, **kwargs):
       super().__init__("Quat", {"ax" : ax, "ang" : ang, **kwargs})

class QuatX(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("QuatX", {"a" : a, **kwargs})

class QuatY(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("QuatY", {"a" : a, **kwargs})

class QuatZ(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("QuatZ", {"a" : a, **kwargs})

class QuatXYZ(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("QuatXYZ", {"a" : a, **kwargs})

class Q_Ident(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("Q_Ident", {**kwargs})

class Q_Add_S(OpenSCADObject):
    def __init__(self, q=None, s=None, **kwargs):
       super().__init__("Q_Add_S", {"q" : q, "s" : s, **kwargs})

class Q_Sub_S(OpenSCADObject):
    def __init__(self, q=None, s=None, **kwargs):
       super().__init__("Q_Sub_S", {"q" : q, "s" : s, **kwargs})

class Q_Mul_S(OpenSCADObject):
    def __init__(self, q=None, s=None, **kwargs):
       super().__init__("Q_Mul_S", {"q" : q, "s" : s, **kwargs})

class Q_Div_S(OpenSCADObject):
    def __init__(self, q=None, s=None, **kwargs):
       super().__init__("Q_Div_S", {"q" : q, "s" : s, **kwargs})

class Q_Add(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("Q_Add", {"a" : a, "b" : b, **kwargs})

class Q_Sub(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("Q_Sub", {"a" : a, "b" : b, **kwargs})

class Q_Mul(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("Q_Mul", {"a" : a, "b" : b, **kwargs})

class Q_Dot(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("Q_Dot", {"a" : a, "b" : b, **kwargs})

class Q_Neg(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Q_Neg", {"q" : q, **kwargs})

class Q_Conj(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Q_Conj", {"q" : q, **kwargs})

class Q_Norm(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Q_Norm", {"q" : q, **kwargs})

class Q_Normalize(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Q_Normalize", {"q" : q, **kwargs})

class Q_Dist(OpenSCADObject):
    def __init__(self, q1=None, q2=None, **kwargs):
       super().__init__("Q_Dist", {"q1" : q1, "q2" : q2, **kwargs})

class Q_Slerp(OpenSCADObject):
    def __init__(self, q1=None, q2=None, u=None, **kwargs):
       super().__init__("Q_Slerp", {"q1" : q1, "q2" : q2, "u" : u, **kwargs})

class Q_Matrix3(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Q_Matrix3", {"q" : q, **kwargs})

class Q_Matrix4(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Q_Matrix4", {"q" : q, **kwargs})

class Q_Axis(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Q_Axis", {"q" : q, **kwargs})

class Q_Angle(OpenSCADObject):
    def __init__(self, q=None, **kwargs):
       super().__init__("Q_Angle", {"q" : q, **kwargs})

class Q_Rot_Vector(OpenSCADObject):
    def __init__(self, v=None, q=None, **kwargs):
       super().__init__("Q_Rot_Vector", {"v" : v, "q" : q, **kwargs})

