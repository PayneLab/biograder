from src.biograder.Encryptor import Encryptor

class Homework:


    def __init__(self):
        self.val = ""

    def parseAnswers(self, answerFile):
        tempArray = []
        for ans in answerFile:
            ans = ans.rstrip('\n')
            tempArray.append(ans)
        return tempArray

    def parseHints(self, hintFile):
        #return a dictionaryor list or something
        pass

    def submit(self, guess, qNum, studentID):
        #encrypt the submission
        enc_guess = Encryptor().encrypt(guess)
        print(enc_guess)
        if self.ansArray[qNum - 1] == enc_guess:
            return True
        else:
            return False

    def getHint(self, hintNum):
        #lessen hintNum to highest possible hint value
        pass

