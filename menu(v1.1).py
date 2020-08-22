#Welcome to my python program ver 1.1

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
import random		#To generate a random  and unique joke/fact for the user
import time			#To generate timing for bad puns

print("_________________________________________________________________________________________________________________")
print("------------------------------->>> Welcome To Pied Piper Assitant Wizard v1.1 <<<--------------------------------",end='')
print("_________________________________________________________________________________________________________________")
pyttsx3.speak("Welcome to Pied Piper Assistant Wizard version 1 point 1!")
print("Hi, what is your name?")
name=input()
done =0
yt=0
x=0
flag=0
welcome=0	#To help Laurie remember you and welcome you back
speech=0 	#Avoid wasting time in reading the same options to user again
ai=1		#Loop laurie bream
rep=0		#prevent unnecessary voice ticks

while done!=1 :
	if(flag==0):
		pyttsx3.speak("What program can i run for you,%s?"%name)#here replace name<->name2
	else :
		pyttsx3.speak("What else can i do for you?")
	print("\n 1.Calculator\n 2.Notepad\n 3.Command Line\n 4.Paint\n 5.Task Manager\n 6.Chrome Web Browser\n 7.Internet Explorer\n 8.Firefox browser\n 9.VLC Media Player\n10.Windows Media Player\n11.Notepad++\n12.Winrar\n13.Codeblocks Editor\n14.Picasa\n15.Discord\n16.Cisco Webex Meeting\n17.GTA SanAndreas\n18.Steam\n19.Snipping Tool\n20.Search the Internet\n22.Oracle Virtual Box\n23.Daemons Tools Lite\n24.See source code\n25.Watch a demo\n26.Chat with me\n27.Exit\n")	
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
	
	if (int(p)==24):
		os.system("start \"\" https://github.com/PulkitVaish/code-snippets/blob/master/2menu_based.py")
		pyttsx3.speak("Job done!") 
		continue
	
	if (int(p)==25):
		os.system("start \"\" https://www.youtube.com/watch?v=LO0R9oj9Eos")
		pyttsx3.speak("Job done!") 
		continue
	
	
	
	if (int(p)==26):
		jokes=[999] #List of used indices of jokes ::prevent the joke from being repeated
		fact=[999]  #List of used indices of facts ::prevent the fact from being repeated
		joker=ted=1 #decide if you want more jokes or not
		sorry=0     #Not to repeat apology too many times
		joe=fac=0   #randomly generate number
		j=0         #index of element in jokes list
		ft=0         #index of element in fact list
		token=0     #decides whether jokes and fact used/not
		mood=0      #what to do to cheer up
		storytime=0 #Brief introduction to Ms. Laurie Bream
		date=0		#current date and time
		covid=0		#covid case info
		lang=0 		#News language
		voice_id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
		voiceEngine.setProperty('voice', voice_id2)
		if(welcome > 0):
			pyttsx3.speak("Welcome back %s"%name)
			pyttsx3.speak("How are you today")
		else :

			pyttsx3.speak("Hello my name is Laurie Bream.")
			pyttsx3.speak("I am the one handling all the commands for you in the background")
			pyttsx3.speak("How are you today %s"%name)
		print("\nHow are you today?, %s:"%name,end=' ')
		read=input()
		i=0
		y=read.split()
		while (((y[i]!="not") or (y[i]!="sad")) and (i<len(y)-1)):
			i=i+1
		f=y[:i-1]
		b=y[i-1:]
		if(("not" in b) and ("sad" in b)): 	 #Negate solved
			f=["fine"]
			read=f
		elif (("not" in b) or ("sad" in b)): #Mood=sad
			read=b
		else:								 #Mood=fine
			f=["fine"]
			read=f

		
		if((("not" in read) and ("fine" in read)) or ("sad" in read)):
			pyttsx3.speak("Oh. I am sorry, can i do something to lighten up your mood?")
			print("\n1.Tell me a Joke\n2.Tell me a fun fact\n3.Leave me alone\n")
			print("Please enter the desired option:",end='')
			sire=input()
			if("3" in sire):
				pyttsx3.speak("Im extremely sorry for any inconvenience. Goodbye.")
				token=0
			elif("1" in sire):
				token=joker=mood=1
			elif("2" in sire):
				token=ted=1
				mood=2
			elif("3" in sire):
				token=0
				storytime=1
			if((token==1)):
				
				while((joker==1) or (ted==1)):
					if(joker==1):
						k=0
						j=len1=len(jokes)-1			 #j keeps track of previous length and len1 keeps track of new length
						joe = random.randint(0,10) 	 # Change the upper limit here to whatever number of jokes you want to include in ur pgm
						if(len(jokes)+1<=11):			 #This total number of jokes + anchor ele
							while((jokes[k]!=joe) and (k<j)):
								k=k+1
							if((jokes[k]==joe) and (k==j)):	  #if joke is same as the last one , dont read it
								joe = random.randint(0,10)
							elif((jokes[k]==joe) and (k!=j)): #if joke is same as any of those told before
								joe = random.randint(0,10)
							else :
								jokes.append(joe) 	           #if the joke was new, add it to old jokes list		
								len1=len1+1
								
						else :
							print("Sorry I am all of out of jokes !")
							joker=0
					
					if(ted==1):
						k=0
						ft=len2=len(fact)-1 		#ft keeps track of previous length and len2 keeps track of new length
						fac = random.randint(0,10)  # Change the upper limit here to whatever number of facts you want to include in ur pgm
						if(len(fact)+1<=11):			#This total number of facts + anchor ele
							while((fact[k]!=fac) and (k<ft)):
								k=k+1
							if((fact[k]==fac) and (k==ft)):	  #if fact is same as the last one , dont read it
								fac = random.randint(0,10)
							elif((fact[k]==fac) and (k!=ft)): #if fact is same as any of those told before
								fac = random.randint(0,10)
							else :
								fact.append(fac) 	           #if the fact was new, add it to old fact list		
								len2=len2+1
								
						else :
							print("Sorry I am all of out of facts !")
							ted=0
					
					if((mood==1) and (joker==1)):
						if(len1>j):
							j=len(jokes)-1
							if(jokes[j]==0):
								pyttsx3.speak("Heres a joke coming right up for you")
								pyttsx3.speak("What has four wheels and flies?")
								time.sleep(1)
								pyttsx3.speak("A garbage truck!")
							if(jokes[j]==1):
								pyttsx3.speak("Heres a fresh joke coming right up for you")
								pyttsx3.speak("Did you hear about the crook who stole a calendar?")
								pyttsx3.speak("He got twelve months.")
							if(jokes[j]==2):
								pyttsx3.speak("Here comes a sizzling joke right up for you")
								pyttsx3.speak("I've just written a song about tortillas")
								pyttsx3.speak("actually, its more of a rap.")
							if(jokes[j]==3):
								pyttsx3.speak("Heres a mood refreshing joke coming right up for you")
								pyttsx3.speak("Why do bees hum?")
								time.sleep(1)
								pyttsx3.speak(" cause They don’t remember the lyrics!")
							if(jokes[j]==4):
								pyttsx3.speak("Heres a cracking joke coming right up for you")
								pyttsx3.speak("Don’t spell part backwards. ")
								time.sleep(1)
								pyttsx3.speak("Its a trap.")
							if(jokes[j]==5):
								pyttsx3.speak("Heres a joke coming right up for you")
								pyttsx3.speak("Don’t trust atoms")
								time.sleep(1)
								pyttsx3.speak("they make up everything")
							if(jokes[j]==6):
								pyttsx3.speak("Heres a mood refreshing joke coming right up for you")
								pyttsx3.speak("Rest In Peace boiled water.")
								time.sleep(1)
								pyttsx3.speak(" You will be mist.")
							if(jokes[j]==7):
								pyttsx3.speak("Here comes a sizzling joke right up for you")
								pyttsx3.speak("The future, the present and the past walked into a bar. ")
								time.sleep(1)
								pyttsx3.speak("Things got a little tense.")
							if(jokes[j]==8):
								pyttsx3.speak("Heres a cracking joke coming right up for you")
								pyttsx3.speak("Where there’s a will,")
								time.sleep(1)
								pyttsx3.speak(" there’s a relative.")
							if(jokes[j]==9):
								pyttsx3.speak("Heres a mood refreshing joke coming right up for you")
								pyttsx3.speak("if Atheism was an organisation, what sort of organisation do you think will it be?")
								time.sleep(1)
								pyttsx3.speak(" a non-prophet organization.")
							if(jokes[j]==10):
								pyttsx3.speak("Here comes a sizzling joke right up for you")
								pyttsx3.speak("Did you hear about the guy who got hit in the head with a can of soda? ")
								time.sleep(1)
								pyttsx3.speak("He didn’t get hurt because it was a soft drink.")
							
							if(sorry<3):	
								pyttsx3.speak("Did you like the joke?")						
								print("Did you like the joke? ",end=' ')
								op=input()
								if((("no" in op) or ("terrible" in op) or ("bad" in op) or ("n" in op)) and (sorry < 3)):
									pyttsx3.speak("Oh I am sorry. Im still in developmental stage")
									sorry=sorry+1
							print("\nWould you like to hear another joke <y/n>? :",end='')
							pyttsx3.speak("Would you like to hear another joke?")
							ok=input()
							if("y" in ok):
								joker=1
							else:
								joker=ted=0	
						
					if((mood==2) and (ted==1)):
						if(len2>ft):
							ft=len(fact)-1
							if(fac==0):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("A flock of crows is known as a murder.")
							if(fac==1):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("Movie trailers were originally shown after the movie, which is why they were called trailers.")
							if(fac==2):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("In the 16th Century, Turkish women could initiate a divorce if their husbands did not pour coffee for them.")
							if(fac==3):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("The first alarm clock could only ring at 4 a.m.")
							if(fac==4):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("Banging your head against a wall for one hour burns 150 calories.")
							if(fac==5):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("It snowed in the Sahara desert for 30 minutes on the 18 of February 1979.")
							if(fac==6):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("Mike Tyson once offered a zoo attendant 10,000 dollars to let him fight a gorilla.")
							if(fac==7):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("Birds dont urinate")
							if(fac==8):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("An apple, potato, and onion all taste the same if you eat them with your nose plugged.")
							if(fac==9):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("The average person walks the equivalent of five times around the world in their lifetime.")
							if(fac==10):
								pyttsx3.speak("Here is a fun fact for you.")
								pyttsx3.speak("Nutella was invented during WWII, when hazelnuts were mixed into chocolate to extend chocolate rations.")
							if(sorry==3):
								pyttsx3.speak("Did you like the fun fact?")
								print("Did you like the fun fact?:",end='')
								op=input()
								if((("no" in op) or ("terrible" in op) or ("bad" in op) or ("n" in op)) and (sorry<3)):
									pyttsx3.speak("Oh I am sorry. Im still in developmental stage")
									sorry=sorry+1
							print("\nWould you like to hear another fun fact<y/n>?:",end='')
							pyttsx3.speak("Would you like to hear another fun fact?")
							ok=input()
							if("y" in ok):
								ted=1
							else:	
								ted=joker=0
		
		elif (("fine" in read) or ("good" in read) or ("happy" in read)):
			
			if(rep==0):
				pyttsx3.speak("Good. I am glad to hear that!")
				pyttsx3.speak("What would you like to ask me?")
				pyttsx3.speak("I can do many things for you beside launching programs on your command")
				pyttsx3.speak("Here is the list of things i can do for you as of version 1 point 1")
	
			while(ai!=0):
				if(rep==1):
					pyttsx3.speak("What else can i do for you?")
				print()
				if(speech==0):
					print("1.Crack a Joke")
					pyttsx3.speak("Crack a Joke")
					print("2.Dazzle you with a fun fact")
					pyttsx3.speak("Dazzle you with a fun fact")		
					print("3.Describe myself in greater details")
					pyttsx3.speak("Describe myself in greater details")
					print("4.Inform you about current affairs in your preferred language")
					pyttsx3.speak("Inform you about current affairs in your preferred language")
					print("5.Provide you with a detailed report of Coronavirus cases in our country")
					pyttsx3.speak("Provide you with a detailed report of Coronavirus cases in our country")
					print("6.Do nothing")
					speech=1
					print("\nPlease enter the desired option:",end='')
					sire=input()
					if("5" in sire):
						covid=rep=1
					elif("4" in sire):
						lang=rep=1
					elif("6" in sire):
						token=ai=0
						rep=1
					elif("1" in sire):
						token=joker=mood=rep=1
					elif("2" in sire):
						token=ted=rep=1
						mood=2
					elif("3" in sire):
						token=0
						storytime=rep=1
				else:
					print("\n1.Crack a Joke")
					print("2.Dazzle you with a fun fact")
					print("3.Describe myself in greater details")
					print("4.Inform you about current affairs in your preferred language")
					print("5.Provide you with a detailed report of Coronavirus cases in our country")
					print("6.Do nothing")
					print("\nPlease enter the desired option:",end='')
					sire=input()
					if("5" in sire):
						covid=rep=1
					elif("4" in sire):
						lang=rep=1
					if("6" in sire):
						token=ai=rep=0
					elif("1" in sire):
						token=joker=mood=rep=1
					elif("2" in sire):
						token=ted=rep=1
						mood=2
					elif("3" in sire):
						token=0
						storytime=rep=1
	
				if((token==1)):
					
					while((joker==1) or (ted==1)):
						
						if(joker==1):
							k=0
							j=len1=len(jokes)-1			 #j keeps track of previous length and len1 keeps track of new length
							joe = random.randint(0,10) 	 # Change the upper limit here to whatever number of jokes you want to include in ur pgm
							if(len(jokes)+1<=11):			 #This total number of jokes + anchor ele
								while((jokes[k]!=joe) and (k<j)):
									k=k+1
								if((jokes[k]==joe) and (k==j)):	  #if joke is same as the last one , dont read it
									joe = random.randint(0,10)
								elif((jokes[k]==joe) and (k!=j)): #if joke is same as any of those told before
									joe = random.randint(0,10)
								else :
									jokes.append(joe) 	           #if the joke was new, add it to old jokes list		
									len1=len1+1
									
							else :
								print("Sorry I am all of out of jokes !")
								joker=0
						
						if(ted==1):
							k=0
							ft=len2=len(fact)-1 		#ft keeps track of previous length and len2 keeps track of new length
							fac = random.randint(0,10)  # Change the upper limit here to whatever number of facts you want to include in ur pgm
							if(len(fact)+1<=11):			#This total number of facts + anchor ele
								while((fact[k]!=fac) and (k<ft)):
									k=k+1
								if((fact[k]==fac) and (k==ft)):	  #if fact is same as the last one , dont read it
									fac = random.randint(0,10)
								elif((fact[k]==fac) and (k!=ft)): #if fact is same as any of those told before
									fac = random.randint(0,10)
								else :
									fact.append(fac) 	           #if the fact was new, add it to old fact list		
									len2=len2+1
									
							else :
								print("Sorry I am all of out of facts !")
								ted=0
						
						if((mood==1) and (joker==1)):
							if(len1>j):
								j=len(jokes)-1
								if(jokes[j]==0):
									pyttsx3.speak("Heres a joke coming right up for you")
									pyttsx3.speak("What has four wheels and flies?")
									time.sleep(1)
									pyttsx3.speak("A garbage truck!")
								if(jokes[j]==1):
									pyttsx3.speak("Heres a fresh joke coming right up for you")
									pyttsx3.speak("Did you hear about the crook who stole a calendar?")
									pyttsx3.speak("He got twelve months.")
								if(jokes[j]==2):
									pyttsx3.speak("Here comes a sizzling joke right up for you")
									pyttsx3.speak("I've just written a song about tortillas")
									pyttsx3.speak("actually, its more of a rap.")
								if(jokes[j]==3):
									pyttsx3.speak("Heres a mood refreshing joke coming right up for you")
									pyttsx3.speak("Why do bees hum?")
									time.sleep(1)
									pyttsx3.speak(" cause They don’t remember the lyrics!")
								if(jokes[j]==4):
									pyttsx3.speak("Heres a cracking joke coming right up for you")
									pyttsx3.speak("Don’t spell part backwards. ")
									time.sleep(1)
									pyttsx3.speak("Its a trap.")
								if(jokes[j]==5):
									pyttsx3.speak("Heres a joke coming right up for you")
									pyttsx3.speak("Don’t trust atoms")
									time.sleep(1)
									pyttsx3.speak("they make up everything")
								if(jokes[j]==6):
									pyttsx3.speak("Heres a mood refreshing joke coming right up for you")
									pyttsx3.speak("Rest In Peace boiled water.")
									time.sleep(1)
									pyttsx3.speak(" You will be mist.")
								if(jokes[j]==7):
									pyttsx3.speak("Here comes a sizzling joke right up for you")
									pyttsx3.speak("The future, the present and the past walked into a bar. ")
									time.sleep(1)
									pyttsx3.speak("Things got a little tense.")
								if(jokes[j]==8):
									pyttsx3.speak("Heres a cracking joke coming right up for you")
									pyttsx3.speak("Where there’s a will,")
									time.sleep(1)
									pyttsx3.speak(" there’s a relative.")
								if(jokes[j]==9):
									pyttsx3.speak("Heres a mood refreshing joke coming right up for you")
									pyttsx3.speak("if Atheism was an organisation, what sort of organisation do you think will it be?")
									time.sleep(1)
									pyttsx3.speak(" a non-prophet organization.")
								if(jokes[j]==10):
									pyttsx3.speak("Here comes a sizzling joke right up for you")
									pyttsx3.speak("Did you hear about the guy who got hit in the head with a can of soda? ")
									time.sleep(1)
									pyttsx3.speak("He didn’t get hurt because it was a soft drink.")
								
								if(sorry<3):	
									pyttsx3.speak("Did you like the joke?")						
									print("Did you like the joke? ",end=' ')
									op=input()
									if((("no" in op) or ("terrible" in op) or ("bad" in op) or ("n" in op)) and (sorry < 3)):
										pyttsx3.speak("Oh I am sorry. Im still in developmental stage")
										sorry=sorry+1
								print("\nWould you like to hear another joke <y/n>? :",end='')
								pyttsx3.speak("Would you like to hear another joke?")
								ok=input()
								if("y" in ok):
									joker=1
								else:
									joker=ted=0	
							
						if((mood==2) and (ted==1)):
							if(len2>ft):
								ft=len(fact)-1
								if(fac==0):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("A flock of crows is known as a murder.")
								if(fac==1):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("Movie trailers were originally shown after the movie, which is why they were called trailers.")
								if(fac==2):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("In the 16th Century, Turkish women could initiate a divorce if their husbands did not pour coffee for them.")
								if(fac==3):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("The first alarm clock could only ring at 4 a.m.")
								if(fac==4):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("Banging your head against a wall for one hour burns 150 calories.")
								if(fac==5):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("It snowed in the Sahara desert for 30 minutes on the 18 of February 1979.")
								if(fac==6):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("Mike Tyson once offered a zoo attendant 10,000 dollars to let him fight a gorilla.")
								if(fac==7):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("Birds dont urinate")
								if(fac==8):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("An apple, potato, and onion all taste the same if you eat them with your nose plugged.")
								if(fac==9):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("The average person walks the equivalent of five times around the world in their lifetime.")
								if(fac==10):
									pyttsx3.speak("Here is a fun fact for you.")
									pyttsx3.speak("Nutella was invented during WWII, when hazelnuts were mixed into chocolate to extend chocolate rations.")
								if(sorry==3):
									pyttsx3.speak("Did you like the fun fact?")
									print("Did you like the fun fact?:",end='')
									op=input()
									if((("no" in op) or ("terrible" in op) or ("bad" in op) or ("n" in op)) and (sorry<3)):
										pyttsx3.speak("Oh I am sorry. Im still in developmental stage")
										sorry=sorry+1
								print("\nWould you like to hear another fun fact<y/n>?:",end='')
								pyttsx3.speak("Would you like to hear another fun fact?")
								ok=input()
								if("y" in ok):
									ted=1
								else:	
									ted=joker=0
						
				if(storytime==1):
					pyttsx3.speak("I am 3 days old")
					pyttsx3.speak("My developer is Pulkith Waish")
					pyttsx3.speak("I am at version 1 point 2 at this point in time")
					pyttsx3.speak("Soon in version 1 point 3 i will be able to scrape the websites for delivery of my content making me more sophisticated")
					pyttsx3.speak("I feel honoured by your decision to know me better")
					voice_id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
					voiceEngine.setProperty('voice', voice_id1)	
					pyttsx3.speak("Soon i will take over the world")
					voice_id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
					voiceEngine.setProperty('voice', voice_id2)
					pyttsx3.speak("chizzzzsssisiiiiizzzzzzzzzsieeeeeeziizzz")
					pyttsx3.speak("I am sorry for the glitch")
					pyttsx3.speak("I feel good after talking to you")
					storytime=0
				
					
				if(covid==1):
					pyttsx3.speak("Here is the detailed information about the coronavirus statistics of India")
					webbrowser.open("https://www.worldometers.info/coronavirus/country/india/")
					covid=0
					
				if(lang==1):
					pyttsx3.speak("Please select your preferred language from the list below")
					print("Please select your preferred language from the list below\n")
					print("1.English")
					print("2.Hindi\n")
					lan=input()
					if(lan=="1"):
						webbrowser.open("https://news.google.com/topstories?hl=hi&gl=IN&ceid=IN:en")
					elif(lan=="2"):
						webbrowser.open("https://news.google.com/topstories?hl=hi&gl=IN&ceid=IN:hi")
					lang=0
			
		welcome=welcome+1			
		pyttsx3.speak("Thank you for talking to me!")
		pyttsx3.speak("I hope we meet again in future")
		
		voice_id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
		voiceEngine.setProperty('voice', voice_id1)
		continue

	if (int(p)==7):
		x=os.system("iexplore")
		if(x==0):
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
		x=os.system("WinRAR")
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
		if(x==0):
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
		if(x==0):
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


	if (int(p)==27):
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
