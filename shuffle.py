#!/usr/bin/python
# coding=utf-8

import random
import os
import socket
import copy
import time
import sys

from ButtonFrame import *

print 'Randomly shuffling the videos...'

if len(sys.argv) != 2:
	print 'Usage: python shuffle.py <ipaddr>'
	exit()
else:
	host = sys.argv[1]

categories = []
categories.append('/warmup')
#categories.append('/corner')
#categories.append('/freekick/close')
#categories.append('/freekick/far')
#categories.append('/heading')
#categories.append('/pass')
#categories.append('/bicycle')
categories.append('/shoot/goal')
categories.append('/shoot/on_goalpost')
categories.append('/shoot/cleared_kept')
categories.append('/shoot/out')
categories.append('/tackle/foul')
categories.append('/tackle/poke')
categories.append('/tackle/sliding')
#categories.append('/touch')

videosroot = '../new_casestudy_videos'
videosasked = []
numVideosPerCat = 3

videoslist = []
random_videoids = []
for category in categories:
	videoslist.append([])
	vlist = os.listdir(videosroot+category)
	random.seed()
	rvlist = copy.copy(vlist)
	random.shuffle(rvlist)
	videosasked.append(videosroot+category+'/'+rvlist[0])
	
	for video in vlist:
		videoslist[len(videoslist)-1].append(videosroot+category+'/'+video)
		
	random_videoids.append(range(0,len(videoslist[len(videoslist)-1])))
	random.seed()
	random.shuffle(random_videoids[len(random_videoids)-1])
	

videolog = open('%f.videolog' % time.time(),'w')

print 'Waiting for client...'

soc = socket.socket()
#host = '192.168.1.102'
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
videosframe = VideoFrame(root,None,connection,videolog)
buttonsframe = ButtonFrame(root,videoslist,random_videoids,videosframe,videosasked,connection,videolog,numVideosPerCat)

def on_close_window():
	global connection
	global soc
	global root
	global videolog
	
	videolog.close()
	connection.close()
	soc.close()
	root.destroy()
	
	print 'Closed!!!!'

root.protocol('WM_DELETE_WINDOW',on_close_window)
root.mainloop()
