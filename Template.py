# -*- encoding: utf-8 -*-
import easySVG
from Common import *
import os.path as path

class Template(object):
    """A template in memory

    provide setters to change the template's changeables.
    and provide result output to a svg picture.
    """
    
    def __init__(self, templNo):
        """
        Args:
            templNo: currently only 1, 2 available
        """
        if templNo == 1:
            svgdoc = easySVG.open(path.join("templ", "1.svg"))
        elif templNo == 2:
            svgdoc = easySVG.open(path.join("templ", "2.svg"))
        self._svgdoc = svgdoc

    def getTitle(self):
        sd = self._svgdoc
        eTitle = sd.getElementById("title")
        return eTitle.getElementsByTagName("tspan")[0].firstChild.data

    def setTitle(self, tt):
        titleLen = 13
        if len(tt) > titleLen:
            raise LenghtError(titleLen)
        sd = self._svgdoc
        eTitle = sd.getElementById("title")
        eTitle.getElementsByTagName("tspan")[0].firstChild.data = tt

    def getDescription(self):
        sd = self._svgdoc
        eDesc = sd.getElementById("desc")
        tspans = eDesc.getElementsByTagName("tspan")
        a = ""
        for tspan in tspans:
            a += tspan.firstChild.data
        return a

    def setDescription(self, ds):
        descLen = 60
        if len(ds) > descLen:
            raise LenghtError(descLen)
        sd = self._svgdoc
        eDesc = sd.getElementById("desc")
        tspans = eDesc.getElementsByTagName("tspan")
        for i in range(4):
            astr = desc[(i * 15):((i + 1) * 15)]
            tspans[i].firstChild.data = astr

    def getShowboxes(self):
        sd = self._svgdoc
        sbconts = []
        for i in range(1, 6):
            sb = sd.getElementById("showbox" + str(i))
            nodelist = sb.getElementsByTagName("text")
            for node in nodelist:
                a = node.getAttribute("plid")
                if a == "cost":
                    cost = node.getElementsByTagName("tspan")[0].firstChild.data
                elif a == "sale":
                    sale = node.getElementsByTagName("tspan")[0].firstChild.data
                elif a == "name":
                    crumbs = node.getElementsByTagName("tspan")
                    name = ""
                    for crumb in crumbs:
                        name += crumb.firstChild.data
            img = sb.getElementsByTagName("image")
            url = img[0].getAttribute("xlink:href")
            sbconts.append((cost, sale, name, url))
        return sbconts

    def setShowbox(self, n, cost, sale, name, url):
        """
        Args:
            n: number of the showboxes setting
        todo:
            check args' type
        """
        nameLen = 9
        nameL = len(name)
        if nameL > nameLen:
            raise LengthError(nameLen)
        sd = self._svgdoc
        sb = sd.getElementById("showbox" + str(n))
        nodelist = sb.getElementsByTagName("text")
        for node in nodelist:
            a = node.getAttribute("plid")
            if a == "cost":
                node.getElementsByTagName("tspan")[0].firstChild.data = cost
            elif a == "sale":
                node.getElementsByTagName("tspan")[0].firstChild.data = sale
            elif a == "name":
                crumbs = node.getElementsByTagName("tspan")
                for i in range(nameLen):
                    if i < nameL:
                        crumbs[i].firstChild.data = name[i]
                    else:
                        crumbs[i].firstChild.data = ""
        img = sb.getElementsByTagName("image")
        img[0].setAttribute("xlink:href", url)
                
    def getPicbox(self):
        ePicbox = self._svgdoc.getElementById("picbox")
        return ePicbox.getAttribute("xlink:href")

    def setPicbox(self, url):
        ePicbox = self._svgdoc.getElementById("picbox")
        ePicbox.setAttribute("xlink:href", url)

    def output(self):
        easySVG.save(self._svgdoc, path.join("cache", "output.svg"))
        easySVG.toPNG(path.join("cache", "output.svg"))

    def listChangeables(self):
        # title
        print "title: %s" % self.getTitle()
        # description
        print "desc: %s" % self.getDescription()
        # showboxes
        sbconts = self.getShowboxes()
        for i in range(5):
            print "showbox%s: %s" % ((i + 1), sbconts[i])
        # big pic box
        print "picbox: %s" % self.getPicbox();

if __name__ == "__main__":
    t = Template(1)
    t.setTitle(u"你好呀")
    t.setShowbox(1, 100, 66, u"你说的什么", u"http://www.google.fr/images/srpr/logo4w.png")
    t.listChangeables()
    t.output()

