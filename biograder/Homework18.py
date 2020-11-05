from .Homework import Homework
from .exceptions import FailedReindexWarning, ReindexMapError
import os
import warnings



class Homework18(Homework):

    def __init__(self, version="latest", no_internet=False):

        valid_versions = ["0.0.1", "0.0.2"]

        data_files = {
            "0.0.1": [
                "HW18_Ans.txt"
            ],
            "0.0.2": [
                "HW18_Ans.txt"
            ]
        }

        super().__init__(hw_number="18", version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        #need to reference file of answer key and hints
        self.answerFile = open("HW18_Ans", "r")
        self.ansArray = self.parseAnswers(self.answerFile)
        # self.hintFile = open("HW18Hint", "r")
        # self.hintDict = self.parseHints(self.hintFile)

    def printSomething(self):
        print("Something")

    def returnAns(self):
        return self.ansArray



