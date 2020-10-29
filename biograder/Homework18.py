from biograder import Homework


class Homework18(Homework):

    def __init__(self):
        super().__init__()
        #need to reference file of answer key and hints
        self.answerFile = open("HW18Ans", "r")
        self.ansArray = self.parseAnswers(self.answerFile)
        self.hintFile = open("HW18Hint", "r")
        self.hintDict = self.parseHints(self.hintFile)

    def printSomething(self):
        print("Something")

    def returnAns(self):
        return self.ansArray



