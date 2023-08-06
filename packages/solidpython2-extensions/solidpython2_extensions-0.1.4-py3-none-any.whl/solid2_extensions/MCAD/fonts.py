from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/MCAD/fonts.scad'}", use_not_include=False)

class outline_2d(OpenSCADObject):
    def __init__(self, outline=None, points=None, paths=None, width=None, resolution=None, **kwargs):
       super().__init__("outline_2d", {"outline" : outline, "points" : points, "paths" : paths, "width" : width, "resolution" : resolution, **kwargs})

class bold_2d(OpenSCADObject):
    def __init__(self, bold=None, width=None, resolution=None, **kwargs):
       super().__init__("bold_2d", {"bold" : bold, "width" : width, "resolution" : resolution, **kwargs})

class polytext(OpenSCADObject):
    def __init__(self, charstring=None, size=None, font=None, line=None, justify=None, align=None, bold=None, bold_width=None, bold_resolution=None, underline=None, underline_start=None, underline_width=None, outline=None, outline_width=None, outline_resolution=None, strike=None, strike_start=None, strike_width=None, **kwargs):
       super().__init__("polytext", {"charstring" : charstring, "size" : size, "font" : font, "line" : line, "justify" : justify, "align" : align, "bold" : bold, "bold_width" : bold_width, "bold_resolution" : bold_resolution, "underline" : underline, "underline_start" : underline_start, "underline_width" : underline_width, "outline" : outline, "outline_width" : outline_width, "outline_resolution" : outline_resolution, "strike" : strike, "strike_start" : strike_start, "strike_width" : strike_width, **kwargs})

class braille_ascii_spec800(OpenSCADObject):
    def __init__(self, inString=None, dot_backing=None, cell_backing=None, justify=None, align=None, dot_h=None, dot_d=None, dot_spacing=None, cell_d2d_spacing=None, line_d2d_spacing=None, echo_translate=None, **kwargs):
       super().__init__("braille_ascii_spec800", {"inString" : inString, "dot_backing" : dot_backing, "cell_backing" : cell_backing, "justify" : justify, "align" : align, "dot_h" : dot_h, "dot_d" : dot_d, "dot_spacing" : dot_spacing, "cell_d2d_spacing" : cell_d2d_spacing, "line_d2d_spacing" : line_d2d_spacing, "echo_translate" : echo_translate, **kwargs})

class _8bit_polyfont(OpenSCADObject):
    def __init__(self, dx=None, dy=None, **kwargs):
       super().__init__("_8bit_polyfont", {"dx" : dx, "dy" : dy, **kwargs})

class braille_ascii_font(OpenSCADObject):
    def __init__(self, dot_h=None, dot_d=None, dot_spacing=None, cell_d2d_spacing=None, line_d2d_spacing=None, **kwargs):
       super().__init__("braille_ascii_font", {"dot_h" : dot_h, "dot_d" : dot_d, "dot_spacing" : dot_spacing, "cell_d2d_spacing" : cell_d2d_spacing, "line_d2d_spacing" : line_d2d_spacing, **kwargs})

