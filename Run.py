import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\r\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
			print user + " typed :" + message
			if "You Suck" in message:
				sendMessage(s, "No, you suck!")
				break
			if "!Join" in message:
				sendMessage(s, "Here is where you apply https://freedom.tm/auth/creatorstudios+apply")
				break
				print(line)
			if "!Twitter" in message:
				sendMessage(s, "Follow us here: https://twitter.com/creatorstudios_")
				break
				print(line)
			if "https://" in message:
				sendMessage(s, "No links allowed")
				break
				print(line)
			
			if "http://" in message:
				sendMessage(s, "No links allowed")
				break
				print(line)
			
			if ".com" in message:
				sendMessage(s, "No links allowed")
				break
				print(line)
			if "!Rules" in message:
				sendMessage(s, "No links allowed!" " " "Be nice!" " " "Don't fight!" " " "Swearing should be at a minimum!")
				break
				print(line)
