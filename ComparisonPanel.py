#!/usr/bin/python
# coding=utf-8

from Tkinter import *
from vlc import *

class ComparisonPanel(Frame):
	def __init__(self,parent,originalvideo,comparedvideo,soc):
		Frame.__init__(self,parent,width=1300,height=710)
		self.pack_propagate(0)
		self.pack()
		self.soc = soc
		
		self.originalvideo = originalvideo
		self.comparedvideo = comparedvideo
		
		self.originalwatched = 0
		
		self.originalpanel = Frame(self,width=650,height=710)
		self.comparedpanel = Frame(self,width=650,height=710)
		
		self.originalpanel.pack_propagate(0)
		self.comparedpanel.pack_propagate(0)
		
		Label(self.originalpanel,text='Orijinal Video').pack()
		Label(self.comparedpanel,text='Gönderilen Video').pack()
		
		self.originalvideopanel = Frame(self.originalpanel)
		self.originalcanvas = Canvas(self.originalvideopanel,bg='#000000').pack(fill=BOTH,expand=1)
		self.originalvideopanel.pack(fill=BOTH,expand=1)
		
		self.comparedvideopanel = Frame(self.comparedpanel)
		self.comparedcanvas = Canvas(self.comparedvideopanel,bg='#000000').pack(fill=BOTH,expand=1)
		self.comparedvideopanel.pack(fill=BOTH,expand=1)
		
		self.originalpanel.pack(side=LEFT)
		self.comparedpanel.pack(side=RIGHT)
		
		self.originalinstance = Instance()
		self.original_player = self.originalinstance.media_player_new()
		self.comparedinstance = Instance()
		self.compared_player = self.comparedinstance.media_player_new()
		
		self.after(1,self.listentostation)
		
	def listentostation(self):
		while True:
			data = self.soc.recv(1024)
			if not data:
				break
			
			delims = data.split()
			if delims[0] == 'CHANGETO':
				self.updateOriginalVideo(delims[1])
			elif delims[0] == 'GUESS':
				self.updateGuessedVideo(delims[1])
			else:
				print 'Invalid query! <%s>' % data

		self.soc.close()
		
	def updateOriginalVideo(self,addr):
		self.originalmedia = self.originalinstance.media_new(addr)
		self.original_player.set_media(self.originalmedia)
		self.original_player.set_xwindow(self.originalvideopanel.winfo_id())
		self.original_player.play()
		
	def updateGuessedVideo(self,addr):
		self.comparedmedia = self.comparedinstance.media_new(addr)
		self.compared_player.set_media(self.comparedmedia)
		self.compared_player.set_xwindow(self.comparedvideopanel.winfo_id())
		self.compared_player.play()
