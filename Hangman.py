import random
WORDLIST = [""]
updatedWord = ""

def initialize():
    global updatedWord
    global SECRET
    WORDLIST = ['one','two','three','four','five','six','seven','eight','nine','ten']
    SECRET = random.choice(WORDLIST)
    updatedWord = [('_'*len(SECRET))]
   
    print(updatedWord)
    print SECRET
    
    val=0

def test():

    global val

    secret = "BALOON"

    updatedword = ['_','_','_','_','_','_','_']

    for i in range (0, len(Secret)):

        print (updatedWord[1])

    Letter = str(input("What is your guess: "))

    val = Secret.find (Letter)

    del updatedWord[val]

    updatedWord.insert(val, Letter)

    for i in range (0, len(Secret)):

        print(updatedWord[i])

    if Secret.find(Letter) ==-1

        return "Wrong Letter"

def getLetter():
    global letter
    letter = str(raw_input('ENTER YOUR GUESS: '))
    print ('YOUR GUESS: ' + letter)

def fillLetter():
    pos = SECRET.find(letter)
    updatedWord[pos] = letter
    
def ifWon():
    if updatedWord == SECRET:
        print ('You Won!')
    else: 
        getLetter()
        
def main():
    
    initialize()
    getLetter()
    


