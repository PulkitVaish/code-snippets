#Welcome to my python program ver 1.0
#Written by Pulkit Vaish
#This version of program uses pyttsx3 module's speak function to convey messages.
#Pied piper is a fictional company part of my favourite sitcom "Silicon Valley"

#This is the first program i created and has been update over the days.
""" As of version 1.0 it can only perform basic task of launching other programs"""


import webbrowser


import pyttsx3
#Rate of speaking words has been decremented.
voiceEngine = pyttsx3.init()
newVoiceRate=150
voiceEngine.setProperty('rate', newVoiceRate)
voice_id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
voiceEngine.setProperty('voice', voice_id2)

import os
print("_________________________________________________________________________________________________________________")
print("------------------------------->>> Welcome To Pied Piper Assistant Wizard v1.0 <<<-------------------------------",end='')
print("_________________________________________________________________________________________________________________")
pyttsx3.speak("Welcome to Pied Piper Assistant Wizard Version 1 point O!")
name="pullkith"#This is the adjusted spelling of my name for correct pronounciation(not compulsory)
print("Hi, what is your name?")
name2=input()
done =0
yt=0
x=0
flag=0
list=0

while done!=1 :
	if(flag==0):
		pyttsx3.speak("What can i do for you,%s?"%name)#here replace name<->name2
	else :
		pyttsx3.speak("What else can i do for you?")	
	print("\nPlease enter your command: ",end='')
	p = input()
	flag=1
	if(p==" "):
		pyttsx3.speak("I am still waiting for thy command!")
		flag=0
		continue
	
	if(("human" in p) or ("bad" in p) or ("married" in p) or ("robot" in p) or ("old" in p) or ("single" in p)):
		pyttsx3.speak("Please use the program for its intended purposes.")
		pyttsx3.speak("The program is still in developmental stage")
		continue

	if(("do not" in p) or ("dont" in p) or ("don't" in p) or ("fake" in p)) and (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)):
		pyttsx3.speak("Ok i will not perform this task.. as you said.")
		continue
		
	if (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("calculator" in p) or ("calci" in p) or ("calculate"in p)):
		os.system("calc")
		pyttsx3.speak("Job done!")
		continue

	if (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("internet explorer" in p) or ("browser" in p) or ("default web browser" in p) or ("IE" in p) or ("ie" in p)):
		x=os.system("iexplore")
		 
		if(x==0):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("notepad" in p) or ("editor" in p) or ("text editor" in p)):
		os.system("notepad")
		pyttsx3.speak("Job done!")
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("media" in p) or ("player" in p) or ("windows player" in p)):
		x=os.system("wmplayer")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("vlc" in p) or ("media player" in p) or ("windows player" in p)):
		x=os.system("vlc")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("winrar" in p) or ("winzip" in p) or ("compressor" in p)):
		x=os.system("WinRAR")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("terminal" in p) or ("command prompt" in p) or ("cmd" in p)):
		pyttsx3.speak("Please note the terminal launched will not have administrator privileges")
		pyttsx3.speak("Also note you will be exited from the current program.")
		print("To exit from the next terminal window and return to this program, please input exit next time")
		print("Do you still wish to continue, enter yes or no:")
		r=input()
		if ("yes" in r):
			os.system("cmd")
		else :
			print("You have chosen No as your answer")
			continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Notepad++" in p) or ("code notepad" in p) or ("editor" in p)):
		x=os.system("notepad++")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("picasa" in p) or ("image viewer" in p) or ("photo" in p) or ("Picasa" in p) or ("Photo" in p)):
		x=os.system("Picasa3")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue
	

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("steam" in p) or ("valve steam" in p) or ("games" in p)):
		x=os.system("steam")
		if(x==0):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!") 
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("chrome" in p) or ("browser" in p) or ("web browser" in p)):
		x=os.system("chrome")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!") 
		continue
		

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("paint" in p) or ("drawing board" in p)):
		os.system("mspaint")
		pyttsx3.speak("Job done!")
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("codeblocks" in p) or ("Codeblocks" in p)):
		x=os.system("CbLauncher")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Task Manager" in p) or ("task manager" in p) or ("Monitor resources" in p)):
		os.system("Taskmgr")
		pyttsx3.speak("Job done!")
		continue
	
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and ("discord" in p):
		x=os.system("Discord")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue
	
		
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("WebEx" in p) or ("Webex" in p) or ("meeting" in p) or ("webex" in p)):
		x=os.system("ptoneclk")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!") 
		continue

		
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("GTA San Andreas" in p) or ("GTA Sa" in p) or ("San Andreas" in p) or ("GTA OG" in p) or ("gta sa" in p)):
		x=os.system("gta-sa")
		 
		if(x==0):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Firefox" in p) or ("Firefox web browser" in p) or ("browser" in p) or ("Open source browser" in p) or ("firefox" in p)):
		x=os.system("firefox")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!") 
		continue
	
	elif (("search" in p) or ("do a search for me" in p) or ("search this" in p)) :
		print("Please input what you want to search on the web!")
		gg=input()
		webbrowser.open("https://www.google.com/search?q=%s"%gg)
		pyttsx3.speak("Job done!")
		continue
		
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Screeshot tool" in p) or ("Screen clipper" in p) or ("Screenshot" in p)):
		os.system("SnippingTool")
		pyttsx3.speak("Job done!")
		continue
	
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("daemons tool lite" in p) or ("ISO mounter" in p) or ("dt lite" in p) or ("daemon" in p)):
		x=os.system("DTLite")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!")	 
		continue
	
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Oracle VB" in p) or ("Virtual Machine" in p) or ("OVB" in p) or ("Virtualization software" in p) or ("oracle vb" in p)):
		x=os.system("VirtualBox")
		 
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=1
			else :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			pyttsx3.speak("Job done!") 
		continue
	
	elif (("exit" in p) or ("stop" in p) or ("terminate" in p) or ("done" in p) or ("quit" in p) or ("bye" in p) or ("nothing" in p) or ("nope" in p)):
		pyttsx3.speak("Thank you for using Pied Piper Assistant wizard!")
		pyttsx3.speak("Goodluck and Have a nice day")
		print("\n>>>Pied Piper Proprietary Software Limited<<<\n")
		done =1
	
	elif (list==2):
		pyttsx3.speak("You seem to be lost?")
		pyttsx3.speak("Would you like to see the list of available commands?")
		print("Please enter yes or no:",end=' ')
		lost=input()
		if(("yes" in lost) or ("y" in lost) or ("sure" in lost) or ("offcourse" in lost)):
			pyttsx3.speak("Here is the list of all the currently available commands in this program!")
			print()
			print("Program -->command\n")
			print("Calculator -->calculator\nNotepad -->notepad\nCommand Prompt -->cmd\nMS Paint -->paint\nTask Manager -->task manager")
			print("Chrome Broswer -->chrome\nInternet Explore -->ie\nFirefox browser -->firefox\nVLC player -->vlc\nWindows Media Player -->windows media player")
			print("Notepad++ -->Notepad++\nWinRaR -->winrar\nCodeBlocks Editor -->codeblocks\nPicasa3 -->picasa")
			print("Discord -->discord\nWebEx Meeting Client -->webex\nGTA Sanandreas -->gta sa\nSteam Client -->steam\nSnipping Tool -->screenshot")
			print("Web Search -->search\nOracle Virtual Box -->OVB\nDaemons Tools Lite -->daemon")
			
	
	else :
		pyttsx3.speak("Looks like you have entered a invalid command")
		pyttsx3.speak("Do you wish to try again ?")
		list=list+1
		print("Please type yes or no:",end=' ')
		q=input()
		if (("yes" in q) or ("y" in q) or ("sure" in q) or ("offcourse" in q)):
			continue
		elif (("no" in q) or ("n" in q) or ("Im done" in q) or ("nope" in q)) :
			pyttsx3.speak("Thank you for using this program!")
			pyttsx3.speak("Goodluck and Have a nice day")
			print("\n>>>Pied Piper Proprietary Software Limited<<<\n")
			done=1
		else :
			pyttsx3.speak("Invalid input, Please type yes or no")
