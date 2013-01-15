# -*- coding: utf-8 -*-
# Copyright 2013 picospuch
"""main"""

import easySVG as es
import sys
from xml.dom import minidom

def usage():
    print sys.argv
    print sys.argv[0] + " title desc bigpic pic1 pic2 pic3 pic4 pic5"
    print "nb: title must be less than 13 chars and desc must be less than 60 chars."

def main():
    argc = len(sys.argv)
    if argc < 5 or \
            len(sys.argv[1].decode("utf-8")) > 13 or \
            len(sys.argv[2].decode("utf-8")) > 60:
        usage()
        sys.exit(1)
    
    title = sys.argv[1].decode("utf-8")
    desc = sys.argv[2].decode("utf-8")
    bigpic = sys.argv[3]
    pic = sys.argv[4:]
    while len(pic) < 5:
        pic.append(pic[-1])

    svgdoc = es.open("templ.svg")
    #split and fill desc
    eDesc = svgdoc.getElementById("desc") 
    egDesc = eDesc.getElementsByTagName("tspan")
    for i in range(4):
        astr = desc[(i * 15):((i + 1) * 15)]
        egDesc[i].firstChild.nodeValue = astr
    
    #fill title
    eTitle = svgdoc.getElementById("title")
    eTitle.getElementsByTagName("tspan")[0].firstChild.nodeValue = title
    
    #fill picbox
    ePicbox = svgdoc.getElementById("picbox")
    ePicbox.setAttribute("xlink:href", bigpic)

    #fill showbox
    for i in range(5):
        showbox = svgdoc.getElementById("showbox" + str(i + 1))
        img = showbox.getElementsByTagName("image")
        img[0].setAttribute("xlink:href", pic[i])

    es.save(svgdoc, "output.svg")
    es.toPNG("output.svg")
    
if __name__ == "__main__":
    main()

