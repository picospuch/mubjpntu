# -*- coding: utf-8 -*-
# Copyright 2013 picospuch
"""short description"""

from xml.dom import minidom
import __builtin__

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

