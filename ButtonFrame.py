#!/usr/bin/python
# coding=utf-8

from VideoFrame import *

class ButtonFrame(Frame):
	def __init__(self,root,videoslist,videoids,vidframe):
		Frame.__init__(self,root,width=260,height=710)
		self.pack_propagate(0)
		self.pack(side=LEFT)
		
		ids = 0
		self.buttonslist = []
		self.videoslist = videoslist
		self.videoids = videoids
		self.vidframe = vidframe
		
		for vid in videoids:
			buttonn = Button(self,text=str(ids+1),bg='#5ed658',width=5,height=2)
			buttonn.bind('<Button-1>',self.watchvideo)
			buttonn.grid(row=ids/3,column=ids%3)
			#buttonn.pack(side=TOP)
			self.buttonslist.append(buttonn)
			ids = ids + 1
			
	def watchvideo(self,event):
		ids = 0
		while self.buttonslist[ids] != event.widget:
			ids = ids + 1
			
		self.vidframe.setvideo(self.videoslist[self.videoids[ids]])
		event.widget.configure(bg='#ffa496')
