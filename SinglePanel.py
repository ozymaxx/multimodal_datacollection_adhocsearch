#!/usr/bin/python
# coding=utf-8

import thread

from Tkinter import *
from vlc import *

class ComparisonPanel(Frame):
	def __init__(self,parent,originalvideo,comparedvideo,soc,scwidth,scheight):
		Frame.__init__(self,parent,width=scwidth,height=scheight)
		self.pack_propagate(0)
		self.pack()
		
		self.aboutstartpath = '../new_casestudy_videos/about_start.ogg'
		self.startvideopath = '../new_casestudy_videos/start_end.ogg'
		self.repeatvideopath = '../new_casestudy_videos/repeat.ogg'
		
		self.soc = soc
		
		self.originalvideo = originalvideo
		
		self.originalwatched = 0
		
		self.originalpanel = Frame(self,width=scwidth,height=scheight)
		
		self.originalpanel.pack_propagate(0)
		
		self.originalvideopanel = Frame(self.originalpanel)
		self.originalcanvas = Canvas(self.originalvideopanel,bg='#000000').pack(fill=BOTH,expand=1)
		self.originalvideopanel.pack(fill=BOTH,expand=1)
		
		self.originalpanel.pack()
		
		self.originalinstance = Instance()
		#self.original_player = self.originalinstance.media_list_player_new()
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
		self.original_player.set_xwindow(self.originalvideopanel.winfo_id())
		
		#playlist = [self.aboutstartpath,addr,self.repeatvideopath,addr,self.repeatvideopath,addr,self.startvideopath]
		playlist = [self.aboutstartpath,addr]#,self.repeatvideopath,addr,self.repeatvideopath,addr,self.startvideopath]
		#playing = set([1,2,3,4])
		for played in playlist:
			#print 'playing %s' % played
			self.originalmedia = self.originalinstance.media_new(played)
			self.original_player.set_media(self.originalmedia)
			self.original_player.play()
			
			while True:
				state = self.original_player.get_state()
				if state == 6:
					break
		
		'''
		self.originalmedia = self.originalinstance.media_new(addr)
		self.original_player.set_media(self.originalmedia)
		self.original_player.play()
		'''
		
		'''
		self.originalmedialist = self.originalinstance.media_list_new()
		self.originalmedialist.insert_media(self.originalinstance.media_new(self.startvideopath),0)
		self.originalmedialist.insert_media(self.originalinstance.media_new(addr),1)
		self.originalmedialist.insert_media(self.originalinstance.media_new(self.repeatvideopath),2)
		self.originalmedialist.insert_media(self.originalinstance.media_new(addr),3)
		self.originalmedialist.insert_media(self.originalinstance.media_new(self.repeatvideopath),4)
		self.originalmedialist.insert_media(self.originalinstance.media_new(addr),5)
		self.originalmedialist.insert_media(self.originalinstance.media_new(self.startvideopath),6)
		self.original_player.set_media_list(self.originalmedialist)
		#self.original_player.set_xwindow(self.originalvideopanel.winfo_id())
		self.original_player.play()
		'''
