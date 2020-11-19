from .Homework import Homework
from .exceptions import FailedReindexWarning, ReindexMapError
import os
import warnings



class Homework3(Homework):

    # version="latest"
    def __init__(self, version="latest", no_internet=False):

        valid_versions = ["0.0.1", "0.0.2", "0.0.3"]

        data_files = {
            "0.0.1": [
                "HW3_Ans.txt"
            ],
            "0.0.2": [
                "HW3_Ans.txt"
            ],
            "0.0.3": [
                "HW3_Ans.txt",
                "HW3_Hint.txt"
            ]
        }

        super().__init__(hw_number="hw3", version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        #need to reference file of answer key and hints
        self.answerFile = open("HW18_Ans.txt", "r")
        self.ansArray = self.parseAnswers(self.answerFile)
        self.hintDict = self.parseHints("HW3_Hint.txt")

    def returnAns(self):
        return self.ansArray



