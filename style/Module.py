# -*- coding: utf-8 -*-
# Copyright 2013 picospuch
"""short description"""

from xml.dom import minidom
import __builtin__

class Abc(object):
    i = 123
    def __init__(self):
        BaseClassName.methodname(self, arguments)
        pass

def open(filename = None):
    """open svg file as a document

    Returns:
        a document object on behalf of the svg file.
    """
    for tagname in ("g", "text", "rect", "image"):
        for item in doc.getElementsByTagName(tagname):
            item.setIdAttribute("id")
    return doc

class B:
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B, C, D]:
    try:
        raise c()
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"

