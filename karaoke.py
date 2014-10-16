#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import sys
import os
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Usage: python karaoke.py file.smil"
	else:
		parser = make_parser()
    	sHandler = SmallSMILHandler()
    	parser.setContentHandler(sHandler)
    	parser.parse(open('karaoke.smil'))
    	etiquetas = sHandler.get_tags()
    	for i in etiquetas:
    		print i.toString()
    		if i.toString().find("http")>=0:
				src = i.toString().split("\t")[1]
				path = src.replace("src=", "")
				print "... Downloading " + path.split("/")[-1] + "..."
				os.system("wget -q " + path)

