#!/usr/bin/python
# coding=utf-8

from ComparisonPanel import *
import socket

IP = '192.168.2.31'
PORT = 3440

print 'Connecting to the station...'

soc = socket.socket()
soc.connect((IP,PORT))

print 'Connected! Preparing the UI...'

root = Tk()
root.resizable(width=False,height=False)
root.title('Video Deneyi')
cpanel = ComparisonPanel(root,None,None,soc)

root.mainloop()
