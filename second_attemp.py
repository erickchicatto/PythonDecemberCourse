#automate the stuff borings with Python
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'bla bla ...'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber==4:
        return 'reply hazy try again'
    elif answerNumber==5:
        return 'bla bla bla ...'
    
#main
r = random.randint(1,5)
fortune = getAnswer(r)
print(fortune)