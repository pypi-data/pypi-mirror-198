from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*2) / 'scad/BOSL/tests/test_convex_hull.scad'}", use_not_include=True)

testpoints_on_sphere = OpenSCADConstant('testpoints_on_sphere')
testpoints_circular = OpenSCADConstant('testpoints_circular')
testpoints_coplanar = OpenSCADConstant('testpoints_coplanar')
testpoints_collinear_2d = OpenSCADConstant('testpoints_collinear_2d')
testpoints_collinear_3d = OpenSCADConstant('testpoints_collinear_3d')
testpoints2d = OpenSCADConstant('testpoints2d')
testpoints3d = OpenSCADConstant('testpoints3d')
class visualize_hull(OpenSCADObject):
    def __init__(self, points=None, **kwargs):
       super().__init__("visualize_hull", {"points" : points, **kwargs})

