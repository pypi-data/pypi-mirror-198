from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/beziers.scad'}", use_not_include=True)

class bezier_polygon(OpenSCADObject):
    def __init__(self, bezier=None, splinesteps=None, N=None, **kwargs):
       super().__init__("bezier_polygon", {"bezier" : bezier, "splinesteps" : splinesteps, "N" : N, **kwargs})

class linear_extrude_bezier(OpenSCADObject):
    def __init__(self, bezier=None, height=None, splinesteps=None, N=None, center=None, convexity=None, twist=None, slices=None, scale=None, orient=None, align=None, **kwargs):
       super().__init__("linear_extrude_bezier", {"bezier" : bezier, "height" : height, "splinesteps" : splinesteps, "N" : N, "center" : center, "convexity" : convexity, "twist" : twist, "slices" : slices, "scale" : scale, "orient" : orient, "align" : align, **kwargs})

class revolve_bezier(OpenSCADObject):
    def __init__(self, bezier=None, splinesteps=None, N=None, convexity=None, angle=None, orient=None, align=None, **kwargs):
       super().__init__("revolve_bezier", {"bezier" : bezier, "splinesteps" : splinesteps, "N" : N, "convexity" : convexity, "angle" : angle, "orient" : orient, "align" : align, **kwargs})

class rotate_extrude_bezier(OpenSCADObject):
    def __init__(self, bezier=None, splinesteps=None, N=None, convexity=None, angle=None, orient=None, align=None, **kwargs):
       super().__init__("rotate_extrude_bezier", {"bezier" : bezier, "splinesteps" : splinesteps, "N" : N, "convexity" : convexity, "angle" : angle, "orient" : orient, "align" : align, **kwargs})

class revolve_bezier_solid_to_axis(OpenSCADObject):
    def __init__(self, bezier=None, splinesteps=None, N=None, convexity=None, angle=None, orient=None, align=None, **kwargs):
       super().__init__("revolve_bezier_solid_to_axis", {"bezier" : bezier, "splinesteps" : splinesteps, "N" : N, "convexity" : convexity, "angle" : angle, "orient" : orient, "align" : align, **kwargs})

class revolve_bezier_offset_shell(OpenSCADObject):
    def __init__(self, bezier=None, offset=None, splinesteps=None, N=None, convexity=None, angle=None, orient=None, align=None, **kwargs):
       super().__init__("revolve_bezier_offset_shell", {"bezier" : bezier, "offset" : offset, "splinesteps" : splinesteps, "N" : N, "convexity" : convexity, "angle" : angle, "orient" : orient, "align" : align, **kwargs})

class extrude_2d_shapes_along_bezier(OpenSCADObject):
    def __init__(self, bezier=None, splinesteps=None, N=None, convexity=None, clipsize=None, **kwargs):
       super().__init__("extrude_2d_shapes_along_bezier", {"bezier" : bezier, "splinesteps" : splinesteps, "N" : N, "convexity" : convexity, "clipsize" : clipsize, **kwargs})

class extrude_bezier_along_bezier(OpenSCADObject):
    def __init__(self, bezier=None, path=None, pathsteps=None, bezsteps=None, bezN=None, pathN=None, **kwargs):
       super().__init__("extrude_bezier_along_bezier", {"bezier" : bezier, "path" : path, "pathsteps" : pathsteps, "bezsteps" : bezsteps, "bezN" : bezN, "pathN" : pathN, **kwargs})

class trace_bezier(OpenSCADObject):
    def __init__(self, bez=None, N=None, size=None, **kwargs):
       super().__init__("trace_bezier", {"bez" : bez, "N" : N, "size" : size, **kwargs})

class bezier_polyhedron(OpenSCADObject):
    def __init__(self, patches=None, tris=None, splinesteps=None, vertices=None, faces=None, **kwargs):
       super().__init__("bezier_polyhedron", {"patches" : patches, "tris" : tris, "splinesteps" : splinesteps, "vertices" : vertices, "faces" : faces, **kwargs})

class trace_bezier_patches(OpenSCADObject):
    def __init__(self, patches=None, tris=None, size=None, showcps=None, splinesteps=None, **kwargs):
       super().__init__("trace_bezier_patches", {"patches" : patches, "tris" : tris, "size" : size, "showcps" : showcps, "splinesteps" : splinesteps, **kwargs})

class bez_point(OpenSCADObject):
    def __init__(self, curve=None, u=None, **kwargs):
       super().__init__("bez_point", {"curve" : curve, "u" : u, **kwargs})

class bez_tangent(OpenSCADObject):
    def __init__(self, curve=None, u=None, **kwargs):
       super().__init__("bez_tangent", {"curve" : curve, "u" : u, **kwargs})

class bezier_segment_closest_point(OpenSCADObject):
    def __init__(self, curve=None, pt=None, max_err=None, u=None, end_u=None, **kwargs):
       super().__init__("bezier_segment_closest_point", {"curve" : curve, "pt" : pt, "max_err" : max_err, "u" : u, "end_u" : end_u, **kwargs})

class bezier_segment_length(OpenSCADObject):
    def __init__(self, curve=None, start_u=None, end_u=None, max_deflect=None, **kwargs):
       super().__init__("bezier_segment_length", {"curve" : curve, "start_u" : start_u, "end_u" : end_u, "max_deflect" : max_deflect, **kwargs})

class fillet3pts(OpenSCADObject):
    def __init__(self, p0=None, p1=None, p2=None, r=None, maxerr=None, w=None, dw=None, **kwargs):
       super().__init__("fillet3pts", {"p0" : p0, "p1" : p1, "p2" : p2, "r" : r, "maxerr" : maxerr, "w" : w, "dw" : dw, **kwargs})

class bezier_path_point(OpenSCADObject):
    def __init__(self, path=None, seg=None, u=None, N=None, **kwargs):
       super().__init__("bezier_path_point", {"path" : path, "seg" : seg, "u" : u, "N" : N, **kwargs})

class bezier_path_closest_point(OpenSCADObject):
    def __init__(self, path=None, pt=None, N=None, max_err=None, seg=None, min_seg=None, min_u=None, min_dist=None, **kwargs):
       super().__init__("bezier_path_closest_point", {"path" : path, "pt" : pt, "N" : N, "max_err" : max_err, "seg" : seg, "min_seg" : min_seg, "min_u" : min_u, "min_dist" : min_dist, **kwargs})

class bezier_path_length(OpenSCADObject):
    def __init__(self, path=None, N=None, max_deflect=None, **kwargs):
       super().__init__("bezier_path_length", {"path" : path, "N" : N, "max_deflect" : max_deflect, **kwargs})

class bezier_polyline(OpenSCADObject):
    def __init__(self, bezier=None, splinesteps=None, N=None, **kwargs):
       super().__init__("bezier_polyline", {"bezier" : bezier, "splinesteps" : splinesteps, "N" : N, **kwargs})

class fillet_path(OpenSCADObject):
    def __init__(self, pts=None, fillet=None, maxerr=None, **kwargs):
       super().__init__("fillet_path", {"pts" : pts, "fillet" : fillet, "maxerr" : maxerr, **kwargs})

class bezier_close_to_axis(OpenSCADObject):
    def __init__(self, bezier=None, N=None, axis=None, **kwargs):
       super().__init__("bezier_close_to_axis", {"bezier" : bezier, "N" : N, "axis" : axis, **kwargs})

class bezier_offset(OpenSCADObject):
    def __init__(self, inset=None, bezier=None, N=None, axis=None, **kwargs):
       super().__init__("bezier_offset", {"inset" : inset, "bezier" : bezier, "N" : N, "axis" : axis, **kwargs})

class bezier_patch_point(OpenSCADObject):
    def __init__(self, patch=None, u=None, v=None, **kwargs):
       super().__init__("bezier_patch_point", {"patch" : patch, "u" : u, "v" : v, **kwargs})

class bezier_triangle_point(OpenSCADObject):
    def __init__(self, tri=None, u=None, v=None, **kwargs):
       super().__init__("bezier_triangle_point", {"tri" : tri, "u" : u, "v" : v, **kwargs})

class bezier_patch(OpenSCADObject):
    def __init__(self, patch=None, splinesteps=None, vertices=None, faces=None, **kwargs):
       super().__init__("bezier_patch", {"patch" : patch, "splinesteps" : splinesteps, "vertices" : vertices, "faces" : faces, **kwargs})

class _tri_count(OpenSCADObject):
    def __init__(self, n=None, **kwargs):
       super().__init__("_tri_count", {"n" : n, **kwargs})

class bezier_triangle(OpenSCADObject):
    def __init__(self, tri=None, splinesteps=None, vertices=None, faces=None, **kwargs):
       super().__init__("bezier_triangle", {"tri" : tri, "splinesteps" : splinesteps, "vertices" : vertices, "faces" : faces, **kwargs})

class bezier_patch_flat(OpenSCADObject):
    def __init__(self, size=None, N=None, orient=None, trans=None, **kwargs):
       super().__init__("bezier_patch_flat", {"size" : size, "N" : N, "orient" : orient, "trans" : trans, **kwargs})

class patch_reverse(OpenSCADObject):
    def __init__(self, patch=None, **kwargs):
       super().__init__("patch_reverse", {"patch" : patch, **kwargs})

class patch_translate(OpenSCADObject):
    def __init__(self, patch=None, v=None, **kwargs):
       super().__init__("patch_translate", {"patch" : patch, "v" : v, **kwargs})

class patch_scale(OpenSCADObject):
    def __init__(self, patch=None, v=None, cp=None, **kwargs):
       super().__init__("patch_scale", {"patch" : patch, "v" : v, "cp" : cp, **kwargs})

class patch_rotate(OpenSCADObject):
    def __init__(self, patch=None, a=None, v=None, cp=None, **kwargs):
       super().__init__("patch_rotate", {"patch" : patch, "a" : a, "v" : v, "cp" : cp, **kwargs})

class patches_translate(OpenSCADObject):
    def __init__(self, patches=None, v=None, **kwargs):
       super().__init__("patches_translate", {"patches" : patches, "v" : v, **kwargs})

class patches_scale(OpenSCADObject):
    def __init__(self, patches=None, v=None, cp=None, **kwargs):
       super().__init__("patches_scale", {"patches" : patches, "v" : v, "cp" : cp, **kwargs})

class patches_rotate(OpenSCADObject):
    def __init__(self, patches=None, a=None, v=None, cp=None, **kwargs):
       super().__init__("patches_rotate", {"patches" : patches, "a" : a, "v" : v, "cp" : cp, **kwargs})

class bezier_surface(OpenSCADObject):
    def __init__(self, patches=None, tris=None, splinesteps=None, i=None, vertices=None, faces=None, **kwargs):
       super().__init__("bezier_surface", {"patches" : patches, "tris" : tris, "splinesteps" : splinesteps, "i" : i, "vertices" : vertices, "faces" : faces, **kwargs})

