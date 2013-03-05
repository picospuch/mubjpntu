# -*- coding: utf-8 -*-
# Copyright 2013 picospuch
"""The Web Service View for mubjpntu"""

from Template import Template
from os import path
from soaplib.service import DefinitionBase
from soaplib.service import rpc
from soaplib.serializers.primitive import String, Integer
from soaplib.serializers.clazz import Array, ClassSerializer
from soaplib.wsgi import Application

class Showbox(ClassSerializer):
    __namespace__ = "tns"
    cost = String
    sale = String
    name = String
    url = String

class Pintu(ClassSerializer):
    __namespace__ = "tns"
    title = String
    description = String
    bigpic = String
    templNo = Integer
    showbox1 = Showbox
    showbox2 = Showbox
    showbox3 = Showbox
    showbox4 = Showbox
    showbox5 = Showbox

class PintuService(DefinitionBase):
    @rpc(Pintu, _returns=String)
    def getPintuUrl(self, pintu):
        t = Template(pintu.templNo)
        t.setTitle(pintu.title)
        t.setDescription(pintu.description)
        for i in range(1, 6):
            t.setShowbox(i, eval("pintu.showbox%d.cost" % i),
                    eval("pintu.showbox%d.sale" % i),
                    eval("pintu.showbox%d.name" % i),
                    eval("pintu.showbox%d.url" % i))
        t.setPicbox(pintu.bigpic)
        t.output()
        return path.join("cache", "output.svg.png")

if __name__=='__main__':
    try:
        from wsgiref.simple_server import make_server
        server = make_server('localhost', 7789, Application([PintuService], 'tns'))
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"

