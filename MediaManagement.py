import os
import time


"""MAIN MENU"""


def spaces():
	print "		"


def header():

	os.system("clear")
	print "					______  ___              ______  ___    _____________        	";
	print "					___   |/  /____  __      ___   |/  /__________  /__(_)_____ ___ ";
	print "					__  /|_/ /__  / / /________  /|_/ /_  _ \  __  /__  /_  __ \`/	";
	print "					_  /  / / _  /_/ /_/_____/  /  / / /  __/ /_/ / _  / / /_/ / 	";
	print "					/_/  /_/  _\__, /        /_/  /_/  \___/\__,_/  /_/  \__,_/  	";
	print "					          /____/                                             	";
	

def main_menu():


	header()
	time.sleep(2)
	os.system("espeak Welcome")
	print "\n\n		Welcome, My-Media is a Media Suite that has the following functionalities:"
	print "\n 		1. MEDIA MANAGEMENT"
	print "\n		2. SEARCH FOR MEDIA ON THE INTERNET"

	ch=input()
	if ch==1:
		mediamanagement()

	if ch==2:
		search()









"""SEARCH THE INTERNET FOR MEDIA"""


def search():

	header()
	os.system("firefox ")
	main_menu()










"""MEDIA MANAGEMENT"""







"""FOR MOVING FILES IN COMMON MEDIA FOLDER TO A SEPARATE  FOLDERS"""
def mediamanagement():



	p=raw_input("Input the directory: ")
	os.chdir(p)
	os.chdir("..")
	path=os.getcwd()


	os.mkdir("Songs")
	os.mkdir("Vids")
	os.mkdir("Pics")


	os.chdir(p)

	for f in os.listdir(p):
		if f.endswith(".mp3"):
			print "Moving "+f
			with open("songnames.txt","a+") as text_file:
				text_file.write(f)
			os.system('mv %s %s' % (p+"/"+f,path+"/Songs/"+f))

		if f.endswith(".mp4"):
			print "Moving "+f
			with open("videonames.txt","a+") as text_file:
				text_file.write(f)
			os.system('mv %s %s' % (p+"/"+f,path+"/Vids/"+f))

		if f.endswith(".jpg") or f.endswith(".jpeg"):
			print "Moving "+f
			with open("photonames.txt","a+") as text_file:
				text_file.write(f)
			os.system('mv %s %s' % (p+"/"+f,path+"/Pics/"+f))

	main_menu()

main_menu()







		
