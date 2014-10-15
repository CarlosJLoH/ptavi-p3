#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class RootLayout():
	def __init__ (self):
		self.width = ""
		self.height = ""
		self.backgroundcolor = ""
	
	def toString (self):
		return "root-layout -> width: " + self.width + ", height: " + self.height + ", backgroundcolor: " + self.backgroundcolor
		
class Region():
	def __init__ (self):
		self.ide = ""
		self.top = ""
		self.bottom = ""
		self.left = ""
		self.right = ""
	
	def toString (self):
		return "region -> ide: " + self.ide + ", top: " + self.top + ", bottom: " + self.bottom + ", left: " + self.left + ", right: " + self.right
		
class Img():
	def __init__ (self):
		self.src = ""
		self.region = ""
		self.begin = ""
		self.dur = ""
	
	def toString (self):
		return "img -> src: " + self.src + ", region: " + self.region + ", begin: " + self.begin + ", dur: " + self.dur

class Audio():
	def __init__ (self):
		self.src = ""
		self.begin = ""
		self.dur = ""

	def toString (self):
		return "audio -> src: " + self.src + ", begin: " + self.begin + ", dur: " + self.dur


class TextStream():
	def __init__ (self):
		self.src = ""
		self.region = ""
	
	def toString (self):
		return "src: " + self.src + ", region: " + self.region
		
class SmallSMILHandler(ContentHandler):

    def __init__ (self):
		self.rootlayout = RootLayout()
		self.region = Region()
		self.img = Img()
		self.audio = Audio()
		self.textstream = TextStream()
		self.etiquetas = []

    def get_tags(self):
		return self.etiquetas
		
    def startElement(self, name, attrs):
        if name == 'root-layout':
        	rootlayout_aux = RootLayout()
         	rootlayout_aux.width = attrs.get('width',"")
     		rootlayout_aux.height = attrs.get('height',"")
       		rootlayout_aux.backgroundcolor = attrs.get('background-color',"")
       		self.rootlayout = rootlayout_aux
        elif name == 'region':
        	region_aux = Region()
        	region_aux.ide = attrs.get('id',"")
       		region_aux.top = attrs.get('top',"")
        	region_aux.bottom = attrs.get('bottom',"")
        	region_aux.left = attrs.get('left',"")
        	region_aux.right = attrs.get('right',"")
        	self.region = region_aux
        elif name == 'img':
        	img_aux = Img()
        	img_aux.src = attrs.get('src',"")
	        img_aux.region = attrs.get('region',"")
           	img_aux.begin = attrs.get('begin',"")
           	img_aux.dur = attrs.get('dur',"")
        	self.img = img_aux
        elif name == 'audio':
        	audio_aux = Audio()
           	audio_aux.src = attrs.get('src',"")
           	audio_aux.begin = attrs.get('begin',"")
           	audio_aux.dur = attrs.get('dur',"")
        	self.audio = audio_aux
        elif name == 'textstream':
        	textstream_aux = TextStream()
           	textstream_aux.src = attrs.get('src',"")
           	textstream_aux.region = attrs.get('region',"")
        	self.textstream = textstream_aux

    def endElement(self, name):
    	if name == 'root-layout':
    		self.etiquetas.append(self.rootlayout)
		
        elif name == 'region':
        	self.etiquetas.append(self.region)

        elif name == 'img':
			self.etiquetas.append(self.img)
           	
        elif name == 'audio':
			self.etiquetas.append(self.audio)
           	
        elif name == 'textstream':
			self.etiquetas.append(self.textstream)

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    etiquetas = sHandler.get_tags()
    for i in etiquetas:
    	print i.toString()
