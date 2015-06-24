import os
import time
import urllib2
from bs4 import BeautifulSoup


cntr=0

"""MAIN MENU"""



def header():

	os.system("clear")
	print "					______  ___              ______  ___    _____________        	";
	print "					___   |/  /____  __      ___   |/  /__________  /__(_)_____ ___ ";
	print "					__  /|_/ /__  / / /________  /|_/ /_  _ \  __  /__  /_  __ \`/	";
	print "					_  /  / / _  /_/ /_/_____/  /  / / /  __/ /_/ / _  / / /_/ / 	";
	print "					/_/  /_/  _\__, /        /_/  /_/  \___/\__,_/  /_/  \__,_/  	";
	print "					          /____/                                             	";
	

def main_menu():

	global cntr
	header()
	time.sleep(2)
	if cntr==0:
		os.system("espeak \"Welcome to My Media\"")
		cntr=1
	else:
		os.system("espeak \"My Media Suite. Please select an option\"")
	print "\n\n		Welcome, My-Media is a Media Suite that has the following functionalities:"
	print "\n 		1. MEDIA MANAGEMENT"
	print "\n		2. SEARCH FOR MEDIA ON THE INTERNET"
	print "\n 		3. LYRICS FOR A SONG"
	ch=input("\n\t\t")
	if ch==1:
		mediamanagement()

	if ch==2:
		search()

	if ch==3:
		lyrics()







"""SEARCH THE INTERNET FOR MEDIA"""


def search():

	header()
	os.system("firefox ")
	main_menu()


def header_med_man():
	header()
	print  "				  __  __          _ _         __  __                                                         _   ";
	print  "				 |  \/  |        | (_)       |  \/  |                                                       | |  ";
	print  "				 | \  / | ___  __| |_  __ _  | \  / | __ _ _ __  _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ ";
	print  "				 | |\/| |/ _ \/ _\` | |/ _\` | | |\/| |/ _\` | '_ \| '_ \ / _\` |/ _\` |/ _ \ '_ \` _ \ / _ \ '_ \| __|";
	print  "				 | |  | |  __/ (_| | | (_| | | |  | | (_| | | | | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ ";
	print  "				 |_|  |_|\___|\__,_|_|\__,_| |_|  |_|\__,_|_| |_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|";
	print  "				                                                              __/ |                              ";
	print  "				                                                             |___/                               ";

	print "\n"







"""MEDIA MANAGEMENT"""







"""FOR MOVING FILES IN COMMON MEDIA FOLDER TO A SEPARATE  FOLDERS"""
def mediamanagement():


	header_med_man()


	print "\n 		1. Sort the media files into separate folders of Audio,Video and Pictures"
	print "\n 		2. Mix two audio files"
	print "\n"
	ch=input("\t\t")
	
	if ch==1:
		sort_media()
	if ch==2:
		mix_audio() 












def sort_media():
	
	p=raw_input("\tInput the directory: ")
	os.chdir(p)
	os.chdir("..")
	path=os.getcwd()

	if not os.path.exists("Songs"):
		os.mkdir("Songs")
	if not os.path.exists("Vids"):
		os.mkdir("Vids")
	if not os.path.exists("Pics"):
		os.mkdir("Pics")


	os.chdir(p)

	for f in os.listdir(p):
		if f.endswith(".mp3"):
			print "Moving "+f
			with open("songnames.txt","a+") as text_file:
				text_file.write(f+"\n")
			os.system('mv %s %s' % (p+"/"+f,path+"/Songs/"+f))

		if f.endswith(".mp4") or f.endswith(".mpeg4") or f.endswith(".avi") or f.endswith(".3gp"):
			print "Moving "+f
			with open("videonames.txt","a+") as text_file:
				text_file.write(f+"\n")
			os.system('mv %s %s' % (p+"/"+f,path+"/Vids/"+f))

		if f.endswith(".jpg") or f.endswith(".jpeg"):
			print "Moving "+f
			with open("photonames.txt","a+") as text_file:
				text_file.write(f+"\n")
			os.system('mv %s %s' % (p+"/"+f,path+"/Pics/"+f))
	time.sleep(2)
	main_menu()




def mix_audio():
	
	header_med_man()
	paud1=raw_input("\tEnter the path for the first audio file: ")
	faud1=open(paud1+".mp3","rb")
	aud1=faud1.read()
	paud2=raw_input("\tEnter the path for the second audio file: ")
	faud2=open(paud2+".mp3","rb")
	aud2=faud2.read()
	naud=raw_input("\tEnter the name of the mixed audio file: ")
	faud=open(naud+".mp3","wb")
	aud=aud1+aud2
	faud.write(aud)
	paud=raw_input("\tEnter the directory to store the mixed audio file: ")
	os.system('mv %s %s' % (os.getcwd()+"/"+naud+".mp3",paud+"/"+naud+".mp3"))
	mediamanagement()



def lyrics():
	path=raw_input("\t\tEnter the URL (Please Make Sure It Is From www.lyricsmode.com): ")
	link=urllib2.urlopen(path)
	soup=BeautifulSoup(link)
	k=soup.p
	k=k.get_text()
	l=k.split('\n')
	l=' '.join(l)
	print l
	ch=raw_input("\n\n\n\tPress Y to continue")
	if ch.upper()=='Y':
		main_menu()













main_menu()







		
