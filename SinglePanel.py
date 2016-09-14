#!/usr/bin/python
# coding=utf-8

import thread

from Tkinter import *
from vlc import *

class ComparisonPanel(Frame):
	def __init__(self,parent,originalvideo,comparedvideo,soc):
		Frame.__init__(self,parent,width=1300,height=710)
		self.pack_propagate(0)
		self.pack()
		self.soc = soc
		
		self.originalvideo = originalvideo
		
		self.originalwatched = 0
		
		self.originalpanel = Frame(self,width=1300,height=710)
		
		self.originalpanel.pack_propagate(0)
		
		self.originalvideopanel = Frame(self.originalpanel)
		self.originalcanvas = Canvas(self.originalvideopanel,bg='#000000').pack(fill=BOTH,expand=1)
		self.originalvideopanel.pack(fill=BOTH,expand=1)
		
		self.originalpanel.pack()
		
		self.originalinstance = Instance()
		self.original_player = self.originalinstance.media_player_new()
		
		thread.start_new_thread(self.listentostation, ())
		
	def listentostation(self):
		while True:
			data = self.soc.recv(1024)
			if not data:
				break
			
			delims = data.split()
			if delims[0] == 'CHANGETO' or delims[0] == 'GUESS':
				self.updateOriginalVideo(delims[1])
				print 'video changed to %s' % delims[1]
			else:
				print 'Invalid query! <%s>' % data

		self.soc.close()
		
	def updateOriginalVideo(self,addr):
		self.originalmedia = self.originalinstance.media_new(addr)
		self.original_player.set_media(self.originalmedia)
		self.original_player.set_xwindow(self.originalvideopanel.winfo_id())
		self.original_player.play()
