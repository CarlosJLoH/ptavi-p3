#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import sys

from KaraokeLocal import KaraokeLocal

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Usage: python karaoke.py file.smil"
	else:
		kLocal = KaraokeLocal(sys.argv[1])
    	kLocal.__str__()
    	kLocal.__do_local__()
