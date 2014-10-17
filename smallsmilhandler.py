#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class RootLayout():
    def __init__(self):
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""

    def toString(self):
        cadena = "root-layout"
        if self.width != "":
            cadena += "\twidth=" + self.width
        if self.height != "":
            cadena += "\theight=" + self.height
        if self.backgroundcolor != "":
            cadena += "\tbackgroundcolor=" + self.backgroundcolor
        return cadena


class Region():
    def __init__(self):
        self.ide = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""

    def toString(self):
        cadena = "region"
        if self.ide != "":
            cadena += "\tid=" + self.ide
        if self.top != "":
            cadena += "\ttop=" + self.top
        if self.bottom != "":
            cadena += "\tbottom=" + self.bottom
        if self.left != "":
            cadena += "\tleft=" + self.left
        if self.right != "":
            cadena += "\tright=" + self.right
        return cadena


class Img():
    def __init__(self):
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""

    def toString(self):
        cadena = "img"
        if self.src != "":
            cadena += "\tsrc=" + self.src
        if self.region != "":
            cadena += "\tregion=" + self.region
        if self.begin != "":
            cadena += "\tbegin=" + self.begin
        if self.dur != "":
            cadena += "\tdur=" + self.dur
        return cadena


class Audio():
    def __init__(self):
        self.src = ""
        self.begin = ""
        self.dur = ""

    def toString(self):
        cadena = "audio"
        if self.src != "":
            cadena += "\tsrc=" + self.src
        if self.begin != "":
            cadena += "\tbegin=" + self.begin
        if self.dur != "":
            cadena += "\tdur=" + self.dur
        return cadena


class TextStream():
    def __init__(self):
        self.src = ""
        self.region = ""

    def toString(self):
        cadena = "textstream"
        if self.src != "":
            cadena += "\tsrc=" + self.src
        if self.region != "":
            cadena += "\tregion=" + self.region
        return cadena


class SmallSMILHandler(ContentHandler):

    def __init__(self):
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
            rootlayout_aux.width = attrs.get('width', "")
            rootlayout_aux.height = attrs.get('height', "")
            rootlayout_aux.backgroundcolor = attrs.get('background-color', "")
            self.rootlayout = rootlayout_aux
        elif name == 'region':
            region_aux = Region()
            region_aux.ide = attrs.get('id', "")
            region_aux.top = attrs.get('top', "")
            region_aux.bottom = attrs.get('bottom', "")
            region_aux.left = attrs.get('left', "")
            region_aux.right = attrs.get('right', "")
            self.region = region_aux
        elif name == 'img':
            img_aux = Img()
            img_aux.src = attrs.get('src', "")
            img_aux.region = attrs.get('region', "")
            img_aux.begin = attrs.get('begin', "")
            img_aux.dur = attrs.get('dur', "")
            self.img = img_aux
        elif name == 'audio':
            audio_aux = Audio()
            audio_aux.src = attrs.get('src', "")
            audio_aux.begin = attrs.get('begin', "")
            audio_aux.dur = attrs.get('dur', "")
            self.audio = audio_aux
        elif name == 'textstream':
            textstream_aux = TextStream()
            textstream_aux.src = attrs.get('src', "")
            textstream_aux.region = attrs.get('region', "")
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
