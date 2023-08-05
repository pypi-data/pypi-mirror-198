from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/vnf.scad'}", use_not_include=False)

EMPTY_VNF = OpenSCADConstant('EMPTY_VNF')
_vnf_validate_errs = OpenSCADConstant('_vnf_validate_errs')
class vnf_polyhedron(OpenSCADObject):
    def __init__(self, vnf=None, convexity=None, extent=None, cp=None, anchor=None, spin=None, orient=None, atype=None, **kwargs):
       super().__init__("vnf_polyhedron", {"vnf" : vnf, "convexity" : convexity, "extent" : extent, "cp" : cp, "anchor" : anchor, "spin" : spin, "orient" : orient, "atype" : atype, **kwargs})

class vnf_wireframe(OpenSCADObject):
    def __init__(self, vnf=None, width=None, **kwargs):
       super().__init__("vnf_wireframe", {"vnf" : vnf, "width" : width, **kwargs})

class _show_vertices(OpenSCADObject):
    def __init__(self, vertices=None, size=None, **kwargs):
       super().__init__("_show_vertices", {"vertices" : vertices, "size" : size, **kwargs})

class _show_faces(OpenSCADObject):
    def __init__(self, vertices=None, faces=None, size=None, **kwargs):
       super().__init__("_show_faces", {"vertices" : vertices, "faces" : faces, "size" : size, **kwargs})

class debug_vnf(OpenSCADObject):
    def __init__(self, vnf=None, faces=None, vertices=None, opacity=None, size=None, convexity=None, **kwargs):
       super().__init__("debug_vnf", {"vnf" : vnf, "faces" : faces, "vertices" : vertices, "opacity" : opacity, "size" : size, "convexity" : convexity, **kwargs})

class vnf_validate(OpenSCADObject):
    def __init__(self, vnf=None, size=None, show_warns=None, check_isects=None, **kwargs):
       super().__init__("vnf_validate", {"vnf" : vnf, "size" : size, "show_warns" : show_warns, "check_isects" : check_isects, **kwargs})

class vnf_vertex_array(OpenSCADObject):
    def __init__(self, points=None, caps=None, cap1=None, cap2=None, col_wrap=None, row_wrap=None, reverse=None, style=None, **kwargs):
       super().__init__("vnf_vertex_array", {"points" : points, "caps" : caps, "cap1" : cap1, "cap2" : cap2, "col_wrap" : col_wrap, "row_wrap" : row_wrap, "reverse" : reverse, "style" : style, **kwargs})

class vnf_tri_array(OpenSCADObject):
    def __init__(self, points=None, row_wrap=None, reverse=None, **kwargs):
       super().__init__("vnf_tri_array", {"points" : points, "row_wrap" : row_wrap, "reverse" : reverse, **kwargs})

class vnf_join(OpenSCADObject):
    def __init__(self, vnfs=None, **kwargs):
       super().__init__("vnf_join", {"vnfs" : vnfs, **kwargs})

class vnf_from_polygons(OpenSCADObject):
    def __init__(self, polygons=None, **kwargs):
       super().__init__("vnf_from_polygons", {"polygons" : polygons, **kwargs})

class _path_path_closest_vertices(OpenSCADObject):
    def __init__(self, path1=None, path2=None, **kwargs):
       super().__init__("_path_path_closest_vertices", {"path1" : path1, "path2" : path2, **kwargs})

class _join_paths_at_vertices(OpenSCADObject):
    def __init__(self, path1=None, path2=None, v1=None, v2=None, **kwargs):
       super().__init__("_join_paths_at_vertices", {"path1" : path1, "path2" : path2, "v1" : v1, "v2" : v2, **kwargs})

class _cleave_connected_region(OpenSCADObject):
    def __init__(self, region=None, eps=None, **kwargs):
       super().__init__("_cleave_connected_region", {"region" : region, "eps" : eps, **kwargs})

class _polyHoles(OpenSCADObject):
    def __init__(self, outer=None, holes=None, extremes=None, eps=None, n=None, **kwargs):
       super().__init__("_polyHoles", {"outer" : outer, "holes" : holes, "extremes" : extremes, "eps" : eps, "n" : n, **kwargs})

class _bridge(OpenSCADObject):
    def __init__(self, pt=None, outer=None, eps=None, **kwargs):
       super().__init__("_bridge", {"pt" : pt, "outer" : outer, "eps" : eps, **kwargs})

class vnf_from_region(OpenSCADObject):
    def __init__(self, region=None, transform=None, reverse=None, **kwargs):
       super().__init__("vnf_from_region", {"region" : region, "transform" : transform, "reverse" : reverse, **kwargs})

class is_vnf(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_vnf", {"x" : x, **kwargs})

class is_vnf_list(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("is_vnf_list", {"x" : x, **kwargs})

class vnf_vertices(OpenSCADObject):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_vertices", {"vnf" : vnf, **kwargs})

class vnf_faces(OpenSCADObject):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_faces", {"vnf" : vnf, **kwargs})

class vnf_reverse_faces(OpenSCADObject):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_reverse_faces", {"vnf" : vnf, **kwargs})

class vnf_quantize(OpenSCADObject):
    def __init__(self, vnf=None, q=None, **kwargs):
       super().__init__("vnf_quantize", {"vnf" : vnf, "q" : q, **kwargs})

class vnf_merge_points(OpenSCADObject):
    def __init__(self, vnf=None, eps=None, **kwargs):
       super().__init__("vnf_merge_points", {"vnf" : vnf, "eps" : eps, **kwargs})

class vnf_drop_unused_points(OpenSCADObject):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_drop_unused_points", {"vnf" : vnf, **kwargs})

class _link_indicator(OpenSCADObject):
    def __init__(self, l=None, imin=None, imax=None, **kwargs):
       super().__init__("_link_indicator", {"l" : l, "imin" : imin, "imax" : imax, **kwargs})

class vnf_triangulate(OpenSCADObject):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_triangulate", {"vnf" : vnf, **kwargs})

class vnf_slice(OpenSCADObject):
    def __init__(self, vnf=None, dir=None, cuts=None, **kwargs):
       super().__init__("vnf_slice", {"vnf" : vnf, "dir" : dir, "cuts" : cuts, **kwargs})

class _split_polygon_at_x(OpenSCADObject):
    def __init__(self, poly=None, x=None, **kwargs):
       super().__init__("_split_polygon_at_x", {"poly" : poly, "x" : x, **kwargs})

class _split_2dpolygons_at_each_x(OpenSCADObject):
    def __init__(self, polys=None, xs=None, _i=None, **kwargs):
       super().__init__("_split_2dpolygons_at_each_x", {"polys" : polys, "xs" : xs, "_i" : _i, **kwargs})

class _slice_3dpolygons(OpenSCADObject):
    def __init__(self, polys=None, dir=None, cuts=None, **kwargs):
       super().__init__("_slice_3dpolygons", {"polys" : polys, "dir" : dir, "cuts" : cuts, **kwargs})

class vnf_volume(OpenSCADObject):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_volume", {"vnf" : vnf, **kwargs})

class vnf_area(OpenSCADObject):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("vnf_area", {"vnf" : vnf, **kwargs})

class _vnf_centroid(OpenSCADObject):
    def __init__(self, vnf=None, eps=None, **kwargs):
       super().__init__("_vnf_centroid", {"vnf" : vnf, "eps" : eps, **kwargs})

class vnf_halfspace(OpenSCADObject):
    def __init__(self, plane=None, vnf=None, closed=None, **kwargs):
       super().__init__("vnf_halfspace", {"plane" : plane, "vnf" : vnf, "closed" : closed, **kwargs})

class _assemble_paths(OpenSCADObject):
    def __init__(self, vertices=None, edges=None, paths=None, i=None, **kwargs):
       super().__init__("_assemble_paths", {"vertices" : vertices, "edges" : edges, "paths" : paths, "i" : i, **kwargs})

class _vnfcut(OpenSCADObject):
    def __init__(self, plane=None, vertices=None, vertexmap=None, inside=None, faces=None, vertcount=None, newfaces=None, newedges=None, newvertices=None, i=None, **kwargs):
       super().__init__("_vnfcut", {"plane" : plane, "vertices" : vertices, "vertexmap" : vertexmap, "inside" : inside, "faces" : faces, "vertcount" : vertcount, "newfaces" : newfaces, "newedges" : newedges, "newvertices" : newvertices, "i" : i, **kwargs})

class _triangulate_planar_convex_polygons(OpenSCADObject):
    def __init__(self, polys=None, **kwargs):
       super().__init__("_triangulate_planar_convex_polygons", {"polys" : polys, **kwargs})

class vnf_bend(OpenSCADObject):
    def __init__(self, vnf=None, r=None, d=None, axis=None, **kwargs):
       super().__init__("vnf_bend", {"vnf" : vnf, "r" : r, "d" : d, "axis" : axis, **kwargs})

class vnf_validate(OpenSCADObject):
    def __init__(self, vnf=None, show_warns=None, check_isects=None, **kwargs):
       super().__init__("vnf_validate", {"vnf" : vnf, "show_warns" : show_warns, "check_isects" : check_isects, **kwargs})

class _vnf_validate_err(OpenSCADObject):
    def __init__(self, name=None, extra=None, **kwargs):
       super().__init__("_vnf_validate_err", {"name" : name, "extra" : extra, **kwargs})

class _pts_not_reported(OpenSCADObject):
    def __init__(self, pts=None, varr=None, reports=None, **kwargs):
       super().__init__("_pts_not_reported", {"pts" : pts, "varr" : varr, "reports" : reports, **kwargs})

class _edge_not_reported(OpenSCADObject):
    def __init__(self, edge=None, varr=None, reports=None, **kwargs):
       super().__init__("_edge_not_reported", {"edge" : edge, "varr" : varr, "reports" : reports, **kwargs})

