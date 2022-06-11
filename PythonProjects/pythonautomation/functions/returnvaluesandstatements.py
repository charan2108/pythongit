import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'certain right'
    elif answerNumber == 2:
        return 'certain left'
    elif answerNumber == 3:
        return 'certainly center'
    elif answerNumber == 4:
        return 'Yes'
    elif answerNumber == 5:
        return 'No'
    elif answerNumber == 6:
        return 'Empty'
    elif answerNumber == 7:
        return 'sweet'
    elif answerNumber == 8:
        return 'Nothing'
    elif answerNumber == 9:
        return 'o'
r =random.randint(1,9) 
hello = getAnswer(r) 
print(hello)  