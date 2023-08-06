from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/math.scad'}", use_not_include=True)

PHI = OpenSCADConstant('PHI')
EPSILON = OpenSCADConstant('EPSILON')
class Cpi(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("Cpi", {**kwargs})

class quant(OpenSCADObject):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quant", {"x" : x, "y" : y, **kwargs})

class quantdn(OpenSCADObject):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quantdn", {"x" : x, "y" : y, **kwargs})

class quantup(OpenSCADObject):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("quantup", {"x" : x, "y" : y, **kwargs})

class constrain(OpenSCADObject):
    def __init__(self, v=None, minval=None, maxval=None, **kwargs):
       super().__init__("constrain", {"v" : v, "minval" : minval, "maxval" : maxval, **kwargs})

class min_index(OpenSCADObject):
    def __init__(self, vals=None, _minval=None, _minidx=None, _i=None, **kwargs):
       super().__init__("min_index", {"vals" : vals, "_minval" : _minval, "_minidx" : _minidx, "_i" : _i, **kwargs})

class max_index(OpenSCADObject):
    def __init__(self, vals=None, _maxval=None, _maxidx=None, _i=None, **kwargs):
       super().__init__("max_index", {"vals" : vals, "_maxval" : _maxval, "_maxidx" : _maxidx, "_i" : _i, **kwargs})

class posmod(OpenSCADObject):
    def __init__(self, x=None, m=None, **kwargs):
       super().__init__("posmod", {"x" : x, "m" : m, **kwargs})

class modrange(OpenSCADObject):
    def __init__(self, x=None, y=None, m=None, step=None, **kwargs):
       super().__init__("modrange", {"x" : x, "y" : y, "m" : m, "step" : step, **kwargs})

class gaussian_rand(OpenSCADObject):
    def __init__(self, mean=None, stddev=None, **kwargs):
       super().__init__("gaussian_rand", {"mean" : mean, "stddev" : stddev, **kwargs})

class log_rand(OpenSCADObject):
    def __init__(self, minval=None, maxval=None, factor=None, **kwargs):
       super().__init__("log_rand", {"minval" : minval, "maxval" : maxval, "factor" : factor, **kwargs})

class segs(OpenSCADObject):
    def __init__(self, r=None, **kwargs):
       super().__init__("segs", {"r" : r, **kwargs})

class lerp(OpenSCADObject):
    def __init__(self, a=None, b=None, u=None, **kwargs):
       super().__init__("lerp", {"a" : a, "b" : b, "u" : u, **kwargs})

class hypot(OpenSCADObject):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("hypot", {"x" : x, "y" : y, "z" : z, **kwargs})

class hypot3(OpenSCADObject):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("hypot3", {"x" : x, "y" : y, "z" : z, **kwargs})

class distance(OpenSCADObject):
    def __init__(self, p1=None, p2=None, **kwargs):
       super().__init__("distance", {"p1" : p1, "p2" : p2, **kwargs})

class sinh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("sinh", {"x" : x, **kwargs})

class cosh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("cosh", {"x" : x, **kwargs})

class tanh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("tanh", {"x" : x, **kwargs})

class asinh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("asinh", {"x" : x, **kwargs})

class acosh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("acosh", {"x" : x, **kwargs})

class atanh(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("atanh", {"x" : x, **kwargs})

class sum(OpenSCADObject):
    def __init__(self, v=None, i=None, tot=None, **kwargs):
       super().__init__("sum", {"v" : v, "i" : i, "tot" : tot, **kwargs})

class sum_of_squares(OpenSCADObject):
    def __init__(self, v=None, i=None, tot=None, **kwargs):
       super().__init__("sum_of_squares", {"v" : v, "i" : i, "tot" : tot, **kwargs})

class sum_of_sines(OpenSCADObject):
    def __init__(self, a=None, sines=None, **kwargs):
       super().__init__("sum_of_sines", {"a" : a, "sines" : sines, **kwargs})

class mean(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("mean", {"v" : v, **kwargs})

class compare_vals(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("compare_vals", {"a" : a, "b" : b, **kwargs})

class compare_lists(OpenSCADObject):
    def __init__(self, a=None, b=None, n=None, **kwargs):
       super().__init__("compare_lists", {"a" : a, "b" : b, "n" : n, **kwargs})

class any(OpenSCADObject):
    def __init__(self, l=None, i=None, succ=None, **kwargs):
       super().__init__("any", {"l" : l, "i" : i, "succ" : succ, **kwargs})

class all(OpenSCADObject):
    def __init__(self, l=None, i=None, fail=None, **kwargs):
       super().__init__("all", {"l" : l, "i" : i, "fail" : fail, **kwargs})

class count_true(OpenSCADObject):
    def __init__(self, l=None, nmax=None, i=None, cnt=None, **kwargs):
       super().__init__("count_true", {"l" : l, "nmax" : nmax, "i" : i, "cnt" : cnt, **kwargs})

class cdr(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("cdr", {"list" : list, **kwargs})

class replist(OpenSCADObject):
    def __init__(self, val=None, n=None, i=None, **kwargs):
       super().__init__("replist", {"val" : val, "n" : n, "i" : i, **kwargs})

class in_list(OpenSCADObject):
    def __init__(self, x=None, l=None, idx=None, **kwargs):
       super().__init__("in_list", {"x" : x, "l" : l, "idx" : idx, **kwargs})

class slice(OpenSCADObject):
    def __init__(self, arr=None, st=None, end=None, **kwargs):
       super().__init__("slice", {"arr" : arr, "st" : st, "end" : end, **kwargs})

class wrap_range(OpenSCADObject):
    def __init__(self, list=None, start=None, end=None, **kwargs):
       super().__init__("wrap_range", {"list" : list, "start" : start, "end" : end, **kwargs})

class select(OpenSCADObject):
    def __init__(self, list=None, start=None, end=None, **kwargs):
       super().__init__("select", {"list" : list, "start" : start, "end" : end, **kwargs})

class reverse(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("reverse", {"list" : list, **kwargs})

class array_subindex(OpenSCADObject):
    def __init__(self, v=None, idx=None, **kwargs):
       super().__init__("array_subindex", {"v" : v, "idx" : idx, **kwargs})

class list_range(OpenSCADObject):
    def __init__(self, n=None, s=None, e=None, step=None, **kwargs):
       super().__init__("list_range", {"n" : n, "s" : s, "e" : e, "step" : step, **kwargs})

class array_shortest(OpenSCADObject):
    def __init__(self, vecs=None, **kwargs):
       super().__init__("array_shortest", {"vecs" : vecs, **kwargs})

class array_longest(OpenSCADObject):
    def __init__(self, vecs=None, **kwargs):
       super().__init__("array_longest", {"vecs" : vecs, **kwargs})

class array_pad(OpenSCADObject):
    def __init__(self, v=None, minlen=None, fill=None, **kwargs):
       super().__init__("array_pad", {"v" : v, "minlen" : minlen, "fill" : fill, **kwargs})

class array_trim(OpenSCADObject):
    def __init__(self, v=None, maxlen=None, **kwargs):
       super().__init__("array_trim", {"v" : v, "maxlen" : maxlen, **kwargs})

class array_fit(OpenSCADObject):
    def __init__(self, v=None, length=None, fill=None, **kwargs):
       super().__init__("array_fit", {"v" : v, "length" : length, "fill" : fill, **kwargs})

class enumerate(OpenSCADObject):
    def __init__(self, l=None, idx=None, **kwargs):
       super().__init__("enumerate", {"l" : l, "idx" : idx, **kwargs})

class array_zip(OpenSCADObject):
    def __init__(self, vecs=None, v2=None, v3=None, fit=None, fill=None, **kwargs):
       super().__init__("array_zip", {"vecs" : vecs, "v2" : v2, "v3" : v3, "fit" : fit, "fill" : fill, **kwargs})

class array_group(OpenSCADObject):
    def __init__(self, v=None, cnt=None, dflt=None, **kwargs):
       super().__init__("array_group", {"v" : v, "cnt" : cnt, "dflt" : dflt, **kwargs})

class flatten(OpenSCADObject):
    def __init__(self, l=None, **kwargs):
       super().__init__("flatten", {"l" : l, **kwargs})

class sort(OpenSCADObject):
    def __init__(self, arr=None, idx=None, **kwargs):
       super().__init__("sort", {"arr" : arr, "idx" : idx, **kwargs})

class sortidx(OpenSCADObject):
    def __init__(self, l=None, idx=None, **kwargs):
       super().__init__("sortidx", {"l" : l, "idx" : idx, **kwargs})

class unique(OpenSCADObject):
    def __init__(self, arr=None, **kwargs):
       super().__init__("unique", {"arr" : arr, **kwargs})

class list_remove(OpenSCADObject):
    def __init__(self, list=None, elements=None, **kwargs):
       super().__init__("list_remove", {"list" : list, "elements" : elements, **kwargs})

class _array_dim_recurse(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_array_dim_recurse", {"v" : v, **kwargs})

class array_dim(OpenSCADObject):
    def __init__(self, v=None, depth=None, **kwargs):
       super().__init__("array_dim", {"v" : v, "depth" : depth, **kwargs})

class vmul(OpenSCADObject):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("vmul", {"v1" : v1, "v2" : v2, **kwargs})

class vdiv(OpenSCADObject):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("vdiv", {"v1" : v1, "v2" : v2, **kwargs})

class vabs(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("vabs", {"v" : v, **kwargs})

class normalize(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("normalize", {"v" : v, **kwargs})

class vector2d_angle(OpenSCADObject):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("vector2d_angle", {"v1" : v1, "v2" : v2, **kwargs})

class vector3d_angle(OpenSCADObject):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("vector3d_angle", {"v1" : v1, "v2" : v2, **kwargs})

class vector_angle(OpenSCADObject):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("vector_angle", {"v1" : v1, "v2" : v2, **kwargs})

class vector_axis(OpenSCADObject):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("vector_axis", {"v1" : v1, "v2" : v2, **kwargs})

class point2d(OpenSCADObject):
    def __init__(self, p=None, **kwargs):
       super().__init__("point2d", {"p" : p, **kwargs})

class path2d(OpenSCADObject):
    def __init__(self, points=None, **kwargs):
       super().__init__("path2d", {"points" : points, **kwargs})

class point3d(OpenSCADObject):
    def __init__(self, p=None, **kwargs):
       super().__init__("point3d", {"p" : p, **kwargs})

class path3d(OpenSCADObject):
    def __init__(self, points=None, **kwargs):
       super().__init__("path3d", {"points" : points, **kwargs})

class translate_points(OpenSCADObject):
    def __init__(self, pts=None, v=None, **kwargs):
       super().__init__("translate_points", {"pts" : pts, "v" : v, **kwargs})

class scale_points(OpenSCADObject):
    def __init__(self, pts=None, v=None, cp=None, **kwargs):
       super().__init__("scale_points", {"pts" : pts, "v" : v, "cp" : cp, **kwargs})

class rotate_points2d(OpenSCADObject):
    def __init__(self, pts=None, ang=None, cp=None, **kwargs):
       super().__init__("rotate_points2d", {"pts" : pts, "ang" : ang, "cp" : cp, **kwargs})

class rotate_points3d(OpenSCADObject):
    def __init__(self, pts=None, v=None, cp=None, axis=None, _from=None, to=None, reverse=None, **kwargs):
       super().__init__("rotate_points3d", {"pts" : pts, "v" : v, "cp" : cp, "axis" : axis, "_from" : _from, "to" : to, "reverse" : reverse, **kwargs})

class rotate_points3d_around_axis(OpenSCADObject):
    def __init__(self, pts=None, ang=None, u=None, cp=None, **kwargs):
       super().__init__("rotate_points3d_around_axis", {"pts" : pts, "ang" : ang, "u" : u, "cp" : cp, **kwargs})

class polar_to_xy(OpenSCADObject):
    def __init__(self, r=None, theta=None, **kwargs):
       super().__init__("polar_to_xy", {"r" : r, "theta" : theta, **kwargs})

class xy_to_polar(OpenSCADObject):
    def __init__(self, x=None, y=None, **kwargs):
       super().__init__("xy_to_polar", {"x" : x, "y" : y, **kwargs})

class xyz_to_planar(OpenSCADObject):
    def __init__(self, point=None, a=None, b=None, c=None, **kwargs):
       super().__init__("xyz_to_planar", {"point" : point, "a" : a, "b" : b, "c" : c, **kwargs})

class planar_to_xyz(OpenSCADObject):
    def __init__(self, point=None, a=None, b=None, c=None, **kwargs):
       super().__init__("planar_to_xyz", {"point" : point, "a" : a, "b" : b, "c" : c, **kwargs})

class cylindrical_to_xyz(OpenSCADObject):
    def __init__(self, r=None, theta=None, z=None, **kwargs):
       super().__init__("cylindrical_to_xyz", {"r" : r, "theta" : theta, "z" : z, **kwargs})

class xyz_to_cylindrical(OpenSCADObject):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("xyz_to_cylindrical", {"x" : x, "y" : y, "z" : z, **kwargs})

class spherical_to_xyz(OpenSCADObject):
    def __init__(self, r=None, theta=None, phi=None, **kwargs):
       super().__init__("spherical_to_xyz", {"r" : r, "theta" : theta, "phi" : phi, **kwargs})

class xyz_to_spherical(OpenSCADObject):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("xyz_to_spherical", {"x" : x, "y" : y, "z" : z, **kwargs})

class altaz_to_xyz(OpenSCADObject):
    def __init__(self, alt=None, az=None, r=None, **kwargs):
       super().__init__("altaz_to_xyz", {"alt" : alt, "az" : az, "r" : r, **kwargs})

class xyz_to_altaz(OpenSCADObject):
    def __init__(self, x=None, y=None, z=None, **kwargs):
       super().__init__("xyz_to_altaz", {"x" : x, "y" : y, "z" : z, **kwargs})

class ident(OpenSCADObject):
    def __init__(self, n=None, **kwargs):
       super().__init__("ident", {"n" : n, **kwargs})

class matrix_transpose(OpenSCADObject):
    def __init__(self, m=None, **kwargs):
       super().__init__("matrix_transpose", {"m" : m, **kwargs})

class mat3_to_mat4(OpenSCADObject):
    def __init__(self, m=None, **kwargs):
       super().__init__("mat3_to_mat4", {"m" : m, **kwargs})

class matrix3_translate(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("matrix3_translate", {"v" : v, **kwargs})

class matrix4_translate(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("matrix4_translate", {"v" : v, **kwargs})

class matrix3_scale(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("matrix3_scale", {"v" : v, **kwargs})

class matrix4_scale(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("matrix4_scale", {"v" : v, **kwargs})

class matrix3_zrot(OpenSCADObject):
    def __init__(self, ang=None, **kwargs):
       super().__init__("matrix3_zrot", {"ang" : ang, **kwargs})

class matrix4_xrot(OpenSCADObject):
    def __init__(self, ang=None, **kwargs):
       super().__init__("matrix4_xrot", {"ang" : ang, **kwargs})

class matrix4_yrot(OpenSCADObject):
    def __init__(self, ang=None, **kwargs):
       super().__init__("matrix4_yrot", {"ang" : ang, **kwargs})

class matrix4_zrot(OpenSCADObject):
    def __init__(self, ang=None, **kwargs):
       super().__init__("matrix4_zrot", {"ang" : ang, **kwargs})

class matrix4_rot_by_axis(OpenSCADObject):
    def __init__(self, u=None, ang=None, **kwargs):
       super().__init__("matrix4_rot_by_axis", {"u" : u, "ang" : ang, **kwargs})

class matrix3_skew(OpenSCADObject):
    def __init__(self, xa=None, ya=None, **kwargs):
       super().__init__("matrix3_skew", {"xa" : xa, "ya" : ya, **kwargs})

class matrix4_skew_xy(OpenSCADObject):
    def __init__(self, xa=None, ya=None, **kwargs):
       super().__init__("matrix4_skew_xy", {"xa" : xa, "ya" : ya, **kwargs})

class matrix4_skew_xz(OpenSCADObject):
    def __init__(self, xa=None, za=None, **kwargs):
       super().__init__("matrix4_skew_xz", {"xa" : xa, "za" : za, **kwargs})

class matrix4_skew_yz(OpenSCADObject):
    def __init__(self, ya=None, za=None, **kwargs):
       super().__init__("matrix4_skew_yz", {"ya" : ya, "za" : za, **kwargs})

class matrix3_mult(OpenSCADObject):
    def __init__(self, matrices=None, m=None, i=None, **kwargs):
       super().__init__("matrix3_mult", {"matrices" : matrices, "m" : m, "i" : i, **kwargs})

class matrix4_mult(OpenSCADObject):
    def __init__(self, matrices=None, m=None, i=None, **kwargs):
       super().__init__("matrix4_mult", {"matrices" : matrices, "m" : m, "i" : i, **kwargs})

class matrix3_apply(OpenSCADObject):
    def __init__(self, pts=None, matrices=None, **kwargs):
       super().__init__("matrix3_apply", {"pts" : pts, "matrices" : matrices, **kwargs})

class matrix4_apply(OpenSCADObject):
    def __init__(self, pts=None, matrices=None, **kwargs):
       super().__init__("matrix4_apply", {"pts" : pts, "matrices" : matrices, **kwargs})

class point_on_segment(OpenSCADObject):
    def __init__(self, point=None, edge=None, **kwargs):
       super().__init__("point_on_segment", {"point" : point, "edge" : edge, **kwargs})

class point_left_of_segment(OpenSCADObject):
    def __init__(self, point=None, edge=None, **kwargs):
       super().__init__("point_left_of_segment", {"point" : point, "edge" : edge, **kwargs})

class _point_above_below_segment(OpenSCADObject):
    def __init__(self, point=None, edge=None, **kwargs):
       super().__init__("_point_above_below_segment", {"point" : point, "edge" : edge, **kwargs})

class point_in_polygon(OpenSCADObject):
    def __init__(self, point=None, path=None, **kwargs):
       super().__init__("point_in_polygon", {"point" : point, "path" : path, **kwargs})

class pointlist_bounds(OpenSCADObject):
    def __init__(self, pts=None, **kwargs):
       super().__init__("pointlist_bounds", {"pts" : pts, **kwargs})

class triangle_area2d(OpenSCADObject):
    def __init__(self, a=None, b=None, c=None, **kwargs):
       super().__init__("triangle_area2d", {"a" : a, "b" : b, "c" : c, **kwargs})

class right_of_line2d(OpenSCADObject):
    def __init__(self, line=None, pt=None, **kwargs):
       super().__init__("right_of_line2d", {"line" : line, "pt" : pt, **kwargs})

class collinear(OpenSCADObject):
    def __init__(self, a=None, b=None, c=None, eps=None, **kwargs):
       super().__init__("collinear", {"a" : a, "b" : b, "c" : c, "eps" : eps, **kwargs})

class collinear_indexed(OpenSCADObject):
    def __init__(self, points=None, a=None, b=None, c=None, eps=None, **kwargs):
       super().__init__("collinear_indexed", {"points" : points, "a" : a, "b" : b, "c" : c, "eps" : eps, **kwargs})

class plane3pt(OpenSCADObject):
    def __init__(self, p1=None, p2=None, p3=None, **kwargs):
       super().__init__("plane3pt", {"p1" : p1, "p2" : p2, "p3" : p3, **kwargs})

class plane3pt_indexed(OpenSCADObject):
    def __init__(self, points=None, i1=None, i2=None, i3=None, **kwargs):
       super().__init__("plane3pt_indexed", {"points" : points, "i1" : i1, "i2" : i2, "i3" : i3, **kwargs})

class distance_from_plane(OpenSCADObject):
    def __init__(self, plane=None, point=None, **kwargs):
       super().__init__("distance_from_plane", {"plane" : plane, "point" : point, **kwargs})

class coplanar(OpenSCADObject):
    def __init__(self, plane=None, point=None, **kwargs):
       super().__init__("coplanar", {"plane" : plane, "point" : point, **kwargs})

class in_front_of_plane(OpenSCADObject):
    def __init__(self, plane=None, point=None, **kwargs):
       super().__init__("in_front_of_plane", {"plane" : plane, "point" : point, **kwargs})

class simplify_path(OpenSCADObject):
    def __init__(self, path=None, eps=None, _a=None, _b=None, _acc=None, **kwargs):
       super().__init__("simplify_path", {"path" : path, "eps" : eps, "_a" : _a, "_b" : _b, "_acc" : _acc, **kwargs})

class simplify_path_indexed(OpenSCADObject):
    def __init__(self, points=None, path=None, eps=None, _a=None, _b=None, _acc=None, **kwargs):
       super().__init__("simplify_path_indexed", {"points" : points, "path" : path, "eps" : eps, "_a" : _a, "_b" : _b, "_acc" : _acc, **kwargs})

