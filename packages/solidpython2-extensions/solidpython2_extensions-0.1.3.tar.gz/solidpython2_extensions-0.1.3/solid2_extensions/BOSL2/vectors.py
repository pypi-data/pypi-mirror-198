from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/vectors.scad'}", use_not_include=False)

class is_vector(OpenSCADObject):
    def __init__(self, v=None, length=None, zero=None, all_nonzero=None, eps=None, **kwargs):
       super().__init__("is_vector", {"v" : v, "length" : length, "zero" : zero, "all_nonzero" : all_nonzero, "eps" : eps, **kwargs})

class add_scalar(OpenSCADObject):
    def __init__(self, v=None, s=None, **kwargs):
       super().__init__("add_scalar", {"v" : v, "s" : s, **kwargs})

class v_mul(OpenSCADObject):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("v_mul", {"v1" : v1, "v2" : v2, **kwargs})

class v_div(OpenSCADObject):
    def __init__(self, v1=None, v2=None, **kwargs):
       super().__init__("v_div", {"v1" : v1, "v2" : v2, **kwargs})

class v_abs(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_abs", {"v" : v, **kwargs})

class v_floor(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_floor", {"v" : v, **kwargs})

class v_ceil(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_ceil", {"v" : v, **kwargs})

class v_lookup(OpenSCADObject):
    def __init__(self, x=None, v=None, **kwargs):
       super().__init__("v_lookup", {"x" : x, "v" : v, **kwargs})

class unit(OpenSCADObject):
    def __init__(self, v=None, error=None, **kwargs):
       super().__init__("unit", {"v" : v, "error" : error, **kwargs})

class v_theta(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("v_theta", {"v" : v, **kwargs})

class vector_angle(OpenSCADObject):
    def __init__(self, v1=None, v2=None, v3=None, **kwargs):
       super().__init__("vector_angle", {"v1" : v1, "v2" : v2, "v3" : v3, **kwargs})

class vector_axis(OpenSCADObject):
    def __init__(self, v1=None, v2=None, v3=None, **kwargs):
       super().__init__("vector_axis", {"v1" : v1, "v2" : v2, "v3" : v3, **kwargs})

class pointlist_bounds(OpenSCADObject):
    def __init__(self, pts=None, **kwargs):
       super().__init__("pointlist_bounds", {"pts" : pts, **kwargs})

class closest_point(OpenSCADObject):
    def __init__(self, pt=None, points=None, **kwargs):
       super().__init__("closest_point", {"pt" : pt, "points" : points, **kwargs})

class furthest_point(OpenSCADObject):
    def __init__(self, pt=None, points=None, **kwargs):
       super().__init__("furthest_point", {"pt" : pt, "points" : points, **kwargs})

class vector_search(OpenSCADObject):
    def __init__(self, query=None, r=None, target=None, **kwargs):
       super().__init__("vector_search", {"query" : query, "r" : r, "target" : target, **kwargs})

class _bt_search(OpenSCADObject):
    def __init__(self, query=None, r=None, points=None, tree=None, **kwargs):
       super().__init__("_bt_search", {"query" : query, "r" : r, "points" : points, "tree" : tree, **kwargs})

class vector_search_tree(OpenSCADObject):
    def __init__(self, points=None, leafsize=None, treemin=None, **kwargs):
       super().__init__("vector_search_tree", {"points" : points, "leafsize" : leafsize, "treemin" : treemin, **kwargs})

class _bt_tree(OpenSCADObject):
    def __init__(self, points=None, ind=None, leafsize=None, **kwargs):
       super().__init__("_bt_tree", {"points" : points, "ind" : ind, "leafsize" : leafsize, **kwargs})

class vector_nearest(OpenSCADObject):
    def __init__(self, query=None, k=None, target=None, **kwargs):
       super().__init__("vector_nearest", {"query" : query, "k" : k, "target" : target, **kwargs})

class _bt_nearest(OpenSCADObject):
    def __init__(self, p=None, k=None, points=None, tree=None, answers=None, **kwargs):
       super().__init__("_bt_nearest", {"p" : p, "k" : k, "points" : points, "tree" : tree, "answers" : answers, **kwargs})

class _insert_sorted(OpenSCADObject):
    def __init__(self, list=None, k=None, new=None, **kwargs):
       super().__init__("_insert_sorted", {"list" : list, "k" : k, "new" : new, **kwargs})

class _insert_many(OpenSCADObject):
    def __init__(self, list=None, k=None, newlist=None, i=None, **kwargs):
       super().__init__("_insert_many", {"list" : list, "k" : k, "newlist" : newlist, "i" : i, **kwargs})

