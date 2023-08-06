from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/linalg.scad'}", use_not_include=False)

class echo_matrix(OpenSCADObject):
    def __init__(self, M=None, description=None, sig=None, sep=None, eps=None, **kwargs):
       super().__init__("echo_matrix", {"M" : M, "description" : description, "sig" : sig, "sep" : sep, "eps" : eps, **kwargs})

class is_matrix(OpenSCADObject):
    def __init__(self, A=None, m=None, n=None, square=None, **kwargs):
       super().__init__("is_matrix", {"A" : A, "m" : m, "n" : n, "square" : square, **kwargs})

class is_matrix_symmetric(OpenSCADObject):
    def __init__(self, A=None, eps=None, **kwargs):
       super().__init__("is_matrix_symmetric", {"A" : A, "eps" : eps, **kwargs})

class is_rotation(OpenSCADObject):
    def __init__(self, A=None, dim=None, centered=None, **kwargs):
       super().__init__("is_rotation", {"A" : A, "dim" : dim, "centered" : centered, **kwargs})

class echo_matrix(OpenSCADObject):
    def __init__(self, M=None, description=None, sig=None, sep=None, eps=None, **kwargs):
       super().__init__("echo_matrix", {"M" : M, "description" : description, "sig" : sig, "sep" : sep, "eps" : eps, **kwargs})

class column(OpenSCADObject):
    def __init__(self, M=None, i=None, **kwargs):
       super().__init__("column", {"M" : M, "i" : i, **kwargs})

class submatrix(OpenSCADObject):
    def __init__(self, M=None, idx1=None, idx2=None, **kwargs):
       super().__init__("submatrix", {"M" : M, "idx1" : idx1, "idx2" : idx2, **kwargs})

class ident(OpenSCADObject):
    def __init__(self, n=None, **kwargs):
       super().__init__("ident", {"n" : n, **kwargs})

class diagonal_matrix(OpenSCADObject):
    def __init__(self, diag=None, offdiag=None, **kwargs):
       super().__init__("diagonal_matrix", {"diag" : diag, "offdiag" : offdiag, **kwargs})

class transpose(OpenSCADObject):
    def __init__(self, M=None, reverse=None, **kwargs):
       super().__init__("transpose", {"M" : M, "reverse" : reverse, **kwargs})

class outer_product(OpenSCADObject):
    def __init__(self, u=None, v=None, **kwargs):
       super().__init__("outer_product", {"u" : u, "v" : v, **kwargs})

class submatrix_set(OpenSCADObject):
    def __init__(self, M=None, A=None, m=None, n=None, **kwargs):
       super().__init__("submatrix_set", {"M" : M, "A" : A, "m" : m, "n" : n, **kwargs})

class hstack(OpenSCADObject):
    def __init__(self, M1=None, M2=None, M3=None, **kwargs):
       super().__init__("hstack", {"M1" : M1, "M2" : M2, "M3" : M3, **kwargs})

class block_matrix(OpenSCADObject):
    def __init__(self, M=None, **kwargs):
       super().__init__("block_matrix", {"M" : M, **kwargs})

class linear_solve(OpenSCADObject):
    def __init__(self, A=None, b=None, pivot=None, **kwargs):
       super().__init__("linear_solve", {"A" : A, "b" : b, "pivot" : pivot, **kwargs})

class linear_solve3(OpenSCADObject):
    def __init__(self, A=None, b=None, **kwargs):
       super().__init__("linear_solve3", {"A" : A, "b" : b, **kwargs})

class matrix_inverse(OpenSCADObject):
    def __init__(self, A=None, **kwargs):
       super().__init__("matrix_inverse", {"A" : A, **kwargs})

class rot_inverse(OpenSCADObject):
    def __init__(self, T=None, **kwargs):
       super().__init__("rot_inverse", {"T" : T, **kwargs})

class null_space(OpenSCADObject):
    def __init__(self, A=None, eps=None, **kwargs):
       super().__init__("null_space", {"A" : A, "eps" : eps, **kwargs})

class qr_factor(OpenSCADObject):
    def __init__(self, A=None, pivot=None, **kwargs):
       super().__init__("qr_factor", {"A" : A, "pivot" : pivot, **kwargs})

class _qr_factor(OpenSCADObject):
    def __init__(self, A=None, Q=None, P=None, pivot=None, col=None, m=None, n=None, **kwargs):
       super().__init__("_qr_factor", {"A" : A, "Q" : Q, "P" : P, "pivot" : pivot, "col" : col, "m" : m, "n" : n, **kwargs})

class _swap_matrix(OpenSCADObject):
    def __init__(self, n=None, i=None, j=None, **kwargs):
       super().__init__("_swap_matrix", {"n" : n, "i" : i, "j" : j, **kwargs})

class back_substitute(OpenSCADObject):
    def __init__(self, R=None, b=None, transpose=None, **kwargs):
       super().__init__("back_substitute", {"R" : R, "b" : b, "transpose" : transpose, **kwargs})

class _back_substitute(OpenSCADObject):
    def __init__(self, R=None, b=None, x=None, **kwargs):
       super().__init__("_back_substitute", {"R" : R, "b" : b, "x" : x, **kwargs})

class cholesky(OpenSCADObject):
    def __init__(self, A=None, **kwargs):
       super().__init__("cholesky", {"A" : A, **kwargs})

class _cholesky(OpenSCADObject):
    def __init__(self, A=None, L=None, n=None, **kwargs):
       super().__init__("_cholesky", {"A" : A, "L" : L, "n" : n, **kwargs})

class det2(OpenSCADObject):
    def __init__(self, M=None, **kwargs):
       super().__init__("det2", {"M" : M, **kwargs})

class det3(OpenSCADObject):
    def __init__(self, M=None, **kwargs):
       super().__init__("det3", {"M" : M, **kwargs})

class det4(OpenSCADObject):
    def __init__(self, M=None, **kwargs):
       super().__init__("det4", {"M" : M, **kwargs})

class determinant(OpenSCADObject):
    def __init__(self, M=None, **kwargs):
       super().__init__("determinant", {"M" : M, **kwargs})

class norm_fro(OpenSCADObject):
    def __init__(self, A=None, **kwargs):
       super().__init__("norm_fro", {"A" : A, **kwargs})

class matrix_trace(OpenSCADObject):
    def __init__(self, M=None, **kwargs):
       super().__init__("matrix_trace", {"M" : M, **kwargs})

