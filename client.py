#!/usr/bin/python
# coding=utf-8

#from ComparisonPanel import *
from SinglePanel import *
import socket

IP = '192.168.1.105'
PORT = 3440

print 'Connecting to the station...'

soc = socket.socket()
soc.connect((IP,PORT))

print 'Connected! Preparing the UI...'

root = Tk()

scwidth = 1210
scheight = 964

root.resizable(width=False,height=False)
root.title('Futbolda Sesli Sinema')
cpanel = ComparisonPanel(root,None,None,soc,scwidth,scheight)

root.mainloop()
