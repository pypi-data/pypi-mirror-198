from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/beziers.scad'}", use_not_include=False)

_bezier_matrix_table = OpenSCADConstant('_bezier_matrix_table')
class debug_bezier(OpenSCADObject):
    def __init__(self, bezpath=None, width=None, N=None, **kwargs):
       super().__init__("debug_bezier", {"bezpath" : bezpath, "width" : width, "N" : N, **kwargs})

class debug_bezier_patches(OpenSCADObject):
    def __init__(self, patches=None, size=None, splinesteps=None, showcps=None, showdots=None, showpatch=None, convexity=None, style=None, **kwargs):
       super().__init__("debug_bezier_patches", {"patches" : patches, "size" : size, "splinesteps" : splinesteps, "showcps" : showcps, "showdots" : showdots, "showpatch" : showpatch, "convexity" : convexity, "style" : style, **kwargs})

class bezier_points(OpenSCADObject):
    def __init__(self, curve=None, u=None, **kwargs):
       super().__init__("bezier_points", {"curve" : curve, "u" : u, **kwargs})

class _signed_pascals_triangle(OpenSCADObject):
    def __init__(self, N=None, tri=None, **kwargs):
       super().__init__("_signed_pascals_triangle", {"N" : N, "tri" : tri, **kwargs})

class _compute_bezier_matrix(OpenSCADObject):
    def __init__(self, N=None, **kwargs):
       super().__init__("_compute_bezier_matrix", {"N" : N, **kwargs})

class _bezier_matrix(OpenSCADObject):
    def __init__(self, N=None, **kwargs):
       super().__init__("_bezier_matrix", {"N" : N, **kwargs})

class bezier_curve(OpenSCADObject):
    def __init__(self, bezier=None, splinesteps=None, endpoint=None, **kwargs):
       super().__init__("bezier_curve", {"bezier" : bezier, "splinesteps" : splinesteps, "endpoint" : endpoint, **kwargs})

class bezier_derivative(OpenSCADObject):
    def __init__(self, bezier=None, u=None, order=None, **kwargs):
       super().__init__("bezier_derivative", {"bezier" : bezier, "u" : u, "order" : order, **kwargs})

class bezier_tangent(OpenSCADObject):
    def __init__(self, bezier=None, u=None, **kwargs):
       super().__init__("bezier_tangent", {"bezier" : bezier, "u" : u, **kwargs})

class bezier_curvature(OpenSCADObject):
    def __init__(self, bezier=None, u=None, **kwargs):
       super().__init__("bezier_curvature", {"bezier" : bezier, "u" : u, **kwargs})

class bezier_closest_point(OpenSCADObject):
    def __init__(self, bezier=None, pt=None, max_err=None, u=None, end_u=None, **kwargs):
       super().__init__("bezier_closest_point", {"bezier" : bezier, "pt" : pt, "max_err" : max_err, "u" : u, "end_u" : end_u, **kwargs})

class bezier_length(OpenSCADObject):
    def __init__(self, bezier=None, start_u=None, end_u=None, max_deflect=None, **kwargs):
       super().__init__("bezier_length", {"bezier" : bezier, "start_u" : start_u, "end_u" : end_u, "max_deflect" : max_deflect, **kwargs})

class bezier_line_intersection(OpenSCADObject):
    def __init__(self, bezier=None, line=None, **kwargs):
       super().__init__("bezier_line_intersection", {"bezier" : bezier, "line" : line, **kwargs})

class bezpath_points(OpenSCADObject):
    def __init__(self, bezpath=None, curveind=None, u=None, N=None, **kwargs):
       super().__init__("bezpath_points", {"bezpath" : bezpath, "curveind" : curveind, "u" : u, "N" : N, **kwargs})

class bezpath_curve(OpenSCADObject):
    def __init__(self, bezpath=None, splinesteps=None, N=None, endpoint=None, **kwargs):
       super().__init__("bezpath_curve", {"bezpath" : bezpath, "splinesteps" : splinesteps, "N" : N, "endpoint" : endpoint, **kwargs})

class bezpath_closest_point(OpenSCADObject):
    def __init__(self, bezpath=None, pt=None, N=None, max_err=None, seg=None, min_seg=None, min_u=None, min_dist=None, **kwargs):
       super().__init__("bezpath_closest_point", {"bezpath" : bezpath, "pt" : pt, "N" : N, "max_err" : max_err, "seg" : seg, "min_seg" : min_seg, "min_u" : min_u, "min_dist" : min_dist, **kwargs})

class bezpath_length(OpenSCADObject):
    def __init__(self, bezpath=None, N=None, max_deflect=None, **kwargs):
       super().__init__("bezpath_length", {"bezpath" : bezpath, "N" : N, "max_deflect" : max_deflect, **kwargs})

class path_to_bezpath(OpenSCADObject):
    def __init__(self, path=None, closed=None, tangents=None, uniform=None, size=None, relsize=None, **kwargs):
       super().__init__("path_to_bezpath", {"path" : path, "closed" : closed, "tangents" : tangents, "uniform" : uniform, "size" : size, "relsize" : relsize, **kwargs})

class bezpath_close_to_axis(OpenSCADObject):
    def __init__(self, bezpath=None, axis=None, N=None, **kwargs):
       super().__init__("bezpath_close_to_axis", {"bezpath" : bezpath, "axis" : axis, "N" : N, **kwargs})

class bezpath_offset(OpenSCADObject):
    def __init__(self, offset=None, bezier=None, N=None, **kwargs):
       super().__init__("bezpath_offset", {"offset" : offset, "bezier" : bezier, "N" : N, **kwargs})

class bez_begin(OpenSCADObject):
    def __init__(self, pt=None, a=None, r=None, p=None, **kwargs):
       super().__init__("bez_begin", {"pt" : pt, "a" : a, "r" : r, "p" : p, **kwargs})

class bez_tang(OpenSCADObject):
    def __init__(self, pt=None, a=None, r1=None, r2=None, p=None, **kwargs):
       super().__init__("bez_tang", {"pt" : pt, "a" : a, "r1" : r1, "r2" : r2, "p" : p, **kwargs})

class bez_joint(OpenSCADObject):
    def __init__(self, pt=None, a1=None, a2=None, r1=None, r2=None, p1=None, p2=None, **kwargs):
       super().__init__("bez_joint", {"pt" : pt, "a1" : a1, "a2" : a2, "r1" : r1, "r2" : r2, "p1" : p1, "p2" : p2, **kwargs})

class bez_end(OpenSCADObject):
    def __init__(self, pt=None, a=None, r=None, p=None, **kwargs):
       super().__init__("bez_end", {"pt" : pt, "a" : a, "r" : r, "p" : p, **kwargs})

class is_bezier_patch(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_bezier_patch", {"x" : x, **kwargs})

class bezier_patch_flat(OpenSCADObject):
    def __init__(self, size=None, N=None, spin=None, orient=None, trans=None, **kwargs):
       super().__init__("bezier_patch_flat", {"size" : size, "N" : N, "spin" : spin, "orient" : orient, "trans" : trans, **kwargs})

class bezier_patch_reverse(OpenSCADObject):
    def __init__(self, patch=None, **kwargs):
       super().__init__("bezier_patch_reverse", {"patch" : patch, **kwargs})

class bezier_patch_points(OpenSCADObject):
    def __init__(self, patch=None, u=None, v=None, **kwargs):
       super().__init__("bezier_patch_points", {"patch" : patch, "u" : u, "v" : v, **kwargs})

class _bezier_rectangle(OpenSCADObject):
    def __init__(self, patch=None, splinesteps=None, style=None, **kwargs):
       super().__init__("_bezier_rectangle", {"patch" : patch, "splinesteps" : splinesteps, "style" : style, **kwargs})

class bezier_vnf(OpenSCADObject):
    def __init__(self, patches=None, splinesteps=None, style=None, **kwargs):
       super().__init__("bezier_vnf", {"patches" : patches, "splinesteps" : splinesteps, "style" : style, **kwargs})

class bezier_vnf_degenerate_patch(OpenSCADObject):
    def __init__(self, patch=None, splinesteps=None, reverse=None, return_edges=None, **kwargs):
       super().__init__("bezier_vnf_degenerate_patch", {"patch" : patch, "splinesteps" : splinesteps, "reverse" : reverse, "return_edges" : return_edges, **kwargs})

class bezier_patch_normals(OpenSCADObject):
    def __init__(self, patch=None, u=None, v=None, **kwargs):
       super().__init__("bezier_patch_normals", {"patch" : patch, "u" : u, "v" : v, **kwargs})

