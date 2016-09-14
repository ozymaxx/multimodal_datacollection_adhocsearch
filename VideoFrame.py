#!/usr/bin/python
# coding=utf-8

from Tkinter import *
from vlc import *

class VideoFrame(Frame):
	def __init__(self,root,videoaddr,connection):
		Frame.__init__(self,root,width=1040,height=710)
		self.pack_propagate(0)
		self.pack(side=RIGHT)
		
		self.videoaddr = videoaddr
		self.connection = connection
		
		self.replay = Button(self,text='TEKRAR OYNAT')
		self.replay.bind('<Button-1>',self.replayvideo)
		self.correct = Button(self,text='SOR BAKALIM BU MU?')
		self.correct.bind('<Button-1>',self.askvideo)
		
		addrtext = ''
		if self.videoaddr != None:
			addrtext = self.videoaddr
			
		self.replay.pack()
		
		#self.videoname = Label(self,text=addrtext)
		self.videopanel = Frame(self)
		self.canvas = Canvas(self.videopanel,bg='#000000').pack(fill=BOTH,expand=1)
		self.videopanel.pack(fill=BOTH,expand=1)
		#self.videoname.pack()
		
		self.correct.pack()
		
		self.instance = Instance()
		self.player = self.instance.media_player_new()
		
	def replayvideo(self,event):
		if self.videoaddr != None:
			self.media = self.instance.media_new(self.videoaddr)
			self.player.set_media(self.media)
			self.player.set_xwindow(self.videopanel.winfo_id())
			self.player.play()
			print 'replayed ',self.videoaddr
		else:
			print 'no videos displayed'
			
	def askvideo(self,event):
		if self.videoaddr != None:
			print 'Is ',self.videoaddr,' the correct video?'
			self.connection.send('GUESS %s' % self.videoaddr)
		else:
			print 'no videos displayed'
		
	def setvideo(self,videoaddr):
		self.videoaddr = videoaddr
		self.replayvideo(None)
