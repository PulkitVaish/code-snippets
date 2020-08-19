#Welcome to my python program ver 2.0
#Written by Pulkit Vaish
#This version of the program uses print() function to convey messages.
#Pied piper is a fictional company part of my favourite sitcom "Silicon Valley"

import os

print("Welcome to Pied Piper Assistant Wizard !")
done =0
x=0
flag=0

while done!=1 :
	if(flag==0):
		print("What can i do for you?")
	else :
		print("What else can i do for you?")	
	print("Please enter your command: ",end='')
	p = input()
	flag=1
	if (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("calculator" in p) or ("calci" in p) or ("calculate"in p)):
		os.system("calc")
		print("Job done!\n")
		continue

	if (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("internet explorer" in p) or ("browser" in p) or ("default web browser" in p) or ("IE" in p)):
		x=os.system("iexplorer")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("notepad" in p) or ("editor" in p) or ("text editor" in p)):
		os.system("notepad")
		print("Job done!\n")
		print("Can i assist you with anything else?")
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("media" in p) or ("player" in p) or ("windows player" in p)):
		x=os.system("wmplayer")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("vlc" in p) or ("media player" in p) or ("windows player" in p)):
		os.system("vlc")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("winrar" in p) or ("winzip" in p) or ("compressor" in p)):
		os.system("WinRAR")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("terminal" in p) or ("command prompt" in p) or ("cmd" in p)):
		print("Please note the terminal launched will not have administrator privileges.")
		print("Also note you will be exited from the current program.")
		print("To exit from the next terminal window and return to this program, please input exit next time")
		print("Do you want to continue, enter yes or no:")
		r=input()
		if ("yes" in r):
			os.system("cmd")
		else :
			print("You have chosen No as your answer")
			continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("++" in p) or ("code" in p) or ("editor" in p)):
		x=os.system("notepad++")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Picasa" in p) or ("Image viewer" in p) or ("Photo" in p)):
		x=os.system("Picasa3")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue
	

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("steam" in p) or ("valve steam" in p) or ("games" in p)):
		x=os.system("steam")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("chrome" in p) or ("browser" in p) or ("web browser" in p)):
		x=os.system("chrome")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue
		

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("paint" in p) or ("drawing board" in p)):
		os.system("mspaint")
		print("Job done!\n")
		print("Can i assist you with anything else?")
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("codeblocks" in p) or ("C editor" in p)):
		x=os.system("CbLauncher")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue


	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Task Manager" in p) or ("Processes" in p) or ("Monitor resources" in p)):
		os.system("Taskmgr")
		print("Job done!\n")
		print("Can i assist you with anything else?")
		continue
	
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and ("discord" in p):
		x=os.system("Update")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue
	
		
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("WebEx" in p) or ("Webex" in p) or ("meeting" in p)):
		x=os.system("ptoneclk")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue

		
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("GTA San Andreas" in p) or ("GTA Sa" in p) or ("San Andreas" in p) or ("GTA OG" in p)):
		x=os.system("gta-sa")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue

	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Firefox" in p) or ("Firefox web browser" in p) or ("browser" in p) or ("Open source browser" in p)):
		x=os.system("firefox")
		if(x==1):
			print("\nUh oh. We failed to open this program for you.")
			print("Path for this program is not set in your environmental variables.")
			print("To set the path in your device, please follow this link")
			print("\n---->https://www.youtube.com/watch?v=LO0R9oj9Eos\n")
		
		else :
			print("Job done!\n")
		continue
		
		
	elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("start" in p) or ("begin" in p) or ("create" in p) or ("initiate" in p) or ("open" in p) or ("activate" in p)) and (("Screeshot tool" in p) or ("Screen clipper" in p) or ("Screenshot" in p)):
		os.system("SnippingTool")
		print("Job done!\n")
		continue


	elif (("exit" in p) or ("stop" in p) or ("terminate" in p) or ("done" in p) or ("quit" in p) or ("bye" in p) or ("nothing" in p) or ("nope" in p)):
		print("\nThank you for using Pied Piper Job wizard!")
		print("Goodluck and Have a nice day")
		print(">>>Pied Piper Proprietary Software Limited<<<\n")
		done =1
	else :
		print("Looks like you have entered a invalid command")
		print("Do you wish to try again ?")
		print("Please type yes or no:",end=' ')
		q=input()
		if (("yes" in q) or ("y" in q) or ("sure" in q) or ("offcourse" in q)):
			continue
		elif (("no" in q) or ("n" in q) or ("Im done" in q) or ("nope" in q)) :
			voiceEngine.setProperty('voice', voice_id1)
			print("\nThank you for using this program!")
			print("Goodluck and Have a nice day")
			print(">>>Pied Piper Proprietary Software Limited<<<\n")
			done=1
		else :
			print("Invalid input, Please type yes or no")
