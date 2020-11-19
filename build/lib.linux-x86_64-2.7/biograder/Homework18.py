from .Homework import Homework
from .exceptions import FailedReindexWarning, ReindexMapError
import os
import warnings



class Homework18(Homework):

    # version="latest"
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

        super().__init__(hw_number="hw18", version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        #need to reference file of answer key and hints
        self.answerFile = open("HW18_Ans.txt", "r")
        self.ansArray = self.parseAnswers(self.answerFile)
        self.hintDict = self.parseHints("HW18_Hint.txt")

    def returnAns(self):
        return self.ansArray



