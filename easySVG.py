# -*- coding: utf-8 -*-
# Copyright 2013 picospuch
"""make some easier for processing SVG with minidom"""

from xml.dom import minidom
import __builtin__
import cairo
import codecs
import rsvg

def open(filename = None):
    """open svg file as a document

    Returns:
        a document object on behalf of the svg file.
    """
    doc = minidom.parse(filename)
    # workaround for making getElementById work.
    for tagname in ("g", "text", "rect", "image"):
        for item in doc.getElementsByTagName(tagname):
            item.setIdAttribute("id")
    return doc

def save(doc, filename):
    """save a DOM doc to a xml file."""
    f = codecs.open(filename, "wb", "utf-8")
    # print f.encoding
    doc.writexml(f)
    f.close()

def toPNG(filename = None):
    """convert SVG file to PNG file."""
    # ref http://cairographics.org/cookbook/librsvgpython/
    hRsvg = rsvg.Handle(filename)
    (w, h, wf, hf) = hRsvg.get_dimension_data()
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(surface)
    hRsvg.render_cairo(ctx)
    hRsvg.close()
    surface.write_to_png(filename + ".png")
    surface.finish()

