from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*2) / 'scad/BOSL/tests/test_math.scad'}", use_not_include=True)

eps = OpenSCADConstant('eps')
class test_quant(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_quant", {**kwargs})

class test_quantdn(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_quantdn", {**kwargs})

class test_quantup(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_quantup", {**kwargs})

class test_constrain(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_constrain", {**kwargs})

class test_posmod(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_posmod", {**kwargs})

class test_modrange(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_modrange", {**kwargs})

class test_segs(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_segs", {**kwargs})

class test_lerp(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_lerp", {**kwargs})

class test_hypot(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_hypot", {**kwargs})

class test_sinh(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_sinh", {**kwargs})

class test_cosh(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_cosh", {**kwargs})

class test_tanh(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_tanh", {**kwargs})

class test_asinh(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_asinh", {**kwargs})

class test_acosh(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_acosh", {**kwargs})

class test_atanh(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_atanh", {**kwargs})

class test_sum(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_sum", {**kwargs})

class test_sum_of_squares(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_sum_of_squares", {**kwargs})

class test_sum_of_sines(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_sum_of_sines", {**kwargs})

class test_mean(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_mean", {**kwargs})

class test_compare_vals(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_compare_vals", {**kwargs})

class test_compare_lists(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_compare_lists", {**kwargs})

class test_any(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_any", {**kwargs})

class test_all(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_all", {**kwargs})

class test_count_true(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_count_true", {**kwargs})

class test_cdr(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_cdr", {**kwargs})

class test_replist(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_replist", {**kwargs})

class test_in_list(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_in_list", {**kwargs})

class test_slice(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_slice", {**kwargs})

class test_select(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_select", {**kwargs})

class test_reverse(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_reverse", {**kwargs})

class test_array_subindex(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_subindex", {**kwargs})

class test_list_range(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_list_range", {**kwargs})

class test_array_shortest(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_shortest", {**kwargs})

class test_array_longest(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_longest", {**kwargs})

class test_array_pad(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_pad", {**kwargs})

class test_array_trim(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_trim", {**kwargs})

class test_array_fit(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_fit", {**kwargs})

class test_enumerate(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_enumerate", {**kwargs})

class test_array_zip(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_zip", {**kwargs})

class test_array_group(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_group", {**kwargs})

class test_flatten(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_flatten", {**kwargs})

class test_sort(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_sort", {**kwargs})

class test_sortidx(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_sortidx", {**kwargs})

class test_unique(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_unique", {**kwargs})

class test_array_dim(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_array_dim", {**kwargs})

class test_vmul(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_vmul", {**kwargs})

class test_vdiv(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_vdiv", {**kwargs})

class test_vabs(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_vabs", {**kwargs})

class test_normalize(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_normalize", {**kwargs})

class test_vector_angle(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_vector_angle", {**kwargs})

class test_vector_axis(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_vector_axis", {**kwargs})

class test_point2d(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_point2d", {**kwargs})

class test_path2d(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_path2d", {**kwargs})

class test_point3d(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_point3d", {**kwargs})

class test_path3d(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_path3d", {**kwargs})

class test_translate_points(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_translate_points", {**kwargs})

class test_scale_points(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_scale_points", {**kwargs})

class test_rotate_points2d(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_rotate_points2d", {**kwargs})

class test_rotate_points3d(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_rotate_points3d", {**kwargs})

class test_simplify_path(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_simplify_path", {**kwargs})

class test_simplify_path_indexed(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("test_simplify_path_indexed", {**kwargs})

