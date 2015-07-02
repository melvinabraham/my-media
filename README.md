# My-Media

My-Media is a Simple **Media Suite** written in **Python**.
Currently it works only in *Linux Distributions* including **Ubuntu**,**Fedora** etc.

##ABOUT


The interface has been redisgned as a Menu Driven Interface with the following functinalities:
	


###1.Media Management:
	 This functionality is used to manage media (Pictures,Videos,Songs). It has the following fuctions:

	1. It **sorts** the files according to their type into respective folders  of the Audio,Video and the Pictures that have been moved.

				
	2. It can be used to mix two Audio files.


###2. Search:

	 This functionality is used to gain more info about the media at hand using the Internet.


###3. Lyrics:

	This uses basic *Web-Scraping* (http://lyricsmode.com) to get the lyrics of the Song.


###4. Play A Song:
	
	THis Functionality uses Rhythmbox To Allow Users to select the song to play from a list.


###5. Stop Music PlayBack:
	
	This functionality can be used to stop Music Playback.


###6. TOP 20 Bollywood Songs:

	This functionality uses *Web-Scraping* (http://www.radiomirchi.com/more/mirchi-top-20/) to get the Top-20 Songs along with their embedded Video Links.

###7. Favourites:

	This functionality helps the user to make a music specicfically for their favourite tracks and play them.



##CONFIGURATION:

*My-Media* uses 3rd-party modules in Python.These are:

*  [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
	
	To install bs4, goto a terminal and type 'sudo apt-get install python-bs4'

*  [espeak](http://espeak.sourceforge.net/)
	
	To install espeak, goto terminal and type 'sudo apt-get install espeak' or download from the above link.

##HOW TO RUN:

To run *My-Media* Suite download the Zip File or Clone Locally From the Repository. Unpack the compressed files, open the terminal in that directory and execute 'python MediaManagement.py' in the terminal.