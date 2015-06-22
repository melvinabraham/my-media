
"""MEDIA MANAGEMENT"""

import os

p=raw_input("Input the directory: ")
os.chdir(p)
os.chdir("..")


"""FOR MOVING FILES IN COMMON MEDIA FOLDER TO A SEPARATE SONGS FOLDER"""

os.mkdir("Songs")


for f in os.listdir(p):
	os.chdir(p)
	if f.endswith(".mp3"):
		print "Moving "+f
		with open("songnames.txt","a+") as text_file:
			text_file.write(f)
		os.chdir("..")
		os.system('mv %s %s' % (p+"/"+f,os.getcwd()+"/Songs/"+f))
