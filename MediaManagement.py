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
	print "\n 		4. PLAY A SONG"
	print "\n 		5. STOP MUSIC PLAYBACK"
	ch=input("\n\t\t")
	if ch==1:
		mediamanagement()

	if ch==2:
		search()

	if ch==3:
		lyrics()

	if ch==4:
		playmusic()

	if ch==5:
		killmusic()

	else:

		print "Enter a valid option"
		time.sleep(1)
		main_menu()


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
	print "\n 		3. Go back to Main Menu"
	ch=input("\t\t")
	
	if ch==1:
		sort_media()
	if ch==2:
		mix_audio() 

	if ch==3:
		main_menu()

	else:

		print "\n\nEnter a valid option"
		time.sleep(1)
		mediamanagement()








def sort_media():

	try:
		p=raw_input("\tInput the directory: ")
		os.chdir(p)
		os.chdir("..")
		path=os.getcwd()

	except OSError:

		print "\n\t\t Check the path entered."
		time.sleep(1)
		main_menu()


	if not os.path.exists("Songs"):
		os.mkdir("Songs")
	if not os.path.exists("Vids"):
		os.mkdir("Vids")
	if not os.path.exists("Pics"):
		os.mkdir("Pics")


	os.chdir(p)
	try:

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

	except:
			
		print "\n\t\tError: Please Check that a valid path was entered."			
		time.sleep(1)

	main_menu()





def mix_audio():
	
	try:	
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


	except:

		print "\n\t\tEntered directory does not exist."
		time.sleep(1)
		mediamanagement()




	try:
		os.system('mv %s %s' % (os.getcwd()+"/"+naud+".mp3",paud+"/"+naud+".mp3"))
	
	except:

		print "\n\tError: Please check the path and name of the audio files: "
		time.sleep(1)

	mediamanagement()



def lyrics():
	
	path=raw_input("\t\tEnter the URL (Please Make Sure It Is From www.lyricsmode.com): ")
	try:
		link=urllib2.urlopen(path)
		soup=BeautifulSoup(link)
		k=soup.p
		k=k.get_text()
		l=k.split('\n')
		l=' '.join(l)
		print l
		
	except: 

		print "\n\t\tPlease check the URL entered"

	

	ch=raw_input("\n\n\n\tPress Y to continue")
	if ch.upper()=='Y':
		main_menu()
	

def killmusic():

	os.system("killall rhythmbox")
	main_menu()


def playmusic():

	i=1
	path=raw_input("\n\t\tEnter the Path Of The Audio Folder")
	try:
		os.chdir(path)

	except OSError:

		print "The entered directory does not exist"
		time.sleep(2)
		main_menu()

	header()
	

	for item in os.listdir(path):
		
		print i,".",item,"\n"
		i=i+1

	ch=raw_input("Please enter the song number you want to play")
	music=os.listdir(path)[int(ch)-1]
	os.system('rhythmbox %s' % (music))

	ch=raw_input("To stop music playback press 'Z' and to go back press 'B'")
	
	if ch.upper()=='B':
		
		main_menu()

	if ch.upper()=='Z':

		killmusic()


main_menu()







		
