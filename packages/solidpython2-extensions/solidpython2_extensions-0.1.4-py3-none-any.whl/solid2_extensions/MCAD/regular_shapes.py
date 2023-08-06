from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/regular_shapes.scad'}", use_not_include=False)

class triangle(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("triangle", {"radius" : radius, **kwargs})

class reg_polygon(OpenSCADObject):
    def __init__(self, sides=None, radius=None, **kwargs):
       super().__init__("reg_polygon", {"sides" : sides, "radius" : radius, **kwargs})

class regular_polygon(OpenSCADObject):
    def __init__(self, sides=None, radius=None, **kwargs):
       super().__init__("regular_polygon", {"sides" : sides, "radius" : radius, **kwargs})

class pentagon(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("pentagon", {"radius" : radius, **kwargs})

class hexagon(OpenSCADObject):
    def __init__(self, radius=None, diameter=None, across_flats=None, **kwargs):
       super().__init__("hexagon", {"radius" : radius, "diameter" : diameter, "across_flats" : across_flats, **kwargs})

class heptagon(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("heptagon", {"radius" : radius, **kwargs})

class octagon(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("octagon", {"radius" : radius, **kwargs})

class nonagon(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("nonagon", {"radius" : radius, **kwargs})

class decagon(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("decagon", {"radius" : radius, **kwargs})

class hendecagon(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("hendecagon", {"radius" : radius, **kwargs})

class dodecagon(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("dodecagon", {"radius" : radius, **kwargs})

class ring(OpenSCADObject):
    def __init__(self, inside_diameter=None, thickness=None, **kwargs):
       super().__init__("ring", {"inside_diameter" : inside_diameter, "thickness" : thickness, **kwargs})

class ellipse(OpenSCADObject):
    def __init__(self, width=None, height=None, **kwargs):
       super().__init__("ellipse", {"width" : width, "height" : height, **kwargs})

class egg_outline(OpenSCADObject):
    def __init__(self, width=None, length=None, **kwargs):
       super().__init__("egg_outline", {"width" : width, "length" : length, **kwargs})

class cone(OpenSCADObject):
    def __init__(self, height=None, radius=None, center=None, **kwargs):
       super().__init__("cone", {"height" : height, "radius" : radius, "center" : center, **kwargs})

class oval_prism(OpenSCADObject):
    def __init__(self, height=None, rx=None, ry=None, center=None, **kwargs):
       super().__init__("oval_prism", {"height" : height, "rx" : rx, "ry" : ry, "center" : center, **kwargs})

class oval_tube(OpenSCADObject):
    def __init__(self, height=None, rx=None, ry=None, wall=None, center=None, **kwargs):
       super().__init__("oval_tube", {"height" : height, "rx" : rx, "ry" : ry, "wall" : wall, "center" : center, **kwargs})

class cylinder_tube(OpenSCADObject):
    def __init__(self, height=None, radius=None, wall=None, center=None, **kwargs):
       super().__init__("cylinder_tube", {"height" : height, "radius" : radius, "wall" : wall, "center" : center, **kwargs})

class tubify(OpenSCADObject):
    def __init__(self, radius=None, wall=None, **kwargs):
       super().__init__("tubify", {"radius" : radius, "wall" : wall, **kwargs})

class triangle_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, **kwargs):
       super().__init__("triangle_prism", {"height" : height, "radius" : radius, **kwargs})

class triangle_tube(OpenSCADObject):
    def __init__(self, height=None, radius=None, wall=None, **kwargs):
       super().__init__("triangle_tube", {"height" : height, "radius" : radius, "wall" : wall, **kwargs})

class pentagon_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, **kwargs):
       super().__init__("pentagon_prism", {"height" : height, "radius" : radius, **kwargs})

class pentagon_tube(OpenSCADObject):
    def __init__(self, height=None, radius=None, wall=None, **kwargs):
       super().__init__("pentagon_tube", {"height" : height, "radius" : radius, "wall" : wall, **kwargs})

class hexagon_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, across_flats=None, **kwargs):
       super().__init__("hexagon_prism", {"height" : height, "radius" : radius, "across_flats" : across_flats, **kwargs})

class hexagon_tube(OpenSCADObject):
    def __init__(self, height=None, radius=None, wall=None, **kwargs):
       super().__init__("hexagon_tube", {"height" : height, "radius" : radius, "wall" : wall, **kwargs})

class heptagon_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, **kwargs):
       super().__init__("heptagon_prism", {"height" : height, "radius" : radius, **kwargs})

class heptagon_tube(OpenSCADObject):
    def __init__(self, height=None, radius=None, wall=None, **kwargs):
       super().__init__("heptagon_tube", {"height" : height, "radius" : radius, "wall" : wall, **kwargs})

class octagon_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, **kwargs):
       super().__init__("octagon_prism", {"height" : height, "radius" : radius, **kwargs})

class octagon_tube(OpenSCADObject):
    def __init__(self, height=None, radius=None, wall=None, **kwargs):
       super().__init__("octagon_tube", {"height" : height, "radius" : radius, "wall" : wall, **kwargs})

class nonagon_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, **kwargs):
       super().__init__("nonagon_prism", {"height" : height, "radius" : radius, **kwargs})

class decagon_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, **kwargs):
       super().__init__("decagon_prism", {"height" : height, "radius" : radius, **kwargs})

class hendecagon_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, **kwargs):
       super().__init__("hendecagon_prism", {"height" : height, "radius" : radius, **kwargs})

class dodecagon_prism(OpenSCADObject):
    def __init__(self, height=None, radius=None, **kwargs):
       super().__init__("dodecagon_prism", {"height" : height, "radius" : radius, **kwargs})

class torus(OpenSCADObject):
    def __init__(self, outerRadius=None, innerRadius=None, **kwargs):
       super().__init__("torus", {"outerRadius" : outerRadius, "innerRadius" : innerRadius, **kwargs})

class torus2(OpenSCADObject):
    def __init__(self, r1=None, r2=None, **kwargs):
       super().__init__("torus2", {"r1" : r1, "r2" : r2, **kwargs})

class oval_torus(OpenSCADObject):
    def __init__(self, inner_radius=None, thickness=None, **kwargs):
       super().__init__("oval_torus", {"inner_radius" : inner_radius, "thickness" : thickness, **kwargs})

class triangle_pyramid(OpenSCADObject):
    def __init__(self, radius=None, **kwargs):
       super().__init__("triangle_pyramid", {"radius" : radius, **kwargs})

class square_pyramid(OpenSCADObject):
    def __init__(self, base_x=None, base_y=None, height=None, **kwargs):
       super().__init__("square_pyramid", {"base_x" : base_x, "base_y" : base_y, "height" : height, **kwargs})

class egg(OpenSCADObject):
    def __init__(self, width=None, length=None, **kwargs):
       super().__init__("egg", {"width" : width, "length" : length, **kwargs})

