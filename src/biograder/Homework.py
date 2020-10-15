from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from src.biograder.Encryptor import Encryptor

class Homework:
    #filepath
    #filehandle

    def __init__(self):
        self.val = ""

    def parseAnswers(self, answerFile):
        tempArray = []
        for ans in answerFile:
            ans = ans.rstrip('\n')
            tempArray.append(ans)
        return tempArray

    def parseHints(self, hintFile):
        #return a dictionary or list or something
        pass

    def submit(self, guess, qNum, studentID):
        #bitGuess = str.encode(guess)
        #encrypt the submission
        #enc_guess = Encryptor().encrypt(bitGuess)

        if self.ansArray[qNum - 1] == guess:
            #add student id google sheet stuff here
            return True
        else:
            return False

    def getHint(self, hintNum):
        #lessen hintNum to highest possible hint value
        pass

