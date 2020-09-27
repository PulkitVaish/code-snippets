
import webbrowser	#To provide links to various websites.
import time			#To generate timing for bad puns
import os			#Give Docker Assistant wings
import pyttsx3		#To bring Docker Assistant to life	
import speech_recognition as sr
import pyaudio
voiceEngine = pyttsx3.init()
done=i=0
oslist=[-1]

#setting up voice recognition feature
r=sr.Recognizer()

newVoiceRate=170#Rate of speaking words has been decremented.
voiceEngine.setProperty('rate', newVoiceRate)
voice_id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
voice_id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voiceEngine.setProperty('voice', voice_id1)

print("_________________________________________________________________________________________________________________")
print("--------------------------------->>> Welcome To Docker Assistant version1 <<<------------------------------------",end='')
print("_________________________________________________________________________________________________________________")
pyttsx3.speak("Welcome To Docker Assistant version 1")
pyttsx3.speak("This is a voice controlled program.")
pyttsx3.speak("Hi, what is your name?")
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("Start speaking please..")
	audio = r.listen(source)
cmd=r.recognize_google(audio)
pyttsx3.speak("Nice to meet you {}".format(cmd))

while(done!=1):
	pyttsx3.speak("What can i do for you?\n")
	print("What can i do for you?")
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("Start speaking please..")
		audio = r.listen(source)
		print("Message received!\n")
	cmd=r.recognize_google(audio)
	if ((("run" in cmd) or ("execute" in cmd) or ("launch" in cmd) or ("start" in cmd) or ("create" in cmd) or ("initiate" in cmd) or ("open" in cmd)) and (("container" in cmd) or ("OS" in cmd) or ("operating system" in cmd))):
		pyttsx3.speak("Please enter the name of OS you want to launch")
		print("Please enter the name of OS you want to launch:",end='')
		osn=input()
		if(osn in oslist[1:]):
			print("OS Name already used,please use a different name!")
			pyttsx3.speak("OS name already used before, please use a different name")
			pyttsx3.speak("List of already used up names is displayed below")
			print("List of already used up names is displayed below:")
			print(oslist[1:])
			pyttsx3.speak("Please enter a different name of OS you want to launch")
			print("Please enter the name of OS you want to launch:",end='')
			osn=input()
		oslist.append(osn)
		pyttsx3.speak("Please select the number corresponding to desired OS image to be used ")
		print("Please select the number corresponding to desired OS image to be used:")
		print("O.S. IMAGE\t VERSION")
		print("1. Centos\tlatest")
		print("2. Centos\t7")
		print("3. Ubuntu\t14.04")
		print("Enter the desired option:",end='')
		osi=input()
		if(osi == "1"):
			webbrowser.open("http://192.168.1.7/cgi-bin/dockerun.py?x={}&y=centos%3Alatest".format(osn))
		elif(osi == "2"):
			webbrowser.open("http://192.168.1.7/cgi-bin/dockerun.py?x={}&y=centos%3A7".format(osn))
		else:
			webbrowser.open("http://192.168.1.7/cgi-bin/dockerun.py?x={}&y=ubuntu%3A14.04".format(osn))
			
	elif ((("stop" in cmd) or ("terminate" in cmd) or ("end" in cmd) or ("close" in cmd)) and (("container" in cmd) or ("os" in cmd) or ("operating system" in cmd))):
		pyttsx3.speak("You will be soon redirected to a webpage, please enter os name which has to be stopped to continue")
		webbrowser.open("http://192.168.1.7/dstop.html")
		
	elif (("nothing" in cmd) or ("done" in cmd) or ("nope" in cmd)):
		pyttsx3.speak("Thank you for using Docker Assistant")
		pyttsx3.speak("Do you want to delete all the containers that were launched during this session?")
		pyttsx3.speak("Please respond with yes or no")
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			print("Start speaking please..")
			audio = r.listen(source)
			print("Message received!\n")
		ch = r.recognize_google(audio)
		print(ch)
		if(ch == "yes"):
			pyttsx3.speak("You will be soon redirected to a webpage please click submit on the webpage to continue")
			webbrowser.open("http://192.168.1.7/dclean.html")
		else:	
			pyttsx3.speak("Please note all the containers will continue to exist after this program exits")
			pyttsx3.speak("In future you must use a name not present in the list below to launch an os")
			print(oslist[1:])
		done=1
	else:
		pyttsx3.speak("Sorry i didn't get you!")
		pyttsx3.speak("Will you like to try again?")
		pyttsx3.speak("Please respond with yes or no")
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			print("Start speaking please..")
			audio = r.listen(source)
			print("Message received!/n")
		choice=r.recognize_google(audio)
		if(choice =="yes"):
			continue
		elif(choice == "no"):
			done=1
			continue
		else:
			pyttsx3.speak("Invalid Choice!")
		
		