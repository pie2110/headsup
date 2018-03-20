myword = "otter"

def start ():
	
	print ("clue:i am silky and ferousious and i like swimming")
	print (" category: animals")
	word = input("guess my word   ")
	checkword(word.lower())
	ss
def checkword(guessedword):
	if guessedword == myword:
		print ("congratualations you won")
	else: 
		print ("you failed")
		tryagain()
def tryagain():
	 word= input ("try again    ")
	 checkword(word.lower())

start()	
	
