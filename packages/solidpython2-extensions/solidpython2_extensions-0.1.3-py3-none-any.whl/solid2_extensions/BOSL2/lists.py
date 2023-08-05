from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/lists.scad'}", use_not_include=False)

class is_homogeneous(OpenSCADObject):
    def __init__(self, l=None, depth=None, **kwargs):
       super().__init__("is_homogeneous", {"l" : l, "depth" : depth, **kwargs})

class is_homogenous(OpenSCADObject):
    def __init__(self, l=None, depth=None, **kwargs):
       super().__init__("is_homogenous", {"l" : l, "depth" : depth, **kwargs})

class _same_type(OpenSCADObject):
    def __init__(self, a=None, b=None, depth=None, **kwargs):
       super().__init__("_same_type", {"a" : a, "b" : b, "depth" : depth, **kwargs})

class min_length(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("min_length", {"list" : list, **kwargs})

class max_length(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("max_length", {"list" : list, **kwargs})

class _list_shape_recurse(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_list_shape_recurse", {"v" : v, **kwargs})

class _list_shape_recurse(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_list_shape_recurse", {"v" : v, **kwargs})

class list_shape(OpenSCADObject):
    def __init__(self, v=None, depth=None, **kwargs):
       super().__init__("list_shape", {"v" : v, "depth" : depth, **kwargs})

class in_list(OpenSCADObject):
    def __init__(self, val=None, list=None, idx=None, **kwargs):
       super().__init__("in_list", {"val" : val, "list" : list, "idx" : idx, **kwargs})

class select(OpenSCADObject):
    def __init__(self, list=None, start=None, end=None, **kwargs):
       super().__init__("select", {"list" : list, "start" : start, "end" : end, **kwargs})

class slice(OpenSCADObject):
    def __init__(self, list=None, start=None, end=None, **kwargs):
       super().__init__("slice", {"list" : list, "start" : start, "end" : end, **kwargs})

class last(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("last", {"list" : list, **kwargs})

class list_head(OpenSCADObject):
    def __init__(self, list=None, to=None, **kwargs):
       super().__init__("list_head", {"list" : list, "to" : to, **kwargs})

class list_tail(OpenSCADObject):
    def __init__(self, list=None, _from=None, **kwargs):
       super().__init__("list_tail", {"list" : list, "_from" : _from, **kwargs})

class bselect(OpenSCADObject):
    def __init__(self, list=None, index=None, **kwargs):
       super().__init__("bselect", {"list" : list, "index" : index, **kwargs})

class repeat(OpenSCADObject):
    def __init__(self, val=None, n=None, i=None, **kwargs):
       super().__init__("repeat", {"val" : val, "n" : n, "i" : i, **kwargs})

class list_bset(OpenSCADObject):
    def __init__(self, indexset=None, valuelist=None, dflt=None, **kwargs):
       super().__init__("list_bset", {"indexset" : indexset, "valuelist" : valuelist, "dflt" : dflt, **kwargs})

class list(OpenSCADObject):
    def __init__(self, l=None, **kwargs):
       super().__init__("list", {"l" : l, **kwargs})

class force_list(OpenSCADObject):
    def __init__(self, value=None, n=None, fill=None, **kwargs):
       super().__init__("force_list", {"value" : value, "n" : n, "fill" : fill, **kwargs})

class reverse(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("reverse", {"list" : list, **kwargs})

class list_rotate(OpenSCADObject):
    def __init__(self, list=None, n=None, **kwargs):
       super().__init__("list_rotate", {"list" : list, "n" : n, **kwargs})

class shuffle(OpenSCADObject):
    def __init__(self, list=None, seed=None, **kwargs):
       super().__init__("shuffle", {"list" : list, "seed" : seed, **kwargs})

class repeat_entries(OpenSCADObject):
    def __init__(self, list=None, N=None, exact=None, **kwargs):
       super().__init__("repeat_entries", {"list" : list, "N" : N, "exact" : exact, **kwargs})

class list_pad(OpenSCADObject):
    def __init__(self, list=None, minlen=None, fill=None, **kwargs):
       super().__init__("list_pad", {"list" : list, "minlen" : minlen, "fill" : fill, **kwargs})

class list_set(OpenSCADObject):
    def __init__(self, list=None, indices=None, values=None, dflt=None, minlen=None, **kwargs):
       super().__init__("list_set", {"list" : list, "indices" : indices, "values" : values, "dflt" : dflt, "minlen" : minlen, **kwargs})

class list_insert(OpenSCADObject):
    def __init__(self, list=None, indices=None, values=None, **kwargs):
       super().__init__("list_insert", {"list" : list, "indices" : indices, "values" : values, **kwargs})

class list_remove(OpenSCADObject):
    def __init__(self, list=None, ind=None, **kwargs):
       super().__init__("list_remove", {"list" : list, "ind" : ind, **kwargs})

class list_remove_values(OpenSCADObject):
    def __init__(self, list=None, values=None, all=None, **kwargs):
       super().__init__("list_remove_values", {"list" : list, "values" : values, "all" : all, **kwargs})

class idx(OpenSCADObject):
    def __init__(self, list=None, s=None, e=None, step=None, **kwargs):
       super().__init__("idx", {"list" : list, "s" : s, "e" : e, "step" : step, **kwargs})

class pair(OpenSCADObject):
    def __init__(self, list=None, wrap=None, **kwargs):
       super().__init__("pair", {"list" : list, "wrap" : wrap, **kwargs})

class triplet(OpenSCADObject):
    def __init__(self, list=None, wrap=None, **kwargs):
       super().__init__("triplet", {"list" : list, "wrap" : wrap, **kwargs})

class combinations(OpenSCADObject):
    def __init__(self, l=None, n=None, _s=None, **kwargs):
       super().__init__("combinations", {"l" : l, "n" : n, "_s" : _s, **kwargs})

class permutations(OpenSCADObject):
    def __init__(self, l=None, n=None, **kwargs):
       super().__init__("permutations", {"l" : l, "n" : n, **kwargs})

class list_to_matrix(OpenSCADObject):
    def __init__(self, v=None, cnt=None, dflt=None, **kwargs):
       super().__init__("list_to_matrix", {"v" : v, "cnt" : cnt, "dflt" : dflt, **kwargs})

class flatten(OpenSCADObject):
    def __init__(self, l=None, **kwargs):
       super().__init__("flatten", {"l" : l, **kwargs})

class full_flatten(OpenSCADObject):
    def __init__(self, l=None, **kwargs):
       super().__init__("full_flatten", {"l" : l, **kwargs})

class set_union(OpenSCADObject):
    def __init__(self, a=None, b=None, get_indices=None, **kwargs):
       super().__init__("set_union", {"a" : a, "b" : b, "get_indices" : get_indices, **kwargs})

class set_difference(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("set_difference", {"a" : a, "b" : b, **kwargs})

class set_intersection(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("set_intersection", {"a" : a, "b" : b, **kwargs})

