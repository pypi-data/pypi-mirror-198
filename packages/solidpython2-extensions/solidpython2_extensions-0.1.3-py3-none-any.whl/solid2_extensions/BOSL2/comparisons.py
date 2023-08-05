from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/comparisons.scad'}", use_not_include=False)

class approx(OpenSCADObject):
    def __init__(self, a=None, b=None, eps=None, **kwargs):
       super().__init__("approx", {"a" : a, "b" : b, "eps" : eps, **kwargs})

class all_zero(OpenSCADObject):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_zero", {"x" : x, "eps" : eps, **kwargs})

class all_nonzero(OpenSCADObject):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_nonzero", {"x" : x, "eps" : eps, **kwargs})

class all_positive(OpenSCADObject):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_positive", {"x" : x, "eps" : eps, **kwargs})

class all_negative(OpenSCADObject):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_negative", {"x" : x, "eps" : eps, **kwargs})

class all_nonpositive(OpenSCADObject):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_nonpositive", {"x" : x, "eps" : eps, **kwargs})

class all_nonnegative(OpenSCADObject):
    def __init__(self, x=None, eps=None, **kwargs):
       super().__init__("all_nonnegative", {"x" : x, "eps" : eps, **kwargs})

class all_equal(OpenSCADObject):
    def __init__(self, vec=None, eps=None, **kwargs):
       super().__init__("all_equal", {"vec" : vec, "eps" : eps, **kwargs})

class is_increasing(OpenSCADObject):
    def __init__(self, list=None, strict=None, **kwargs):
       super().__init__("is_increasing", {"list" : list, "strict" : strict, **kwargs})

class is_decreasing(OpenSCADObject):
    def __init__(self, list=None, strict=None, **kwargs):
       super().__init__("is_decreasing", {"list" : list, "strict" : strict, **kwargs})

class _type_num(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("_type_num", {"x" : x, **kwargs})

class compare_vals(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("compare_vals", {"a" : a, "b" : b, **kwargs})

class compare_lists(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("compare_lists", {"a" : a, "b" : b, **kwargs})

class min_index(OpenSCADObject):
    def __init__(self, vals=None, all=None, **kwargs):
       super().__init__("min_index", {"vals" : vals, "all" : all, **kwargs})

class max_index(OpenSCADObject):
    def __init__(self, vals=None, all=None, **kwargs):
       super().__init__("max_index", {"vals" : vals, "all" : all, **kwargs})

class find_approx(OpenSCADObject):
    def __init__(self, val=None, list=None, start=None, all=None, eps=None, **kwargs):
       super().__init__("find_approx", {"val" : val, "list" : list, "start" : start, "all" : all, "eps" : eps, **kwargs})

class __find_approx(OpenSCADObject):
    def __init__(self, val=None, list=None, eps=None, i=None, **kwargs):
       super().__init__("__find_approx", {"val" : val, "list" : list, "eps" : eps, "i" : i, **kwargs})

class deduplicate(OpenSCADObject):
    def __init__(self, list=None, closed=None, eps=None, **kwargs):
       super().__init__("deduplicate", {"list" : list, "closed" : closed, "eps" : eps, **kwargs})

class deduplicate_indexed(OpenSCADObject):
    def __init__(self, list=None, indices=None, closed=None, eps=None, **kwargs):
       super().__init__("deduplicate_indexed", {"list" : list, "indices" : indices, "closed" : closed, "eps" : eps, **kwargs})

class unique(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("unique", {"list" : list, **kwargs})

class _unique_sort(OpenSCADObject):
    def __init__(self, l=None, **kwargs):
       super().__init__("_unique_sort", {"l" : l, **kwargs})

class unique_count(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("unique_count", {"list" : list, **kwargs})

class _valid_idx(OpenSCADObject):
    def __init__(self, idx=None, imin=None, imax=None, **kwargs):
       super().__init__("_valid_idx", {"idx" : idx, "imin" : imin, "imax" : imax, **kwargs})

class _group_sort_by_index(OpenSCADObject):
    def __init__(self, l=None, idx=None, **kwargs):
       super().__init__("_group_sort_by_index", {"l" : l, "idx" : idx, **kwargs})

class _group_sort(OpenSCADObject):
    def __init__(self, l=None, **kwargs):
       super().__init__("_group_sort", {"l" : l, **kwargs})

class _sort_scalars(OpenSCADObject):
    def __init__(self, arr=None, **kwargs):
       super().__init__("_sort_scalars", {"arr" : arr, **kwargs})

class _sort_vectors(OpenSCADObject):
    def __init__(self, arr=None, _i=None, **kwargs):
       super().__init__("_sort_vectors", {"arr" : arr, "_i" : _i, **kwargs})

class _sort_vectors(OpenSCADObject):
    def __init__(self, arr=None, idxlist=None, _i=None, **kwargs):
       super().__init__("_sort_vectors", {"arr" : arr, "idxlist" : idxlist, "_i" : _i, **kwargs})

class _sort_general(OpenSCADObject):
    def __init__(self, arr=None, idx=None, indexed=None, **kwargs):
       super().__init__("_sort_general", {"arr" : arr, "idx" : idx, "indexed" : indexed, **kwargs})

class _lexical_sort(OpenSCADObject):
    def __init__(self, arr=None, **kwargs):
       super().__init__("_lexical_sort", {"arr" : arr, **kwargs})

class _indexed_sort(OpenSCADObject):
    def __init__(self, arrind=None, **kwargs):
       super().__init__("_indexed_sort", {"arrind" : arrind, **kwargs})

class sort(OpenSCADObject):
    def __init__(self, list=None, idx=None, **kwargs):
       super().__init__("sort", {"list" : list, "idx" : idx, **kwargs})

class sortidx(OpenSCADObject):
    def __init__(self, list=None, idx=None, **kwargs):
       super().__init__("sortidx", {"list" : list, "idx" : idx, **kwargs})

class group_sort(OpenSCADObject):
    def __init__(self, list=None, idx=None, **kwargs):
       super().__init__("group_sort", {"list" : list, "idx" : idx, **kwargs})

class group_data(OpenSCADObject):
    def __init__(self, groups=None, values=None, **kwargs):
       super().__init__("group_data", {"groups" : groups, "values" : values, **kwargs})

class list_smallest(OpenSCADObject):
    def __init__(self, list=None, k=None, **kwargs):
       super().__init__("list_smallest", {"list" : list, "k" : k, **kwargs})

