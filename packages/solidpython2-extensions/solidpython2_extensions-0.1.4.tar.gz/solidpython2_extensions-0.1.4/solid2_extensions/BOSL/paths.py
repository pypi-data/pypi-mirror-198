from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/paths.scad'}", use_not_include=True)

class modulated_circle(OpenSCADObject):
    def __init__(self, r=None, sines=None, **kwargs):
       super().__init__("modulated_circle", {"r" : r, "sines" : sines, **kwargs})

class extrude_from_to(OpenSCADObject):
    def __init__(self, pt1=None, pt2=None, convexity=None, twist=None, scale=None, slices=None, **kwargs):
       super().__init__("extrude_from_to", {"pt1" : pt1, "pt2" : pt2, "convexity" : convexity, "twist" : twist, "scale" : scale, "slices" : slices, **kwargs})

class extrude_2d_hollow(OpenSCADObject):
    def __init__(self, wall=None, height=None, twist=None, slices=None, center=None, orient=None, align=None, **kwargs):
       super().__init__("extrude_2d_hollow", {"wall" : wall, "height" : height, "twist" : twist, "slices" : slices, "center" : center, "orient" : orient, "align" : align, **kwargs})

class extrude_2dpath_along_spiral(OpenSCADObject):
    def __init__(self, polyline=None, h=None, r=None, twist=None, center=None, orient=None, align=None, **kwargs):
       super().__init__("extrude_2dpath_along_spiral", {"polyline" : polyline, "h" : h, "r" : r, "twist" : twist, "center" : center, "orient" : orient, "align" : align, **kwargs})

class extrude_2dpath_along_3dpath(OpenSCADObject):
    def __init__(self, polyline=None, path=None, ang=None, convexity=None, **kwargs):
       super().__init__("extrude_2dpath_along_3dpath", {"polyline" : polyline, "path" : path, "ang" : ang, "convexity" : convexity, **kwargs})

class extrude_2d_shapes_along_3dpath(OpenSCADObject):
    def __init__(self, path=None, convexity=None, clipsize=None, **kwargs):
       super().__init__("extrude_2d_shapes_along_3dpath", {"path" : path, "convexity" : convexity, "clipsize" : clipsize, **kwargs})

class trace_polyline(OpenSCADObject):
    def __init__(self, pline=None, N=None, showpts=None, size=None, color=None, **kwargs):
       super().__init__("trace_polyline", {"pline" : pline, "N" : N, "showpts" : showpts, "size" : size, "color" : color, **kwargs})

class debug_polygon(OpenSCADObject):
    def __init__(self, points=None, paths=None, convexity=None, size=None, **kwargs):
       super().__init__("debug_polygon", {"points" : points, "paths" : paths, "convexity" : convexity, "size" : size, **kwargs})

class simplify2d_path(OpenSCADObject):
    def __init__(self, path=None, eps=None, **kwargs):
       super().__init__("simplify2d_path", {"path" : path, "eps" : eps, **kwargs})

class simplify3d_path(OpenSCADObject):
    def __init__(self, path=None, eps=None, **kwargs):
       super().__init__("simplify3d_path", {"path" : path, "eps" : eps, **kwargs})

class path_length(OpenSCADObject):
    def __init__(self, path=None, **kwargs):
       super().__init__("path_length", {"path" : path, **kwargs})

class path2d_regular_ngon(OpenSCADObject):
    def __init__(self, n=None, r=None, d=None, cp=None, scale=None, **kwargs):
       super().__init__("path2d_regular_ngon", {"n" : n, "r" : r, "d" : d, "cp" : cp, "scale" : scale, **kwargs})

class path3d_spiral(OpenSCADObject):
    def __init__(self, turns=None, h=None, n=None, r=None, d=None, cp=None, scale=None, **kwargs):
       super().__init__("path3d_spiral", {"turns" : turns, "h" : h, "n" : n, "r" : r, "d" : d, "cp" : cp, "scale" : scale, **kwargs})

class points_along_path3d(OpenSCADObject):
    def __init__(self, polyline=None, path=None, q=None, n=None, **kwargs):
       super().__init__("points_along_path3d", {"polyline" : polyline, "path" : path, "q" : q, "n" : n, **kwargs})

