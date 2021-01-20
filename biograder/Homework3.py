from .Homework import Homework
from .exceptions import FailedReindexWarning, ReindexMapError
import os
import warnings



class Homework3(Homework):

    # version="latest"
    def __init__(self, version="latest", no_internet=False):

        valid_versions = ["0.0.3", "1.0.0", "1.0.1"]

        data_files = {
            "0.0.3": [
                "HW3_Ans.txt",
                "HW3_Hint.txt"
            ],
            "1.0.0": [
                "HW3_Ans.txt",
                "HW3_Hint.txt"
            ],
            "1.0.1": [
                "HW3_Ans.txt",
                "HW3_Hint.txt"
            ],
        }

        super().__init__(hw_number="hw3", version=version, valid_versions=valid_versions, data_files=data_files, no_internet=no_internet)
        #need to reference file of answer key and hints
        for file_path in self._data_files_paths:
            path_elements = file_path.split(os.sep)  # Get a list of the levels of the path
            file_name = path_elements[-1]

            if (file_name == "HW3_Ans.txt"):
                self.ansArray = self.parseAnswers(file_path)
            elif (file_name == "HW3_Hint.txt"):
                self.hintDict = self.parseHints(file_path)




