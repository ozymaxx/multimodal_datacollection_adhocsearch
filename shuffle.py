#!/usr/bin/python
# coding=utf-8

import random
import os
import socket
import copy

from ButtonFrame import *

print 'Randomly shuffling the videos...'

categories = []
categories.append('/corner')
categories.append('/freekick/close')
categories.append('/freekick/far')
categories.append('/heading')
categories.append('/pass')
categories.append('/shoot/bicycle')
categories.append('/shoot/goal')
categories.append('/shoot/goalpost')
categories.append('/shoot/kept')
categories.append('/shoot/out')
categories.append('/tackle/foul')
categories.append('/tackle/poke')
categories.append('/tackle/sliding')
categories.append('/touch')

videosroot = '../new_casestudy_videos'
videosasked = []

videoslist = []
for category in categories:
	vlist = os.listdir(videosroot+category)
	random.seed()
	rvlist = copy.copy(vlist)
	random.shuffle(rvlist)
	videosasked.append(videosroot+category+'/'+rvlist[0])
	
	for video in vlist:
		videoslist.append(videosroot+category+'/'+video)
		

videoids = range(0,len(videoslist))
random.seed()
random.shuffle(videoids)

print 'Waiting for client...'

soc = socket.socket()
host = '192.168.2.31'
portnum = 3440
soc.bind((host,portnum))
soc.listen(5)
connection,address = soc.accept()

print 'Client has connected! Preparing UI...' 

w = 1300
h = 710

root = Tk()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.title('Video Deneyi')
root.resizable(width=False,height=False)
videosframe = VideoFrame(root,None,connection)
buttonsframe = ButtonFrame(root,videoslist,videoids,videosframe,videosasked,connection)
root.mainloop()
