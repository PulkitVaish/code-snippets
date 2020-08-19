#Welcome to my python program ver 4.0
#Written by Pulkit Vaish
#This version of program uses pyttsx3 module's speak function to convey messages and is menu driven.
#Note when using terminal inside a terminal, give 24 and exit commmands alternatively till the tiltle bar displays only file opened.
#Pied piper is a fictional company,part of my favourite sitcom "Silicon Valley".


import webbrowser


import pyttsx3
#Rate of speaking words has been decremented.
voiceEngine = pyttsx3.init()
newVoiceRate=150
voiceEngine.setProperty('rate', newVoiceRate)


import os

pyttsx3.speak("Welcome to Pied Piper Assistant Wizard !")

done =0
yt=0
x=0
flag=0

while done!=1 :
	if(flag==0):
		pyttsx3.speak("What can i do for you?")
	else :
		pyttsx3.speak("What else can i do for you?")
	print("\n 1.Calculator\n 2.Notepad\n 3.Command Line\n 4.Paint\n 5.Task Manager\n 6.Chrome Web Browser\n 7.Internet Explorer\n 8.Firefox browser\n 9.VLC Media Player\n10.Windows Media Player\n11.Notepad++\n12.Winrar\n13.Codeblocks Editor\n14.Picasa\n15.Discord\n16.Cisco Webex Meeting\n17.GTA SanAndreas\n18.Steam\n19.Snipping Tool\n20.Search the Internet\n22.Oracle Virtual Box\n23.Daemons Tools Lite\n24.Exit\n")	
	print("Please choose the desired option: ",end='')
	p = input()
	flag=1
	if(" " in p) :
		print("Still waiting for thy command!")
		continue
	if (int(p)==1):
		os.system("calc")
		pyttsx3.speak("Job done!") 
		continue

	if (int(p)==7):
		x=os.system("iexplorer")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue

	if (int(p)==2):
		os.system("notepad")
		pyttsx3.speak("Job done!")
		 
		continue

	if (int(p)==10):
		x=os.system("wmplayer")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue

	if (int(p)==9):
		os.system("vlc")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue


	if (int(p)==12): 
		os.system("WinRAR")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue



	if (int(p)==3):
		pyttsx3.speak("Please note the terminal launched will not have administrator privileges")
		pyttsx3.speak("Also note you will be exited from the current program.")
		print("To exit from the next terminal window and return to this program, please input exit next time")
		print("Do you still wish to continue, please enter yes or no:")
		r=input()
		if ("yes" in r):
			os.system("cmd")
			
		else :
			print("You have chosen No as your answer")
			continue
		continue


	if (int(p)==11): 
		x=os.system("notepad++")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue


	if (int(p)==14):
		x=os.system("Picasa3")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue

	

	if (int(p)==18):
		x=os.system("steam")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue



	if (int(p)==6):
		x=os.system("chrome")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue

		

	if (int(p)==4):
		os.system("mspaint")
		pyttsx3.speak("Job done!")
		continue


	if (int(p)==13):
		x=os.system("CbLauncher")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue


	if (int(p)==5): 
		os.system("Taskmgr")
		pyttsx3.speak("Job done!")
		continue
	
	if (int(p)==15):
		x=os.system("Discord")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue

		
	if (int(p)==16): 
		x=os.system("ptoneclk")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue


		
	if (int(p)==17):
		x=os.system("gta-sa")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue


	if (int(p)==8):
		x=os.system("firefox")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue

		
		
	if (int(p)==19):
		os.system("SnippingTool")
		pyttsx3.speak("Job done!")
		 
		continue


	if (int(p)==24):
		pyttsx3.speak("Thank you for using Pied Piper Assistant wizard!")
		pyttsx3.speak("Goodluck and Have a nice day")
		print("\n>>>Pied Piper Proprietary Software Limited<<<\n")
		done =1
		break

	if (int(p)==20):
		print("Please input what you want to search on the web!")
		gg=input()
		webbrowser.open("https://www.google.com/search?q=%s"%gg)
		pyttsx3.speak("Job done!")
		continue
	
	if (int(p)==22):
		x=os.system("VirtualBox")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue
	
	
	if (int(p)==23):
		x=os.system("DTLite")
		if(x==1):
			pyttsx3.speak("Oh no. We failed to open this program for you.")
			pyttsx3.speak("Path for this program is not set in your environment variables")
			if(yt==0):
				print("Do you want to learn how to set the path now,(y/n): ?")
				y=input()
				if("y" in y):
					os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
					yt=yt+1
			elif(yt==1) :
				pyttsx3.speak("To set the path in future in your device, please follow this link")
				print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
			else :
				break;
		
		else :
			pyttsx3.speak("Job done!")
			 
		continue
	
		 
	else :
		pyttsx3.speak("Invalid Entry")
		pyttsx3.speak("Do you wish to try again ?")
		print("Please type yes or no:",end=' ')
		q=input()
		if (("yes" in q) or ("y" in q) or ("sure" in q) or ("offcourse" in q) or("ye" in q)):
			continue
		elif (("no" in q) or ("n" in q) or ("Im done" in q) or ("nope" in q) or ("nah" in q)) :
			pyttsx3.speak("Thank you for using this program!")
			pyttsx3.speak("Goodluck and Have a nice day")
			print("\n>>>Pied Piper Proprietary Software Limited<<<\n")
			done=1
		else :
			pyttsx3.speak("Invalid input, Please type yes or no")
