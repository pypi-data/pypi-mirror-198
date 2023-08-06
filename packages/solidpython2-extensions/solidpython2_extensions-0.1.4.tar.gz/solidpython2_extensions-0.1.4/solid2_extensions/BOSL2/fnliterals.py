from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/fnliterals.scad'}", use_not_include=False)

class map(OpenSCADObject):
    def __init__(self, func=None, list=None, **kwargs):
       super().__init__("map", {"func" : func, "list" : list, **kwargs})

class filter(OpenSCADObject):
    def __init__(self, func=None, list=None, **kwargs):
       super().__init__("filter", {"func" : func, "list" : list, **kwargs})

class reduce(OpenSCADObject):
    def __init__(self, func=None, list=None, init=None, **kwargs):
       super().__init__("reduce", {"func" : func, "list" : list, "init" : init, **kwargs})

class accumulate(OpenSCADObject):
    def __init__(self, func=None, list=None, init=None, **kwargs):
       super().__init__("accumulate", {"func" : func, "list" : list, "init" : init, **kwargs})

class _while(OpenSCADObject):
    def __init__(self, init=None, cond=None, func=None, **kwargs):
       super().__init__("_while", {"init" : init, "cond" : cond, "func" : func, **kwargs})

class for_n(OpenSCADObject):
    def __init__(self, n=None, init=None, func=None, **kwargs):
       super().__init__("for_n", {"n" : n, "init" : init, "func" : func, **kwargs})

class find_all(OpenSCADObject):
    def __init__(self, func=None, list=None, **kwargs):
       super().__init__("find_all", {"func" : func, "list" : list, **kwargs})

class find_first(OpenSCADObject):
    def __init__(self, func=None, list=None, start=None, **kwargs):
       super().__init__("find_first", {"func" : func, "list" : list, "start" : start, **kwargs})

class binsearch(OpenSCADObject):
    def __init__(self, key=None, list=None, idx=None, cmp=None, **kwargs):
       super().__init__("binsearch", {"key" : key, "list" : list, "idx" : idx, "cmp" : cmp, **kwargs})

class simple_hash(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("simple_hash", {"x" : x, **kwargs})

class hashmap(OpenSCADObject):
    def __init__(self, hashsize=None, items=None, table=None, **kwargs):
       super().__init__("hashmap", {"hashsize" : hashsize, "items" : items, "table" : table, **kwargs})

class f_1arg(OpenSCADObject):
    def __init__(self, target_func=None, **kwargs):
       super().__init__("f_1arg", {"target_func" : target_func, **kwargs})

class f_2arg(OpenSCADObject):
    def __init__(self, target_func=None, **kwargs):
       super().__init__("f_2arg", {"target_func" : target_func, **kwargs})

class f_2arg_simple(OpenSCADObject):
    def __init__(self, target_func=None, **kwargs):
       super().__init__("f_2arg_simple", {"target_func" : target_func, **kwargs})

class f_3arg(OpenSCADObject):
    def __init__(self, target_func=None, **kwargs):
       super().__init__("f_3arg", {"target_func" : target_func, **kwargs})

class ival(OpenSCADObject):
    def __init__(self, target_func=None, **kwargs):
       super().__init__("ival", {"target_func" : target_func, **kwargs})

class xval(OpenSCADObject):
    def __init__(self, target_func=None, **kwargs):
       super().__init__("xval", {"target_func" : target_func, **kwargs})

class f_cmp(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_cmp", {"a" : a, "b" : b, **kwargs})

class f_gt(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_gt", {"a" : a, "b" : b, **kwargs})

class f_lt(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_lt", {"a" : a, "b" : b, **kwargs})

class f_gte(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_gte", {"a" : a, "b" : b, **kwargs})

class f_lte(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_lte", {"a" : a, "b" : b, **kwargs})

class f_eq(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_eq", {"a" : a, "b" : b, **kwargs})

class f_neq(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_neq", {"a" : a, "b" : b, **kwargs})

class f_approx(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_approx", {"a" : a, "b" : b, **kwargs})

class f_napprox(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_napprox", {"a" : a, "b" : b, **kwargs})

class f_or(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_or", {"a" : a, "b" : b, **kwargs})

class f_and(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_and", {"a" : a, "b" : b, **kwargs})

class f_nor(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_nor", {"a" : a, "b" : b, **kwargs})

class f_nand(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_nand", {"a" : a, "b" : b, **kwargs})

class f_xor(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_xor", {"a" : a, "b" : b, **kwargs})

class f_not(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_not", {"a" : a, **kwargs})

class f_even(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_even", {"a" : a, **kwargs})

class f_odd(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_odd", {"a" : a, **kwargs})

class f_add(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_add", {"a" : a, "b" : b, **kwargs})

class f_sub(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_sub", {"a" : a, "b" : b, **kwargs})

class f_mul(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_mul", {"a" : a, "b" : b, **kwargs})

class f_div(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_div", {"a" : a, "b" : b, **kwargs})

class f_mod(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_mod", {"a" : a, "b" : b, **kwargs})

class f_pow(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_pow", {"a" : a, "b" : b, **kwargs})

class f_neg(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_neg", {"a" : a, **kwargs})

class f_min(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_min", {"a" : a, **kwargs})

class f_max(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_max", {"a" : a, **kwargs})

class f_min2(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_min2", {"a" : a, "b" : b, **kwargs})

class f_max2(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_max2", {"a" : a, "b" : b, **kwargs})

class f_min3(OpenSCADObject):
    def __init__(self, a=None, b=None, c=None, **kwargs):
       super().__init__("f_min3", {"a" : a, "b" : b, "c" : c, **kwargs})

class f_max3(OpenSCADObject):
    def __init__(self, a=None, b=None, c=None, **kwargs):
       super().__init__("f_max3", {"a" : a, "b" : b, "c" : c, **kwargs})

class f_sin(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_sin", {"a" : a, **kwargs})

class f_cos(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_cos", {"a" : a, **kwargs})

class f_tan(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_tan", {"a" : a, **kwargs})

class f_asin(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_asin", {"a" : a, **kwargs})

class f_acos(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_acos", {"a" : a, **kwargs})

class f_atan(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_atan", {"a" : a, **kwargs})

class f_atan2(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_atan2", {"a" : a, "b" : b, **kwargs})

class f_len(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_len", {"a" : a, **kwargs})

class f_chr(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_chr", {"a" : a, **kwargs})

class f_ord(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_ord", {"a" : a, **kwargs})

class f_str(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_str", {"a" : a, **kwargs})

class f_str2(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_str2", {"a" : a, "b" : b, **kwargs})

class f_str3(OpenSCADObject):
    def __init__(self, a=None, b=None, c=None, **kwargs):
       super().__init__("f_str3", {"a" : a, "b" : b, "c" : c, **kwargs})

class f_floor(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_floor", {"a" : a, **kwargs})

class f_round(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_round", {"a" : a, **kwargs})

class f_ceil(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_ceil", {"a" : a, **kwargs})

class f_abs(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_abs", {"a" : a, **kwargs})

class f_sign(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_sign", {"a" : a, **kwargs})

class f_ln(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_ln", {"a" : a, **kwargs})

class f_log(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_log", {"a" : a, **kwargs})

class f_exp(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_exp", {"a" : a, **kwargs})

class f_sqr(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_sqr", {"a" : a, **kwargs})

class f_sqrt(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_sqrt", {"a" : a, **kwargs})

class f_norm(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_norm", {"a" : a, **kwargs})

class f_cross(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_cross", {"a" : a, "b" : b, **kwargs})

class f_is_def(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_def", {"x" : x, **kwargs})

class f_is_undef(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_undef", {"x" : x, **kwargs})

class f_is_bool(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_bool", {"x" : x, **kwargs})

class f_is_num(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_num", {"x" : x, **kwargs})

class f_is_int(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_int", {"x" : x, **kwargs})

class f_is_nan(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_nan", {"x" : x, **kwargs})

class f_is_finite(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_finite", {"x" : x, **kwargs})

class f_is_string(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_string", {"x" : x, **kwargs})

class f_is_list(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_list", {"x" : x, **kwargs})

class f_is_range(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_range", {"x" : x, **kwargs})

class f_is_function(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("f_is_function", {"x" : x, **kwargs})

class f_is_vector(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_is_vector", {"a" : a, "b" : b, **kwargs})

class f_is_path(OpenSCADObject):
    def __init__(self, a=None, b=None, **kwargs):
       super().__init__("f_is_path", {"a" : a, "b" : b, **kwargs})

class f_is_region(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_is_region", {"a" : a, **kwargs})

class f_is_vnf(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_is_vnf", {"a" : a, **kwargs})

class f_is_patch(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("f_is_patch", {"a" : a, **kwargs})

