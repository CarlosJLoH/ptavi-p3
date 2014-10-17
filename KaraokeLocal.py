#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

class KaraokeLocal():

	def __init__ (self, fichero):
		self.parser = make_parser()
		self.sHandler = SmallSMILHandler()
		self.parser.setContentHandler(self.sHandler)
		self.parser.parse(open(fichero))

	def __str__ (self):
		etiquetas = self.sHandler.get_tags()
		for i in etiquetas:
			print i.toString()
		print "\n"

	def __do_local__ (self):
		etiquetas = self.sHandler.get_tags()
		for i in etiquetas:
			print i.toString()
			if i.toString().find("http")>=0:
				src = i.toString().split("\t")[1]
				path = src.replace("src=", "")
				print "... Downloading " + path.split("/")[-1] + "..."
				os.system("wget -q " + path)

