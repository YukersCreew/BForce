#!/usr/bin/python

import os
import sys
import time

R = '\033[1;31m'
H = '\033[1;32m'

os.system("clear")

def Menu():
	os.system("cd data;python yuker.py")
	print("\n "+R+"["+H+"A"+R+"] "+H+"Facebook ")
	print("\n "+R+"["+H+"B"+R+"] "+H+"HotMail ")
	print("\n "+R+"["+H+"C"+R+"] "+H+"Yahoo ")
	print("\n "+R+"["+H+"D"+R+"] "+H+"Gmail ")
	print("\n "+R+"["+H+"X"+R+"] "+H+"Exit ")
	print("\n "+R+"["+H+"Note"+R+"] "+H+"Tools Brute Force")
	
	
	
	Yukers = input("\n"+R+"["+H+"Yukers"+R+"] > "+R+"")
	
	if Yukers == "X" or Yukers == "x":
		print("Good Bye My Friend's :)")
		time.sleep(2)
		os.system("killall -9 com.termux")
		
	elif Yukers == "A" or Yukers == "a":
		os.system("cd data;python2 YFB.py;cd Yukers")
		
	elif Yukers == "B" or Yukers == "b":
		os.system("clear")
		os.system("cd data;python2 YHTML.py;")
		
	elif Yukers == "C" or Yukers == "c":
		os.system("clear")
		os.system("cd data;python2 YHM.py")
		
	elif  Yukers == "D" or Yukers == "d":
		os.system("clear")
		os.system("cd data;python2 YGM.py")
		
	
Menu()