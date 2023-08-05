from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/attachments.scad'}", use_not_include=False)

_tags = OpenSCADConstant('_tags')
_tag = OpenSCADConstant('_tag')
_tag_prefix = OpenSCADConstant('_tag_prefix')
_overlap = OpenSCADConstant('_overlap')
_color = OpenSCADConstant('_color')
_save_color = OpenSCADConstant('_save_color')
_attach_to = OpenSCADConstant('_attach_to')
_attach_anchor = OpenSCADConstant('_attach_anchor')
_attach_norot = OpenSCADConstant('_attach_norot')
_parent_anchor = OpenSCADConstant('_parent_anchor')
_parent_spin = OpenSCADConstant('_parent_spin')
_parent_orient = OpenSCADConstant('_parent_orient')
_parent_size = OpenSCADConstant('_parent_size')
_parent_geom = OpenSCADConstant('_parent_geom')
_tags_shown = OpenSCADConstant('_tags_shown')
_tags_hidden = OpenSCADConstant('_tags_hidden')
_ANCHOR_TYPES = OpenSCADConstant('_ANCHOR_TYPES')
EDGES_NONE = OpenSCADConstant('EDGES_NONE')
EDGES_ALL = OpenSCADConstant('EDGES_ALL')
EDGE_OFFSETS = OpenSCADConstant('EDGE_OFFSETS')
CORNERS_NONE = OpenSCADConstant('CORNERS_NONE')
CORNERS_ALL = OpenSCADConstant('CORNERS_ALL')
CORNER_OFFSETS = OpenSCADConstant('CORNER_OFFSETS')
class position(OpenSCADObject):
    def __init__(self, _from=None, **kwargs):
       super().__init__("position", {"_from" : _from, **kwargs})

class orient(OpenSCADObject):
    def __init__(self, dir=None, anchor=None, spin=None, **kwargs):
       super().__init__("orient", {"dir" : dir, "anchor" : anchor, "spin" : spin, **kwargs})

class attach(OpenSCADObject):
    def __init__(self, _from=None, to=None, overlap=None, norot=None, **kwargs):
       super().__init__("attach", {"_from" : _from, "to" : to, "overlap" : overlap, "norot" : norot, **kwargs})

class tag(OpenSCADObject):
    def __init__(self, tag=None, **kwargs):
       super().__init__("tag", {"tag" : tag, **kwargs})

class force_tag(OpenSCADObject):
    def __init__(self, tag=None, **kwargs):
       super().__init__("force_tag", {"tag" : tag, **kwargs})

class tag_scope(OpenSCADObject):
    def __init__(self, scope=None, **kwargs):
       super().__init__("tag_scope", {"scope" : scope, **kwargs})

class diff(OpenSCADObject):
    def __init__(self, remove=None, keep=None, **kwargs):
       super().__init__("diff", {"remove" : remove, "keep" : keep, **kwargs})

class tag_diff(OpenSCADObject):
    def __init__(self, tag=None, remove=None, keep=None, **kwargs):
       super().__init__("tag_diff", {"tag" : tag, "remove" : remove, "keep" : keep, **kwargs})

class intersect(OpenSCADObject):
    def __init__(self, intersect=None, keep=None, **kwargs):
       super().__init__("intersect", {"intersect" : intersect, "keep" : keep, **kwargs})

class tag_intersect(OpenSCADObject):
    def __init__(self, tag=None, intersect=None, keep=None, **kwargs):
       super().__init__("tag_intersect", {"tag" : tag, "intersect" : intersect, "keep" : keep, **kwargs})

class conv_hull(OpenSCADObject):
    def __init__(self, keep=None, **kwargs):
       super().__init__("conv_hull", {"keep" : keep, **kwargs})

class tag_conv_hull(OpenSCADObject):
    def __init__(self, tag=None, keep=None, **kwargs):
       super().__init__("tag_conv_hull", {"tag" : tag, "keep" : keep, **kwargs})

class hide(OpenSCADObject):
    def __init__(self, tags=None, **kwargs):
       super().__init__("hide", {"tags" : tags, **kwargs})

class show_only(OpenSCADObject):
    def __init__(self, tags=None, **kwargs):
       super().__init__("show_only", {"tags" : tags, **kwargs})

class show_all(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("show_all", {**kwargs})

class show_int(OpenSCADObject):
    def __init__(self, tags=None, **kwargs):
       super().__init__("show_int", {"tags" : tags, **kwargs})

class edge_mask(OpenSCADObject):
    def __init__(self, edges=None, _except=None, **kwargs):
       super().__init__("edge_mask", {"edges" : edges, "_except" : _except, **kwargs})

class corner_mask(OpenSCADObject):
    def __init__(self, corners=None, _except=None, **kwargs):
       super().__init__("corner_mask", {"corners" : corners, "_except" : _except, **kwargs})

class face_profile(OpenSCADObject):
    def __init__(self, faces=None, r=None, d=None, convexity=None, **kwargs):
       super().__init__("face_profile", {"faces" : faces, "r" : r, "d" : d, "convexity" : convexity, **kwargs})

class edge_profile(OpenSCADObject):
    def __init__(self, edges=None, _except=None, convexity=None, **kwargs):
       super().__init__("edge_profile", {"edges" : edges, "_except" : _except, "convexity" : convexity, **kwargs})

class corner_profile(OpenSCADObject):
    def __init__(self, corners=None, _except=None, r=None, d=None, convexity=None, **kwargs):
       super().__init__("corner_profile", {"corners" : corners, "_except" : _except, "r" : r, "d" : d, "convexity" : convexity, **kwargs})

class attachable(OpenSCADObject):
    def __init__(self, anchor=None, spin=None, orient=None, size=None, size2=None, shift=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, h=None, vnf=None, path=None, region=None, extent=None, cp=None, offset=None, anchors=None, two_d=None, axis=None, geom=None, **kwargs):
       super().__init__("attachable", {"anchor" : anchor, "spin" : spin, "orient" : orient, "size" : size, "size2" : size2, "shift" : shift, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "h" : h, "vnf" : vnf, "path" : path, "region" : region, "extent" : extent, "cp" : cp, "offset" : offset, "anchors" : anchors, "two_d" : two_d, "axis" : axis, "geom" : geom, **kwargs})

class show_anchors(OpenSCADObject):
    def __init__(self, s=None, std=None, custom=None, **kwargs):
       super().__init__("show_anchors", {"s" : s, "std" : std, "custom" : custom, **kwargs})

class anchor_arrow(OpenSCADObject):
    def __init__(self, s=None, color=None, flag=None, _tag=None, **kwargs):
       super().__init__("anchor_arrow", {"s" : s, "color" : color, "flag" : flag, "_tag" : _tag, **kwargs})

class anchor_arrow2d(OpenSCADObject):
    def __init__(self, s=None, color=None, _tag=None, **kwargs):
       super().__init__("anchor_arrow2d", {"s" : s, "color" : color, "_tag" : _tag, **kwargs})

class expose_anchors(OpenSCADObject):
    def __init__(self, opacity=None, **kwargs):
       super().__init__("expose_anchors", {"opacity" : opacity, **kwargs})

class frame_ref(OpenSCADObject):
    def __init__(self, s=None, opacity=None, **kwargs):
       super().__init__("frame_ref", {"s" : s, "opacity" : opacity, **kwargs})

class _edges_text3d(OpenSCADObject):
    def __init__(self, txt=None, size=None, **kwargs):
       super().__init__("_edges_text3d", {"txt" : txt, "size" : size, **kwargs})

class _show_edges(OpenSCADObject):
    def __init__(self, edges=None, size=None, text=None, txtsize=None, toplabel=None, **kwargs):
       super().__init__("_show_edges", {"edges" : edges, "size" : size, "text" : text, "txtsize" : txtsize, "toplabel" : toplabel, **kwargs})

class _show_corners(OpenSCADObject):
    def __init__(self, corners=None, size=None, text=None, txtsize=None, toplabel=None, **kwargs):
       super().__init__("_show_corners", {"corners" : corners, "size" : size, "text" : text, "txtsize" : txtsize, "toplabel" : toplabel, **kwargs})

class _show_cube_faces(OpenSCADObject):
    def __init__(self, faces=None, size=None, toplabel=None, botlabel=None, **kwargs):
       super().__init__("_show_cube_faces", {"faces" : faces, "size" : size, "toplabel" : toplabel, "botlabel" : botlabel, **kwargs})

class reorient(OpenSCADObject):
    def __init__(self, anchor=None, spin=None, orient=None, size=None, size2=None, shift=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, h=None, vnf=None, path=None, region=None, extent=None, offset=None, cp=None, anchors=None, two_d=None, axis=None, geom=None, p=None, **kwargs):
       super().__init__("reorient", {"anchor" : anchor, "spin" : spin, "orient" : orient, "size" : size, "size2" : size2, "shift" : shift, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "h" : h, "vnf" : vnf, "path" : path, "region" : region, "extent" : extent, "offset" : offset, "cp" : cp, "anchors" : anchors, "two_d" : two_d, "axis" : axis, "geom" : geom, "p" : p, **kwargs})

class named_anchor(OpenSCADObject):
    def __init__(self, name=None, pos=None, orient=None, spin=None, **kwargs):
       super().__init__("named_anchor", {"name" : name, "pos" : pos, "orient" : orient, "spin" : spin, **kwargs})

class attach_geom(OpenSCADObject):
    def __init__(self, size=None, size2=None, shift=None, scale=None, twist=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, h=None, vnf=None, region=None, extent=None, cp=None, offset=None, anchors=None, two_d=None, axis=None, **kwargs):
       super().__init__("attach_geom", {"size" : size, "size2" : size2, "shift" : shift, "scale" : scale, "twist" : twist, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "h" : h, "vnf" : vnf, "region" : region, "extent" : extent, "cp" : cp, "offset" : offset, "anchors" : anchors, "two_d" : two_d, "axis" : axis, **kwargs})

class _attach_geom_2d(OpenSCADObject):
    def __init__(self, geom=None, **kwargs):
       super().__init__("_attach_geom_2d", {"geom" : geom, **kwargs})

class _attach_geom_size(OpenSCADObject):
    def __init__(self, geom=None, **kwargs):
       super().__init__("_attach_geom_size", {"geom" : geom, **kwargs})

class _attach_transform(OpenSCADObject):
    def __init__(self, anchor=None, spin=None, orient=None, geom=None, p=None, **kwargs):
       super().__init__("_attach_transform", {"anchor" : anchor, "spin" : spin, "orient" : orient, "geom" : geom, "p" : p, **kwargs})

class _get_cp(OpenSCADObject):
    def __init__(self, geom=None, **kwargs):
       super().__init__("_get_cp", {"geom" : geom, **kwargs})

class _force_anchor_2d(OpenSCADObject):
    def __init__(self, anchor=None, **kwargs):
       super().__init__("_force_anchor_2d", {"anchor" : anchor, **kwargs})

class _find_anchor(OpenSCADObject):
    def __init__(self, anchor=None, geom=None, **kwargs):
       super().__init__("_find_anchor", {"anchor" : anchor, "geom" : geom, **kwargs})

class _is_shown(OpenSCADObject):
    def __init__(self, **kwargs):
       super().__init__("_is_shown", {**kwargs})

class _standard_anchors(OpenSCADObject):
    def __init__(self, two_d=None, **kwargs):
       super().__init__("_standard_anchors", {"two_d" : two_d, **kwargs})

class _edges_vec_txt(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("_edges_vec_txt", {"x" : x, **kwargs})

class _edges_text(OpenSCADObject):
    def __init__(self, edges=None, **kwargs):
       super().__init__("_edges_text", {"edges" : edges, **kwargs})

class _is_edge_array(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("_is_edge_array", {"x" : x, **kwargs})

class _edge_set(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_edge_set", {"v" : v, **kwargs})

class _normalize_edges(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_normalize_edges", {"v" : v, **kwargs})

class _edges(OpenSCADObject):
    def __init__(self, v=None, _except=None, **kwargs):
       super().__init__("_edges", {"v" : v, "_except" : _except, **kwargs})

class _is_corner_array(OpenSCADObject):
    def __init__(self, x=None, **kwargs):
       super().__init__("_is_corner_array", {"x" : x, **kwargs})

class _normalize_corners(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_normalize_corners", {"v" : v, **kwargs})

class _corner_set(OpenSCADObject):
    def __init__(self, v=None, **kwargs):
       super().__init__("_corner_set", {"v" : v, **kwargs})

class _corners(OpenSCADObject):
    def __init__(self, v=None, _except=None, **kwargs):
       super().__init__("_corners", {"v" : v, "_except" : _except, **kwargs})

class _corner_edges(OpenSCADObject):
    def __init__(self, edges=None, v=None, **kwargs):
       super().__init__("_corner_edges", {"edges" : edges, "v" : v, **kwargs})

class _corner_edge_count(OpenSCADObject):
    def __init__(self, edges=None, v=None, **kwargs):
       super().__init__("_corner_edge_count", {"edges" : edges, "v" : v, **kwargs})

class _corners_text(OpenSCADObject):
    def __init__(self, corners=None, **kwargs):
       super().__init__("_corners_text", {"corners" : corners, **kwargs})

