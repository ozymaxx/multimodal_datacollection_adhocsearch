#!/usr/bin/python
# coding=utf-8

from VideoFrame import *

class ButtonFrame(Frame):
	def __init__(self,root,videoslist,videoids,vidframe,videosasked,connection,videolog):
		Frame.__init__(self,root,width=260,height=710)
		self.pack_propagate(0)
		self.pack(side=LEFT)
		
		ids = 0
		self.buttonslist = []
		self.videoslist = videoslist
		self.videoids = videoids
		self.vidframe = vidframe
		self.videosasked = videosasked
		self.askedcount = 0
		self.connection = connection
		self.videolog = videolog
		
		self.asknewbutton = Button(self,text='YENİ VİDEO SOR',width=15,height=2)
		self.asknewbutton.bind('<Button-1>',self.sendNextVideo)
		self.asknewbutton.grid(row=0,column=0,columnspan=3)
		
		for vid in videoids:
			buttonn = Button(self,text=str(ids+1),bg='#5ed658',width=5,height=2)
			buttonn.bind('<Button-1>',self.watchvideo)
			buttonn.grid(row=ids/3+1,column=ids%3)
			#buttonn.pack(side=TOP)
			self.buttonslist.append(buttonn)
			ids = ids + 1
			
	def watchvideo(self,event):
		ids = 0
		while self.buttonslist[ids] != event.widget:
			ids = ids + 1
			
		self.vidframe.setvideo(self.videoslist[self.videoids[ids]])
		event.widget.configure(bg='#ffa496')
		
	def sendNextVideo(self,event):
		if self.askedcount < len(self.videosasked):
                        os.system('/usr/bin/canberra-gtk-play --id="complete"')
			query = 'CHANGETO %s' % self.videosasked[self.askedcount]
			self.videolog.write('%s\n' % query)
			self.connection.send(query)
			self.askedcount = self.askedcount + 1
			map(lambda x: x.configure(bg='#5ed658'),self.buttonslist)
			self.vidframe.setvideo(None)
		else:
			tkMessageBox.showwarning('Videolar Tamamlandı','Çalışmada sorulması gereken tüm videoları sordunuz!')
